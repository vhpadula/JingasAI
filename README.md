# JingasAI
DIY home assistant and automation system. This project should implement a local 'Alexa' that runs on a Raspberry Pi.

This project was inspired by this YouTube video: https://www.youtube.com/watch?v=ob0p7G2QoHA&t=3s

# Architecture
The JingasAI has the following design:
![aisystem](https://github.com/vhpadula/JingasAI/assets/64943143/304904ba-b96b-4eda-bf0b-5ab96ca36046)

Which contains the following AI models:
## 1. Wake Word Detection
The Wake Word Detection module implements a Binary Classification Model in order to turn JingasAI on via voice prompt of the keyword "Jingas". Inside the model, A Recurrent Neural Network (RNN) is implemented to continuously hear audio and detect the keyword (1) inside background noise (0).
## 2. Speech Recognition
## 3. Natural Language Processing
## 4. Speech Synthesis

## Controller
The AI models are orchestrated by the **Controller**, that also connects them to the **Skills** that the Assistant can perform

## Skills
The Skillset of JingasAI should be fully scalable, but for now, it will refrain to:
- Turning on and off a smart outlet, which will have a reading lamp connected. JingasAI should be able to follow simple voice commands refering to this outlet as the lamp, and also implement a routine (e.g turning on the lamp at 22:00 and turning it off by 23:00, while giving a voice prompt to enable the user to disable this automation)

