import streamlit as st
import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
                                                    load_model_and_predict,
                                                    resize_input_image,
                                                    plot_predictions_probabilities
                                                    )


def ModelPredictionAnalysis():
    st.write("Testing the 'model_prediction_analysis' page and it seems to work fine!")


