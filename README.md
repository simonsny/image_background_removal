----------------------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/60827480/121077339-cd3aa200-c7d7-11eb-9d7c-b7b2b3ff5b80.png)

<p> <strong> An applied AI UseCase by Faktion and Becode to remove the background in seconds! </strong> </p>
----------------------------------------------------------------------------------------------------------------

---

## **Table of Contents**
Your sections headers will be used to reference the location of destination.

- [Author Info](#author-info)
- [Description](#description)
- [How To Use](#how-to-use)
- [Repo Artitecture](#repo-artitecture)
- [Next Step](#next-step)
- [License](#license)

---

---

![image](https://user-images.githubusercontent.com/60827480/119011524-70488a80-b995-11eb-8ddd-55f7c9363572.png)

---

This project outcome belongs to **[Arlene Postrado](https://github.com/arlene14ko)**, **[Daniel Mendoza](https://github.com/danielmendoza4213)**, **[Louan Mastrogiovanni](https://github.com/Louan-M)** and **[Martin Makyeme](https://github.com/makyeme)** who are currently Junior Data Scientists/AI Operators in making at BeCode's Theano 2.27 promotion.

- Repository: `yoga_pose`
- Type of challenge: `Learning`
- Level: `Junior Data Scientist`
- Duration: `5 days`
- Deadline : `19/05/21 5:00 PM`
- Team challenge: `Group Project`
- Deployment Strategy: `Github page and Flask`
- Promotion : `AI Theano 2`
- Coding Bootcamp: `Becode Artificial Intelligence (AI) Bootcamp`

---

## Mission Objectives

- Be able to work with computer vision libraries, and techniques for tracking poses on images on videos
- Be able to explore the pre-trained models for pose tracking on live and streaming media
- Be able to predict Yoga poses in real time
- Be able to use Neural Networks and Machine Learning models
- Be able to deploy the models for end customers

---

## The Mission

YogaLive is a platform that provides yoga classes virtually. YogaLive is looking for a solution to improve the quality of their services, the main challenge they face is to analyse how students are performing the different poses in a normal yoga class. Being virtual and live classes, it can be difficult for teachers and students to know how well the poses are being performed, this can be due to both the number of students and technical issues such as the quality of the video

The company has provided us with sample images of different poses performed by one of their teachers, in order to obtain a model that can recognise the type of pose, estimate the duration of each pose and how many times this pose has been performed. If possible also a model to get a dayly, weekly or monthly student report.

Update: Data has been increase with google images to test models

---

### Table of Contents

- Packages Requirements
- Repository
- Visual
- Pending things to do
- Collaboration

---

## About the Repository

This is a repository is about developing a model that is able to predict a yoga pose using pretrained Convolutional Neural Networks and the computer vision libraries and techniques.

This project is currently deployed locally, if you wanted to try to run this on your own and you dont have a GPU on your computer, you can use [Google Colab](https://colab.research.google.com/) as it needs a lot of computing power.

**Here is a sample dashboard:**!

![image](https://user-images.githubusercontent.com/60827480/119103353-5baed580-ba1b-11eb-9537-4cdc7afc5376.png)


---

### Repository

This has 2 versions:

1. You can run this program locally using the **app.py**
2. If you dont have a GPU, you can run the **YogaLive_app_py.ipynb** notebook using [Google Colab](https://colab.research.google.com/).

**0. Exploration Phase folder**

- This is where the exploration about the domain is done.
- This currently has 1 notebook namely:

  1. **landmark_from_images.ipynb**
     - this is where we explored how to get the landmarks in an image using mediapipe
  2. **real time prediction.ipynb**
     - this is where we explored how to get the landmarks with the test video

**1. MACHINE LEARNING folder**

1. **Creating the training dataset.ipynb**

   - this is the notebook where we first created our dataset using MediaPipe and getting those landmarks, saving those landmarks in a csv file and creating a Machine Learning Model using that csv file

2. **SVM.ipynb**

   - this is the notebook where we created the Machine Learning Model

3. **yoga_poses_model.pkl**
   - this is the saved Machine Learning model using pickle and this used the MediaPipe landmarks

**2. NEURAL NETWORK folder**

1. **CNN_Model.py**

   - this is where our CNN model was created and was later used as our model to get the pose analysis

2. **VGG16.ipynb**

   - this is the pretrained CNN model which we used to create our model

3. **final_model folder**
   - this folder contains the final model of our CNN, but we did not upload it because it is too heavy. If you want to know more, dont hesitate to contact us!

**.gitignore**

- is a txt file used for specifying which files/folders does git needs to ignore so it will not upload to github
- This is used because our dataset cannot be uploaded as it is confidential and also our CNN final model was 1.25GB which the Github cannot handle as of the moment
- If you want to have access to our final model, please dont hesitate to send us a message! :)

**static folder**

- this is where the logo and favicon is saved

**templates folder**

- this is where all the html templates are saved
- this has 3 html files namely:

  1.  **layout.html**

      - this is where all the imports for the html is located
      - this is also where the NavBar and the Footer is saved so it will be shown on all pages

  2.  **analyze.html**

      - this is where the the user needs to input the details to be able to analyze the poses
      - it has a tab depending on the user needs:

              - Live tab - allows the user to use live stream video to analyze the pose
              - Upload tab - allows the user to upload a video file to analyzethe pose

  3.  **live_feed.html**
      - this is the page where you will see the video with the analyzed poses and the details of the pose

**app.py**

- You can run this repository on your local computer using this python file
- Flask app containing all the functions for the program to run in flask
- Routes include but not limited to: - route that will ask the user input - route that will show the live feed/stream and predicting the poses
- Functions include but not limited to: - function that get the video, extract frames from that video and predict the the poses - function that calculate the angles

**yogaLive_app_py.ipynb**

- You can run this notebook using [Google Colab](https://colab.research.google.com/)'s GPU
- This notebook contains all the functions for the program to run in Google Colab, it also includes code for you to connect Google Colab with your drive to properly run the code
- Routes include but not limited to: - route that will ask the user input - route that will show the live feed/stream and predicting the poses
- Functions include but not limited to: - function that get the video, extract frames from that video and predict the the poses - function that calculate the angles

**README.md**

- has all the necessary information regarding the project
- It would be highly recommended to read all the information in the README file.

---

## Libraries Used For This Project

**OpenCV** https://opencv.org/

- OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library.
- In this project, OpenCV is used to read the videos and get the frames from each image

**Keras** https://flask.palletsprojects.com/en/1.1.x/

- Keras follows best practices for reducing cognitive load: it offers consistent & simple APIs, it minimizes the number of user actions required for common use cases, and it provides clear & actionable error messages.
- In this project, Keras is used to create the model easier

**MediaPipe** https://mediapipe.dev/

- MediaPipe offers open source cross-platform, customizable ML solutions for live and streaming media.
- In this project, MediaPipe pose is used to extract the landmarks to use it for training our SVM model and also afterwards to get the landmarks to calculate the angles

**Flask** https://flask.palletsprojects.com/en/1.1.x/

- Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries
- In this project, flask is used to create the web dashboard application

**Pandas** https://pypi.org/project/pandas/

- Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
- In this project, pandas is used convert a list to create a dataframe and convert that dataframe to a csv

---

## Clone / Fork This Repository

- This project is open to collaborations as well as forking or cloning for further development. If you wish to clone/fork this repository, you can just click on the repository, then click the Clone/Fork button and follow the instructions.

## P E N D I N G . . .

- We believe that with a bigger dataset, accuracy of the predictions models can be imporved.

![Thank you](https://static.euronews.com/articles/320895/560x315_320895.jpg?1452514624)

### Thank you for reading. Have fun with the code! 🤗




## image_background_removal

Yoga_Pose_Detection
│
│   README.md               :explains the project
│   requirements.txt        :packages to install to run the program
│   .gitignore              :specifies which files to ignore when pushing to the repository
│__   
│   utils                   :directory that contains python files with usefull functions and Classes.
│   │
│   │ preprocessing.py      :python file that contains preprocessing functions. (example file)
│__
│   data                    :directory that contains the data needed for this project (train and test images).
│   │ DUTS-TE               
│   │   │ DUTS-TE-Image
│   │   │ DUTS-TE-Mask 
│   │ DUTS-TR
│   │   │ DUTS-TR-Image
│   │   │ DUTS-TR-Mask 


<p> <strong> "Yoga is the journey of the self, through the self, to the self." -- The Bhagavad Gita </strong> </p>



## **Description**

<p align="justify">
Online Yoga coaching jobs are becoming challenging for the coaches because it's hard for them to keep track of the progress of each one of the participants. They would like to evaluate if the students are doing the poses correctly and provide custom-made training plans but it's hard to do when hundreds are joining the same class.
</p>
<p align="justify">
Project Goal is to to build an application able to track the poses done by the yoga practitioner, measure time, repetitions and evaluate if the poses are done correctly.
The MVP is where the customers receive a report of the yoga poses, which ones were done correctly, and metrics related to time and repetition.
</p>

<p align="justify">
We are using the MediaPipe, one of the cutting edge tech to detect the body position and as for classification we used RandomForest, a Machine Learning model which helps produce a great result.
We came up with many conclusions, as we also tried to attempt many different models to complete the project. Including CNN model, and Neural Network model which is stated to be very advanced and preferred Neural Network AI model for most of the digital visual analysis.
</p>

<br/>

## **Technologies**
<br/>

| Library       | Used to                                        |
| ------------- | :----------------------------------------------|
| Flask         | to scale up to complex applications.           |
| gunicorn      | a Python WSGI HTTP Server for UNIX.            |
| itsdangerous  | to ensure that a token has not been tampered   |
| Jinja2        | a combination of Django templates and python   |
| MarkupSafe    | to mitigates injection attacks                 |
| Werkzeug      | to build all sorts of end user applications    |
| numpy         | to scientific uses                             |
| scipy         | for fast N-dimensional array manipulation      |
| scikit-learn  | for machine learning built on top of SciPy     |
| matplotlib    | for creating visualizations                    |
| pandas        | to work with data structure and manipulate it  |
| mediapipe	| to with different body position 		 |


[**↥ Back To The Top**](#table-of-contents)

---

## **How To Use**

### **Installation** 

`Python Ver. '3.8'`

**Note:** Just use the command below to install the required library with the correct version to run the program smoothly.

`pip install -r requiement.txt`


1. After the required library install basic application can be run by just running `app.py` python script.

2. **(optional: <u>separate training set</u>)** Download import file and move it to `\yoga_gesture_detection\pose_recognition_data\training data\training frames\videos`
3. **(optional: <u>generate different model</u>)** Inside `_Project_Analysis` directory run `body_pose_detection.ipynb`
	* Frame to video
	* Train model separately
	* generate different models for personal testing
4. Run the `app.py` file to host the application locally.


[**↥ Back To The Top**](#table-of-contents)

---

## **Repo Artitecture**
```
Yoga_Pose_Detection
│
│   README.md               :explains the project
│   requirements.txt        :packages to install to run the program
│   .gitignore              :specifies which files to ignore when pushing to the repository
│__   
│   _Project_Analysis       :directory contain all analysis done while doing this project.
│   │
│   │ body_pose_detection.ipynb            :frame-to-video getting coordinates. Classifying Body pose
│   │ Neural_Network_model_training:ipynb  :research and analysis performed for Neural Networking
│   │ Classification.ipynb  :analysing the best ML model to go with for classification
│   │ counting.py           :Performing the reputation and time counts.
│__   
│   data          	    :directory the main video/image features files.
│   │
│   │ coords.csv	    :csv file containing every classification coordinate in image/videos.
│__   
│   main       		    :directory the main video/image features files.
│   │
│   │ pose_detection.py     :main script file to detect the pose and classify it accordingly.
│__   
│   saved_model    	    :directory the saved training model of the classification.
│   │
│   │ body_language.pkl     :pickel/saved file of the trained model.
│__   
│   templates               :directory contain all the main html that work as a dashboard.
│   │
│   │ Dashboard.html        :dashboard for user to view the results.
│   │ index.html            :home page for website, provide the general informations.
│__   
│   upload                  :directory contains all the video file uploaded by the user for analysis.
│
│   app.py                  :python script file to deploy model and html files for web application.
```

[**↥ Back To The Top**](#table-of-contents)

---

## **Next Step**

- Separate Web Dashboard for application performing the analysis, also including real time update.
- Improve Overall analysis Dashboard.
- Use of Neural Network.
- Improve Accuracy with Object detection.
- Improvement of angle detection.

[**↥ Back To The Top**](#table-of-contents)

---
## **License**

Copyright (c) [2021] [Sijal Kumar Joshi, Simon Snyders, Vincent Rolin]

<p align="justify">
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
</p>
<p align="justify">
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
</p>
<p align="justify">
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
</p>

[**↥ Back To The Top**](#table-of-contents)

---

## **Authors Info**

- Linkedin - [Sijal Kumar Joshi](https://www.linkedin.com/in/sijal-kumar-joshi-b1545584/), [Simon Snyders](https://www.linkedin.com/in/simon-snyders-9452aa146/), [Vincent Rolin](https://www.linkedin.com/in/vincent-rolin-/)
- Github   - [Sijal Kumar Joshi](https://github.com/sijal001), [Simon Snyders](https://github.com/simonsny), [Vincent Rolin](https://github.com/RolyVy)

[**↥ Back To The Top**](#table-of-contents)

