# Mildew Detection in Cherry Leaves

## 1. Introduction

**link to the [Dashboard](https://)**

Short Description:<br>
At the core of this project is a collection of different cell images that we've put together very carefully. These images are the building blocks of the study. The main goal is to find out how well deep learning methods can help automatically detect powdery mildew.

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

  - The neural network can achieve an accuracy of at least 96% in distinguishing powdery mildew leaves from non-powdery mildew leaves in the dataset, demonstrating its effectiveness in this task.

- ### Validate
  - The hypothesis will be validated using a TensorFlow model to assess the model's ability to achieve an accuracy of at least 96% in distinguishing powdery mildew leaves from non-powdery mildew leaves in the dataset.

<br><br>

## 5. The rationale to map the business requirements to the Data Visualisations and ML tasks

*- List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.*

  ## Business Understanding:

  **1. The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.**

  - Within our dataset, we have categorized images of both infected and non-infected leaves. In this context, we aim to visually illustrate the distinctions between infected and non-infected leaves.
    - Visualize the average image variability for each class (Infected or not-infected)
    - Visualize the difference between an average infected and an average non-infected cherry leaves
    - Present an image montage for each class

*This will help the client to understand the data*

  **2. The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.**

  - The machine learning task for this project involves binary classification using TensorFlow. The objective is to create a model that can predict whether a cherry leaf is infected or not-infected with powdery mildew. This task falls under supervised learning, as it requires training a model on a labeled dataset with two classes: "Infected" and "not-Infected.
    - The model takes an image of a cherry leaf as input.
    - The result will be a prediction of whether the leaf is infected or not-infected.

_This prediction will be used in an easy to understand dashboard for the client_

## 6. ML Business Case

*- In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course*
  
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

*- List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.*

*- Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).*

## 8. Unfixed Bugs

*- You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.*

## 9. Deployment

### Heroku

- The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## 10. Main Data Analysis and Machine Learning Libraries

*- Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.*

## 11. Credits

*- In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism.*

*- You can break the credits section up into Content and Media, depending on what you have included in your project.*

### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

*- The photos used on the home and sign-up page are from This Open-Source site.*

*- The images used for the gallery page were taken from this other open-source site.*

## Acknowledgements (optional)

*- Thank the people that provided support throughout this project.*
