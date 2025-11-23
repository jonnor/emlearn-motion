
# Notes 

#### Functionality

- Datasets
- Training
- Labeling
- Feature extraction
- Hyperparameter tuning
- Evaluation. Grouping. Class/EventDetection/EventTimeRegression
- Data recording
- Data visualization
- Deployment. Wrapping emlearn
- Model validation
- Error analysis
- Post processing. Filtering, event discretization
- On device learning. For personalization and demos/quickstart

#### Should have

- Benchmarks on standard datasets. With scores and compute requirements
- Examples that run on Zephyr and Arduino. On reference hardware
- Bindings in emlearn-micropython

#### Preprocessing/feature extraction

Exists

- FFT
- Gravity separation, lowpass

TODO

- Axis remapping
- Gravity separation, complimentary filter
- Gravity separation, Mahogny/Madgewick

#### Import from misc repos

- toothbrush. Usecase/training pipeline. Consume emlearn-motion as library
- har_trees in emlearn-micropython. Training pipeline
- leaf-clustering-random-forests. Use emlearn-motion for download/load/normalize

embeddedml. 

- emlearn/activity-reconition.md
- handson/har-chestmount/
- handson/cat-tracker/
- handson/tkeyo-gestures/
- handson/continous-gestures/
- applications/human-activity-recognition.md
- applications/animal-activity-recognition.md
- applications/gesture-recognition.md
- applications/fall-detection.md

## Datasets

#### KU-HAR
https://data.mendeley.com/datasets/45f952y38r/5

#### AGHAR benchmark
https://www.nature.com/articles/s41597-024-03951-4
November 2024

> AGHAR benchmark, a curated collection of datasets for domain adaptation and generalization studies in smartphone-based HAR

> We standardized six datasets in terms of
> accelerometer units, sampling rate, gravity component, activity labels, user partitioning,
> and time window size, removing trivial biases while preserving intrinsic differences

Ku-HAR, MotionSense, RealWorld, UCI-HAR, WISDM

Dataset: https://zenodo.org/records/11992126
https://github.com/H-IAAC/DAGHAR


#### Support in emlearn
Things that would benefit motion, but are useful also outside these usecases.

- .npy support
- MiniRocket feature extractor
- Temporal Convolutional Network (TCN)
- Dynamic Time Warping, DTW+KNN

