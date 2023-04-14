# Multiple-Disease-Prediction-System
Facilitates disease prediction by diagnosing user symptoms. 

**OVERVIEW**

<p align="justify">The multiple disease prediction system is a machine learning-based web application. It makes use of machine learning algorithms to analyze user symptoms and determine whether or not the user is suffering from a particular disease.
Existing systems that facilitate early disease detection make use of either technical parameters or questionnaires. These existing formats are tedious or are presented in a way that is difficult for users to understand. Given the sensitivity of the issue at hand, namely disease prediction, this application has employed simple worded symptoms as a crucial construct. </p>

<p align="justify">The web-application has been developed using the Streamlit framework. Streamlit is a Python framework that makes it easy to create web applications for data science and machine learning projects. It facilitates the creation of interactive web apps with just a few lines of code, and it's designed to be intuitive and easy to use. </p>

Installation procedure for Streamlit-

_Streamlit can be installed using pip._

                  pip install streamlit
                  pip install streamlit-option-menu

_The above commands help install streamlit and streamlit-option-menu. Streamlit requires Python 3.6 or a higher version._

_Streamlit-option-menu facilitates the design of a multi-web page application and customizing the appearance of the sidebar._

**WORKING SUMMARY**

<p align="justify">The multiple disease prediction provides a default 5 symptom entry display. It mandates that the user enter atleast 3 symptoms. Repetition of symptoms is not allowed. Additionally, the user can also enter more symptoms by requesting more input/select boxes.

Three machine learning algorithms have been utilized. They are:
                                                              1. Decision Tree
                                                              2. Random Forest
                                                              3. Naive Bayes
                                                                                                                           
The symptoms entered are fed as input to each of the aforementioned algorithms. Each symptom select box has been provided with a default entry 'None'. The none input is not passed to the machine learning algorithms.</p>

**SOFTWARE USED**

The Spyder IDE has been utilized to write the code for the multiple disease prediction system.

<p align="justify">Installation of Spyder IDE: The preferred method of installation is to install Spyder using Anaconda. By default, Spyder is included in Anaconda.Anaconda can be installed from https://docs.anaconda.com/anaconda/install/windows/ for the windows platform.</p>


**LIBRARIES**



**DEPLOYMENT**

<p align="justify">There are two ways of deploying the Streamlit app. It can be deployed on a local machine or can be made public.
Deployment using localhost is achieved using the Streamlit run command. 

streamlit run "C:\Users\Krishna\Downloads\DISEASE\website.py" 

The above command helps deploy the Streamlit web-app using the localhost.</p> 
