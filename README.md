# Mildew Detection in Cherry Leaves

## 1. Introduction

**link to the [Dashboard](https://cherry-leaves-predictor-08aefcc201b6.herokuapp.com/)**

Short Description:<br>
At the core of this project is a collection of various cherry leaf images that we've assembled with great care. These images are the building blocks of the study. The main goal is to determine how effectively deep learning methods can assist in automatically detecting powdery mildew in cherry leaves.

Project Planing:<br>
The project have embraced each phase of the CRISP-DM framework as a pivotal milestone within the project plan.<br>
[Project plan (CRISP-DM)](https://github.com/users/Stojj2/projects/6/views/2)

## 2. Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## 3. Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## 4. Hypothesis and how to validate?

- ### Hypothesis (H1)

  - The neural network can achieve an accuracy of at least 97% in distinguishing powdery mildew leaves from non-powdery mildew leaves in the dataset, demonstrating its effectiveness in this task.

- ### Validate
  - The hypothesis will be validated using a TensorFlow model to assess the model's ability to achieve an accuracy of at least 97% in distinguishing powdery mildew leaves from non-powdery mildew leaves in the dataset.

<br><br>

## 5. The rationale to map the business requirements to the Data Visualisations and ML tasks

### Business Understanding:

**1. The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.**

- Within our dataset, we have categorized images of both infected and non-infected leaves. In this context, we aim to visually illustrate the distinctions between infected and non-infected leaves.
  - Visualize the average image variability for each class (Infected or not-infected)
  - Visualize the difference between an average infected and an average non-infected cherry leaves
  - Present an image montage for each class

_This will help the client to understand the data_

**2. The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.**

- The machine learning task for this project involves binary classification using TensorFlow. The objective is to create a model that can predict whether a cherry leaf is infected or not-infected with powdery mildew. This task falls under supervised learning, as it requires training a model on a labeled dataset with two classes: "healthy" and "powdery_mildew".
  - The model takes an image of a cherry leaf as input.
  - The result will be a prediction of whether the leaf is healthy or has powdery mildew.

_This prediction will be used in an easy to understand dashboard for the client_

## 6. ML Business Case

**1. What are the business requirements?**

- The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.

- The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

**2. Is there any business requirement that can be answered with conventional data analysis?**

- Yes, we can use conventional data analysis to conduct a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.

**3. Does the client need a dashboard or an API endpoint?**

- The client needs a dashboard.

**4. What does the client consider as a successful project outcome?**

- A study showing how to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
- Also, the capability to predict if a cherry leaf is healthy or contains powdery mildew.

**5. Can you break down the project into Epics and User Stories?**

- Yes, the project has been dissected following the CRISP-DM methodology.
  1. [Business understanding](https://github.com/Stojj2/Portfolio-Project-5/milestone/1)
  2. [Data understanding](https://github.com/Stojj2/Portfolio-Project-5/milestone/2)
  3. [Data preparation](https://github.com/Stojj2/Portfolio-Project-5/milestone/3)
  4. [Modeling](https://github.com/Stojj2/Portfolio-Project-5/milestone/4)
  5. [Evaluation](https://github.com/Stojj2/Portfolio-Project-5/milestone/5)
  6. [Deployment](https://github.com/Stojj2/Portfolio-Project-5/milestone/6)

## 7. Dashboard Design

### **1. Summary**

- On this page, we'll provide the user with a brief overview of the project.

  - **Description**

    - Farmy & Foods faces a challenge with powdery mildew in their cherry plantations, leading to a time-consuming manual inspection process. To save time, they're considering implementing an ML system to detect powdery mildew from cherry leaf images. If successful, this approach could be expanded to other crops.

  - **Data**

    - In this project, we possess a dataset containing 4,208 cherry leaf images, with half being healthy and the other half being pre-sorted as infected.

  - **Links**

    - [GitHub Repository](https://github.com/Stojj2/Portfolio-Project-5)
    - [Readme.md](https://github.com/Stojj2/Portfolio-Project-5/blob/main/README.md)
    - [Cherry Leaves Dataset](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)

  - **Requirements**

    1. The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.

    2. The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

- ### **2. Data-Understanding**
  - We'll use data plots to make it simpler to grasp the distinctions between the classes we're aiming to predict.
    - Checkboxes
      1. Average vs. Variability Image
      2. Difference **average Healthy** and **averagy Powdery Mildew**
      3. Image Montage
- ### **3. Predicting**

  - This page is designed for uploading an image of unseen cherry leaf data and utilizing the trained model to make predictions based on it.
  - The prediction will be visualized through a diagram displaying the classes and their corresponding probability levels.
  - This section will also allow users to upload multiple images for prediction and, at the end, export the results to an Excel spreadsheet.

- ### **4. Hypothesis and Validation**

  - This section will present Hypothesis H1 and provide details about the validation process.

  - The Validation section is enclosed within a green-colored box.

- ### **5. Model-Prediction-Analysis**

  - The objective of this section is to showcase the performance of the CNN model.

  - This section will include a chart that visualizes the distribution of labels within the datasets.

  - Two distinct plots, one depicting the accuracy and the other showing the loss. Each plot represents the model's performance at different epochs, allowing for a detailed examination of how accuracy and loss metrics evolve during the training process.

  - The final component on this page will be a calculation of the model's generalized performance based on the **test** set.

## 8. Bugs

1. **Issue with Image Montage Creation in Dashboard**
   - An incident occurred where the validation folder containing picture data was mistakenly removed, causing the montage function to be unable to access the images for creating an image montage.
     - The folder was successfully restored using GitHub's "Browse old repositories" feature.

_During the testing of the dashboard and Jupyter notebooks, no other known bugs were identified._

## 9. Deployment

### Heroku

- The App live link is: [Cherry Leaves Predictor](https://cherry-leaves-predictor-08aefcc201b6.herokuapp.com/)
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## 10. Main Data Analysis and Machine Learning Libraries

- **Numpy**
  - NumPy is at the core of Pandas and Matplotlib, converting images to arrays for analysis and machine learning. It also calculates means and standard deviations, supporting data processing and model training.
- **Pandas**
  - Pandas played a role in creating and managing DataFrames, as demonstrated in the generation of accuracy and loss plots during model training.
- **Matplotlib**
  - In the data augmentation section, we utilized Matplotlib for visualizing the images.
- **Seaborn**
  - Seaborn was helpful in making the image montage because it's great at handling visualizations with multiple axes.
- **Streamlit**
  - Used to build the interactive web dashboard for data presentation and exploration.
- **Tensorflow**
  - Used for our deep learning tasks, especially when working with neural networks for image classification.
- **Keras**
  - Integrated with TensorFlow for building and training the deep learning model.

## 11. Credits

- **CodeInstitute**

  - This project draws inspiration from a project provided by CodeInstitute and incorporates code and concepts from that project. The original project served as a foundational reference for the development and implementation of the current project, allowing for the exploration and application of similar concepts and methodologies.

    [CodeInstitute - Malaria Detector](https://github.com/Code-Institute-Solutions/WalkthroughProject01)

- **Rohit Sharma**

  - My mentor, Rohit Sharma, provided invaluable assistance in project planning and offered constructive feedback throughout the project, guiding me every step of the way.

- **Kaggle**
  - Kaggle played a crucial role in sourcing the necessary data for this project, which had already been shared on the Kaggle platform by CodeInstitute.
