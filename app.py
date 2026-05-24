import pickle
import numpy as np
import pandas as pd
import streamlit as st
loaded_model=pickle.load(open('/home/loki/Developer/Ml/Project/LogisticRegreesion/FakeNews/model.pkl','rb'))
feature_extreactor=pickle.load(open('/home/loki/Developer/Ml/Project/LogisticRegreesion/FakeNews/feature.pkl','rb'))
def fake_mail_detector(input):
    sample_features = feature_extreactor.transform([input])

    prediction = loaded_model.predict(sample_features)

    if prediction[0] == 0:
        return "Spam"
    else:
        return "Ham"

def main():
    st.title("Fake mail detection") 
    mail_text=st.text_input("Enter the conntent of the mail")
    result=""
    if st.button("Predict"):
        result=fake_mail_detector(mail_text)
    st.success(result)

if __name__=='__main__':
    main()    
              

