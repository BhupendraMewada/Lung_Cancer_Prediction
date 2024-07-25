#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import nest_asyncio

nest_asyncio.apply()

# rest of your code


import numpy as np
import pickle
import asyncio

# loading the saved model
loaded_model = pickle.load(open(r'C:/Users/Dell/Downloads/capstone/Lung Cancer Prediction with Symptoms/trained_model.pkl', 'rb'))

# creating a function for Prediction
async def Cancer_Prediction(input_data):
    # Make a prediction based on the input
    prediction = loaded_model.predict([input_data])
    # Print the prediction
    if prediction < 0.5:
        return 'The person does not have lung cancer'
    else:
        return 'The person has lung cancer'

def main():
    # giving a title
    st.title('Lung Cancer Prediction Web App')
    
    # getting the input data from the user
    Yellow_Fingers = st.text_input('Yellow Fingers')
    Anxiety = st.text_input('Anxiety')
    Fatigue = st.text_input('Fatigue')
    Wheezing = st.text_input('Wheezing')
    Coughing = st.text_input('Coughing')
    Shortness_of_Breath = st.text_input('Shortness of Breath')
    Swallowing_Difficulty = st.text_input('Swallowing Difficulty')
    Chest_Pain = st.text_input('Chest Pain')
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Lung Cancer Test Result'):
        diagnosis = asyncio.run(Cancer_Prediction([Yellow_Fingers, Anxiety, Fatigue, Wheezing, Coughing, Shortness_of_Breath, Swallowing_Difficulty, Chest_Pain]))
        
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()



# In[ ]:





# In[ ]:




