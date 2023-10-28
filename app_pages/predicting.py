import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (load_model_and_predict, resize_input_image, plot_predictions_probabilities)


def Predicting():
    st.header("Predicting")
    st.write("---")
    st.info(
        f"* The client is interested in predicting whether a leaf image contains powdery mildew or not "
        f"or not."
        f"\n\n* You can access a dataset of cherry leaf images for prediction. These images are available for download at the following link "
        f"\n\n **[Link](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)**"
    )


    images_buffer = st.file_uploader('upload samples of leaves. You can select multiple samples if needed.',
                                     type='png', accept_multiple_files=True)

    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:

            img_pil = (Image.open(image))
            st.info(f"Leaf Sample: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(
                img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

            version = 'v1'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(
                resized_img, version=version)
            plot_predictions_probabilities(pred_proba, pred_class)

            df_report = df_report.append({"Name": image.name, 'Result': pred_class},
                                         ignore_index=True)

        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(
                df_report), unsafe_allow_html=True)
