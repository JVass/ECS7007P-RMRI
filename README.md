# ECS7007P - RMRI
## Paper comparison

| Paper No | Paper name | Author | Date | Journal/Conference | Dataset | Annotations | Implementation | Comments |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | 
|1 | Musical key extraction from audio | Steffen Pauws | 2004 | ISMIR | 5 CDs with 237 performances of single Piano musical pieces (Not readily available) | Original Key (not readily available) | Soundfile for reading audio files, Custom STFT with pseudo-psychoacoustic filtering, custom preprocessing -> filtering/thresholding, mono audio,   | The dataset and annotations are not available but they can be easily obtained. The custom nature of the method will render every r2g function useless which will result in a new implementation of our methods. |
| 2 | Harmonic change detection for musical chords segmentation | Degani et al | 2015 | IEEE International Conference on Multimedia and Expo (ICME) | 16 beatles songs (R2G FLAC Beatles discography locally) | Annotations for chords, key changes, beats, structural segmentation for the whole Beatles discography (R2G http://isophonics.net/content/reference-annotations-beatles)  | Soundfile for reading audio files, , librosa's cqt function, custom Chromagram generation based on CQT, custom Tonal Centroid mapping (fairly easy implementation) | This paper is heavily influenced by Harte and Sandler [2009] (https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.375.1367&rep=rep1&type=pdf). It is demanding but relatively ok with respect to our capacity imo. |
|3 | Convex non-negative matrix factorization for automatic music structure identification | Nieto et al | 2013 |  IEEE International Conference on Acoustics, Speech and Signal Processing | Beatles Dataset (176 songs - R2G FLAC Beatles discography locally) SALAMI dataset (Audio downloaded via YouTube https://github.com/jblsmith/matching-salami, | Beatles Dataset annotations ( ), SALAMI annotations (https://github.com/DDMAL/salami-data-public)| Soundfile for reading audio files, every other functionality will be custom or we could use beat Synchronous Chromagrams from  pyechonest https://pypi.org/project/pyechonest/ but the documentation is not available :/) | It seems that this requires much more work than 1, 2. Beat synchronous chromagrams are required and are based on  |  

---
## Comments

As for now, it seems that the can be sorted with a descending relevance with respect to the assignment as follows:

1. Harmonic change detection for musical chords segmentation
2. Musical key extraction from audio
3. Convex non-negative matrix factorization for automatic music structure identification

The ordering is based on:

1. The availability of the dataset or if they aren't readily available, which can be obtained with least effort
2. The size of the dataset
3. The ready to go (R2G) functions and packages that are available online which will lower the implementation load we have to bear
4. The clear writing.

---
## To-do list

To be announced when we meet.