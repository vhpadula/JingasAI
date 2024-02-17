# JingasAI
DIY home assistant and automation system. This project should implement a local 'Alexa' that runs on a Raspberry Pi.

This project was inspired by this YouTube video: https://www.youtube.com/watch?v=ob0p7G2QoHA&t=3s

# Architecture
The JingasAI has the following design:
![aisystem](https://github.com/vhpadula/JingasAI/assets/64943143/304904ba-b96b-4eda-bf0b-5ab96ca36046)

Which contains the following AI models:
## 1. Wake Word Detection
The Wake Word Detection module implements a Binary Classification Model in order to turn JingasAI on via voice prompt of the keyword "Jingas". Inside the model, A Recurrent Neural Network (RNN) is implemented to continuously hear audio and detect the keyword (1) inside background noise (0) and signal to the controller to start the speech recognition 

### Datasets
For the background noise, the model will be trained with sounds recorded in my own apartment for an afternoon, and also the Mozilla Common Voice Dataset, which is an open source, multi-language dataset of voices that anyone can use to train speech-enabled applications. I'll be training the model with voices in Portuguese. 
The dataset can be accessed via the link: https://commonvoice.mozilla.org/en/datasets


For the Keyword Detection, it will be trained with my own voice prompts. I've recorded myself saying "Jingas" 100 times.

### The Model
The RNN implements a Long Short Term Memory Model (LSTM) in each of its cells. The LSTM Model used is encoded in the PyTorch Library, and is contained in the **model.py** file. It implements a normalization layer, 2 hidden layers and a linear classifier in the final layer. It also uses dropout in order to prevent overfitting.

### Data Processing
Data Augmentation techniques are used for expanding all datasets. Not only is the keyword data copied multiple times to compensate for the small set, but also all keyword audio waves are converted into Mel-Frequency Cepstral Coefficients (MFCC) spectrogram, That way we can process the audio data as "images", and apply SpecAugment. SpecAugment cuts part of our spectrograms to generate new data. Not only it makes our datasets bigger but it also helps the Neural Network to learn making better decisions with less audio information. This is contained in the **dataset.py** file. Also, for optimizing the training, all audio files need to be split into chunks around the same size. All the files for splitting the audio, and recording and duplicating the wakewords can be found in the **utils** folder

### Training
For training the model the optimizer used is AdamW Algorithm. A Learning Rate Scheduler is also used for avoiding the model to stop learning in a local minimum. The Error function used for Backpropagation in Gradient Descent is a Binary Cross Entropy Cost Function. The training algorithm can be found in the **train.py** file

There were made several "Utils" scripts for splitting, recording and creating the jsons for the data. The repo now contains the trained model which is capable of handling most cases except for the false positives "Pingas" and microphone issues.
![image](https://github.com/vhpadula/JingasAI/assets/64943143/55a46e0c-681d-45eb-8b4b-968a09e084de)

## 2. Speech Recognition
## 3. Natural Language Processing
## 4. Speech Synthesis

## Controller
The AI models are orchestrated by the **Controller**, that also connects them to the **Skills** that the Assistant can perform

## Skills
The Skillset of JingasAI should be fully scalable, but for now, it will refrain to:
- Turning on and off a smart outlet, which will have a reading lamp connected. JingasAI should be able to follow simple voice commands refering to this outlet as the lamp, and also implement a routine (e.g turning on the lamp at 22:00 and turning it off by 23:00, while giving a voice prompt to enable the user to disable this automation)

