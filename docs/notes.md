
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
- leaf-clustering-random-forests. Dataset download/load/normalize

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

#### Support in emlearn
Things that are useful also outside of motion usecases.

- .npy support
- MiniRocket feature extractor
- Temporal Convolutional Network (TCN)
- Dynamic Time Warping
