import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.summary import Summary
from app_pages.data_understanding import DataUnderstanding
from app_pages.predicting import Predicting
from app_pages.hypothesis_and_validation import HypothesisAndValidation
from app_pages.model_prediction_analysis import ModelPredictionAnalysis

# Create an instance
app = MultiPage(app_name="Cherry Leaves Detector")

# Add your app pages here using .add_page()
app.app_page("1 - Summary", Summary)
app.app_page("2 - Data Understanding", DataUnderstanding)
app.app_page("3 - Predicting", Predicting)
app.app_page("4 - Hypothesis And Validation", HypothesisAndValidation)
app.app_page("5 - Model Prediction Analysis", ModelPredictionAnalysis)

app.run()
