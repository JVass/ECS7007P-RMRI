"""
Visualizing the hcdf of a section with the true annotations
"""

from hcdf_package.custom_functions import *
import soundfile as sf
from scipy.signal import medfilt


SONG_TO_VISUALIZE = 0
TIME_TO_START = 80.151
TIME_TO_STOP = 	108.016	
NO_OF_SEGMENT = 3


fmin = 110
fmax = 3520
number_of_chroma = 12
number_of_octaves = 5
bins_per_octave = 36
hop_length = 1024
window_size = 8192
FS = 11025
std = 8**(1/2)
peak_estimation_filter_size = 7 # in total samples, half-1 on the right and half-1 on the left

chroma_parameters = {
    "window": window_size,
    "hop": hop_length,
    "fs": FS
}


song_names = ["07 - Please Please Me (2009 Digital Remaster)", "11 - Do You Want To Know A Secret (2009 Digital Remaster)",
            "03 - All My Loving (2009 Digital Remaster)", "06 - Till There Was You (2009 Digital Remaster)",
            "01 - A Hard Day_s Night (2009 Digital Remaster)", "03 - If I Fell (2009 Digital Remaster)",
            "08 - Eight Days A Week (2009 Digital Remaster)", "11 - Every Little Thing (2009 Digital Remaster)",
            "01 - Help! (2009 Digital Remaster)", "13 - Yesterday (2009 Digital Remaster)",
            "01 - Drive My Car (2009 Digital Remaster)", "07 - Michelle (2009 Digital Remaster)",
            "02 - Eleanor Rigby (2009 Digital Remaster)", "05 - Here There And Everywhere (2009 Digital Remaster)",
            "03 - Lucy In The Sky With Diamonds (2009 Digital Remaster)", "07 - Being For The Benefit Of Mr Kite! (2009 Digital Remaster)"]


sample_to_start = int(TIME_TO_START / (1/FS))
sample_to_stop = int(TIME_TO_STOP / (1/FS))

data, fs = sf.read(f"audio_files/{song_names[SONG_TO_VISUALIZE]}.flac")
# Stereo to mono taking the first channel
data = data[:,0]

data = lr.resample(data, orig_sr = fs, target_sr = FS)

data = data[sample_to_start : sample_to_stop]    

if __name__ == "__main__":
    # This is the same as the baseline. They are needed for plotting.
    tonnetz = lr.feature.tonnetz(y = data, 
                                    sr = fs, 
                                    n_chroma = number_of_chroma,
                                    n_octaves = number_of_octaves,
                                    bins_per_octave = bins_per_octave,
                                    hop_length = hop_length,
                                    fmin = fmin,
                                    norm = 1)
    filter_kernel = Gaussian1DKernel(std)
    smoothed_tonnetz = convolve_per_feature(tonnetz, filter_kernel)
    hcdf = harmonic_change_function(tonnetz, euclidean_distance)
    smoothed_hcdf = harmonic_change_function(smoothed_tonnetz, euclidean_distance)
    anno = annotations()
    chord_changes = anno.fetch_changes(song_names[SONG_TO_VISUALIZE])
    test = peak_finder_k_neighbours(smoothed_hcdf,peak_estimation_filter_size)
    indexes_of_peaks = np.where(test==1)
    indexes_of_peaks = indexes_of_peaks[1]

    # Plotting the peaks that were estimated for the smoothed hcdf, the ones that were a hit and the ones that were not and the transcription times as vertical lines
    plt.figure(figsize = (50,10))
    plt.plot(np.squeeze(smoothed_hcdf), label = "Smoothed HCDF")
   
    timestamps_per_frame = np.arange(0,smoothed_hcdf.shape[1]) * hop_length * (1/FS)
    timestamps_per_frame += TIME_TO_START
    for change in chord_changes:
        if change >= TIME_TO_STOP:
            break

        if change >= TIME_TO_START:
            frame_index_for_timestamp = np.where(np.logical_and(change <= timestamps_per_frame + 93e-3, timestamps_per_frame <= change))
            plt.axvline(x = frame_index_for_timestamp[0][0], color = (167/255, 196/255, 242/255), label = 'axvline - full height')

    # get the envelope based on the hilbert transform
    plt.plot(medfilt(smoothed_hcdf[0], kernel_size = 3))

    plt.savefig(f"./output/please_please_me_verse_{NO_OF_SEGMENT}.png")
    plt.close()