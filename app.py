import streamlit as st
import pickle


with open("iris_model.sav", "rb") as f:
    model, scaler = pickle.load(f)

st.title("🌸 Iris Flower Prediction App")


sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, step=0.1)
sepal_width  = st.number_input("Sepal Width (cm)", min_value=0.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, step=0.1)
petal_width  = st.number_input("Petal Width (cm)", min_value=0.0, step=0.1)

if st.button("Predict"):
    
    sample = [[sepal_length, sepal_width, petal_length, petal_width]]
    sample_scaled = scaler.transform(sample)

   
    prediction = model.predict(sample_scaled)
    target_names = ["Setosa", "Versicolor", "Virginica"]

    st.success(f"🌼 Predicted Flower: **{target_names[prediction[0]]}**")
