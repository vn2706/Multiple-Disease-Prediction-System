# Multiple-Disease-Prediction-System
Facilitates disease prediction by diagnosing user symptoms.

**OVERVIEW**

The multiple disease prediction system is a machine learning-based web application. It makes use of machine learning algorithms to analyze user symptoms and determine whether or not the user is suffering from a particular disease.
Existing systems that facilitate early disease detection make use of either technical parameters or questionnaires. These existing formats are tedious or are presented in a way that is difficult for users to understand. Given the sensitivity of the issue at hand, namely disease prediction, this application has employed simple worded symptoms as a crucial construct.

The web-application has been developed using the Streamlit framework. Streamlit is a Python framework that makes it easy to create web applications for data science and machine learning projects. It facilitates the creation of interactive web apps with just a few lines of code, and it's designed to be intuitive and easy to use.

Installation procedure for Streamlit-

Streamlit can be installed using pip.

                  pip install streamlit
                  pip install streamlit-option-menu

The above commands help install streamlit and streamlit-option-menu. Streamlit requires Python 3.6 or a higher version.

Streamlit-option-menu facilitates the design of a multi-web page application and customizing the appearance of the sidebar.

** WORKING SUMMARY **

The multiple disease prediction provides a default 5 symptom entry display. It mandates that the user enter atleast 3 symptoms. Repetition of symptoms is not allowed. Additionally, the user can also enter more symptoms by requesting more input/select boxes.

Three machine learning algorithms have been utilized. They are:
                                                              1. Decision Tree
                                                              2. Random Forest
                                                              3. Naive Bayes
                                                                                                                           
The symptoms entered are fed as input to each of the aforementioned algorithms. Each symptom select box has been provided with a default entry 'None'. The none input is not passed to the machine learning algorithms.

SOFTWARE USED: 


