----------------------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/60827480/121077339-cd3aa200-c7d7-11eb-9d7c-b7b2b3ff5b80.png)

<h5> <strong> An applied Artificial Intelligence UseCase by Faktion and Becode to remove the background in seconds using Deep Learning technologies! </strong> </h5>

---

This project outcome belongs to **[Simon Snyders](https://github.com/simonsny)**, **[Louan Mastrogiovanni](https://github.com/Louan-M)** and **[Gülce Padem](https://github.com/gpadem)**, and **[Arlene Postrado](https://github.com/arlene14ko)** who are currently Junior Data Scientists/AI Operators at BeCode's Theano 2.27 promotion.

- Repository: `image_background_removal`
- Type of challenge: `Learning`
- Level: `Junior Data Scientist`
- Duration: `2 weeks`
- Deadline : `10/06/21 4:00 PM`
- Team challenge: `Group Project`
- Deployment Strategy: `Github Page, Google Collab and Flask`
- Promotion : `AI Theano 2`
- Coding Bootcamp: `Becode Artificial Intelligence (AI) Bootcamp`
- Use Case Given By: `[Faktion](https://www.faktion.com/)`

---
## **Table of Contents**
- [Mission Objectives](#mission-objectives)
- [About The Repository](#about-the-repository)
- [Architecture](#architecture)
- [Repository](#repository)
- [How To Use](#how-to-use)
- [Libraries Used For This Project](#libraries-used-for-this-project)
- [Future Plans](#future-plans)
- [Collaboration](#collaboration)
- [Authors Info](#authors-info)

---

## **Mission Objectives**

- Be able to work with computer vision libraries, and techniques to remove the background on images
- Be able to explore the pre-trained models for background removal on image and videos
- Be able to create and deploy a quality background removal API
- Be able to use Neural Networks and Machine Learning models
- Be able to deploy the models for end customers

---

## **About The Repository**
![image](https://user-images.githubusercontent.com/60827480/121079465-6ec2f300-c7da-11eb-80ab-e69e244c9775.png)

<p align="justify">
One of our partner companies gave us a usecase to use Deep Learning technologies to remove the image background of an image. There are already a lot of pretrained models available but our partner would like to have the better quality of the results on the images.
</p>
<p align="justify">The goal is to train our own model or use transfer learning to create a model that can give a quality result and also a result that is fast and reliable. We were given the [DUTS Image dataset](http://saliencydetection.net/duts/) to train and test on and also 15 High Quality images that the client chose.</p>

<p align="justify"> ------ Conclusion here -----
</p>
<p align = "justify">This project is currently deployed locally, if you wanted to try to run this on your own and you dont have a GPU on your computer, you can use [Google Colab](https://colab.research.google.com/) as it needs a lot of computing power.</p>

<br/>

**Here is a sample dashboard:**!
 ---------------- SAMPLE HERE ----------------

---
## **Architecture**

Image_Background_Removal
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


---

## **How To Use**

### **Installation** 

`Python Ver. '3.8'`
---add other stuff here -----


---

## **Repository**


**README.md**

- has all the necessary information regarding the project
- It would be highly recommended to read all the information in the README file.


------------- ADD OTHER STUFF HERE ----------

---

## **Libraries Used For This Project**

**OpenCV** https://opencv.org/

- OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library.
- In this project, OpenCV is used to read the image and calculate the erosion and dilation for the trimap

**Keras** https://flask.palletsprojects.com/en/1.1.x/

- Keras follows best practices for reducing cognitive load: it offers consistent & simple APIs, it minimizes the number of user actions required for common use cases, and it provides clear & actionable error messages.
- In this project, Keras is used to create the model easier

**Flask** https://flask.palletsprojects.com/en/1.1.x/

- Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries
- In this project, flask is used to create the web dashboard application


------------- ADD OTHER STUFF HERE ----------

---

## **Future Plans**

--- add stuff here-------

---

## **Collaboration**

- This project is open to collaborations as well as forking or cloning for further development. If you wish to clone/fork this repository, you can do so by clicking on the repository, then click the Clone/Fork button and follow the instructions.
---

## **Authors Info**

- Linkedin - **[Simon Snyders](https://www.linkedin.com/in/simon-snyders-9452aa146/)**, **[Louan Mastrogiovanni](https://www.linkedin.com/in/louan-mastrogiovanni-9a0a46143/)** and **[Gülce Padem](https://www.linkedin.com/in/gulce-padem/)**, and **[Arlene Postrado](https://www.linkedin.com/in/arlene-postrado/)**
- Github   - **[Simon Snyders](https://github.com/simonsny)**, **[Louan Mastrogiovanni](https://github.com/Louan-M)** and **[Gülce Padem](https://github.com/gpadem)**, and **[Arlene Postrado](https://github.com/arlene14ko)**

---

![Thank you](https://static.euronews.com/articles/320895/560x315_320895.jpg?1452514624)

### Thank you for reading. Have fun with the code! 🤗

[**↥ Back To The Top**](#table-of-contents)

---


