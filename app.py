# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 15:07:22 2023

@author: Kalpesh
"""

import numpy as np
import pickle
import streamlit as st

model = pickle.load(open('model1.pkl','rb'))

#creating a function for prediction

def prediction(input_data):
    #input_data = (8.316765884214679,214.37339408562252,22018.417440775294,8.05933237743854,356.88613564305666,363.2665161642437,18.436524495493302,100.34167436508008,4.628770536837084)
    input_data = (7.628552723143854,156.79369424379345,26244.036907954305,8.337610433523373,255.04319358074315,495.9669861271219,13.633974380958477,65.60484124722676,4.182057147919716)
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'Water is not Potable'
    else:
      return 'Water is Potable'
  
    
def main():
    #giving a title
    st.title('Water Potability Prediction')
    
    #getting input data
    
    pH = st.text_input("pH")
    Hardness = st.text_input("Hardness")
    Solids = st.text_input("Solids")
    Chloramines = st.text_input("Chloramines")
    Sulfate = st.text_input("Sulfate")
    Conductivity = st.text_input("Conductivity")
    Organic_carbon = st.text_input("Organic_carbon")
    Trihalomethanes = st.text_input("Trihalomethanes")
    Turbidity = st.text_input("Turbidity")
    
    
    #code for prediction
    
    potability = ''
    
    #creating button for Prediction
    
    if st.button('Prediction'):
        potability = prediction([pH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity])
    
    st.success(potability)
      
            
      
      
      
if __name__ == '__main__':
    main()
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
