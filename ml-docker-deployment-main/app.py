import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.title("Mushroom Classifier 🍄")

# Load dataset
df = pd.read_csv("mushrooms.csv")
X = df.drop(columns=['class'])
y = df['class']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

st.write("Model is trained and ready!")
