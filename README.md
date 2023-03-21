# Emotify 🎶🎶
## ABSTRACT :
* Song recommendation has a long history, but in most scenarios, recommendation is determined by understanding the user's preferences over a period of time, such as looking at their previous song preferences, listening time, etc. .
* We propose a new song recommendation method, where a person's emotion is determined from their photo and the predicted emotion
## Description :
* We first process the image of the user taken as an input with the help of React-webcam(npm). This captured image is then made available for the CNN in combination with DNN to make a prediction whether the current mood of the user is 'Happy' ,'Angry' or 'Sad'. The image is sent to a python backend (flask) where it uses the already trained H5 file to give prediction.
## Dataset:
* The dataset contain 35,685 examples of 48x48 pixel gray scale images of faces divided into train and test dataset. Images are categorized based on the emotion shown in the facial expressions (happiness, neutral, sadness, anger, surprise, disgust, fear).
