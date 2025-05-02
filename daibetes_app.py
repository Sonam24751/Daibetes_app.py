import streamlit as st
import joblib


loaded_model = joblib.load('daibetes.pkl')

def main():
    st.markdown("<h1 style='color:grey;'>Diabetes Prediction</h1>", unsafe_allow_html=True)

    glucose = st.number_input('Glucose', min_value=0, max_value=300, value=120)
    blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=180, value=70)
    
    insulin = st.number_input('Insulin', min_value=0, max_value=900, value=80)
   
    
    age = st.number_input('Age', min_value=1, max_value=120, value=30)

    if st.button('Predict'):

        input_data = [[ glucose, blood_pressure,
                       insulin,   age]]
        
        prediction = loaded_model.predict(input_data)
        
        if prediction[0] == 1:
            st.error("The model predicts: Diabetic")
        else:
            st.success("The model predicts: Not Diabetic")

if __name__ == '__main__':
    main()
