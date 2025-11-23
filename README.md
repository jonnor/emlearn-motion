
# emlearn-motion

Framework for

## Status
**EXPERIMENTAL**. Not ready for use

## Scope

emlearn-motion

#### Tasks

Aim to support most tasks that are relevant to do from motion data (accelerometer/gyro/IMU)
on wearable devices. For example:

- Human Activity Recognition (HAR)
- Animal Acticity Detection
- Exercise Recognition
- Gesture Recognition
- Repetition counting. Steps. Exercise etc
- Fall detection

#### Functionality

- Deploy ML models to device using emlearn

## Datasets


#### UCI-HAR

[UCI-HAR dataset](https://www.archive.ics.uci.edu/dataset/341/smartphone+based+recognition+of+human+activities+and+postural+transitions).
The classes are by default limited to the three static postures (standing, sitting, lying) plus three dynamic activities (walking, walking downstairs, walking upstairs).
The data is from a waist-mounted smartphone.
Samplerate is 50Hz.
By default only the accelerometer data is used (not the gyro).

![UCI HAR classes](./img/UCI-HAR-dataset.png)

#### Excercise detection (custom)

This dataset was collected using the data recording tools described further below.
The data contains 3 kinds of exercises, plus "other" non-exercise activity.
The classes are: Jumping Jacks, Squats, Lunges, Other.
The data was collected using an M5Stick C PLUS 2, mounted on the wrist like a watch (button facing forward).

![Exercise detection](./img/har_exercises_classes.png)

## Installing

```
FIXME: document 
```

## Usage


Install requirements
```
pip install .
```

Download training data
```
python -m emlearn_motion.datasets.download --dataset uci_har
```

Run training process
```
python emlearn_motion.train --dataset uci_har
```

Deploy to device

```
FIXME: document
```


## Documentation

```
FIXME: coming

## Recording motion data for custom tasks
## Labeling recorded motion data
## Train model on custom dataset
```


