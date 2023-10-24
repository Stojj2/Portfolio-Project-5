import streamlit as st


def Summary():
    st.header("Summary")

    st.info(
        f"**Description**\n\n"
        f"* Farmy & Foods faces a challenge with powdery mildew in their cherry plantations, leading to a time-consuming manual inspection process. To save time, they're considering implementing an ML system to detect powdery mildew from cherry leaf images. If successful, this approach could be expanded to other crops. \n\n"
        f"* At the core of this project is a collection of various cherry leaf images that we've assembled with great care. These images are the building blocks of the study. The main goal is to determine how effectively deep learning methods can assist in automatically detecting powdery mildew in cherry leaves."
        )

    st.info(
        f"**Data**\n\n"
        f"* In this project, we possess a dataset containing 4,208 cherry leaf images, with half being healthy and the other half being pre-sorted as infected."
        )

    st.info(
        f" **Links**\n\n"
        f"[GitHub Repository](https://github.com/Stojj2/Portfolio-Project-5)\n\n"
        f"[Readme.md](https://github.com/Stojj2/Portfolio-Project-5/blob/main/README.md)\n\n"
        f"[Cherry Leaves Dataset](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)"
        )


    st.info(
        f"**Requirements**\n\n"
        f"* The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew."
        f"\n\n"
        f"* The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew."
    )
