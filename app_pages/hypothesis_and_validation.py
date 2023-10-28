import streamlit as st


def HypothesisAndValidation():
    st.header("Hypothesis And Validation")
    st.write("---")

    st.info(
        f"**Hypothesis (H1)**"
        f"\n\nThe neural network can achieve an accuracy"
        f"of at least 97% in distinguishing powdery mildew leaves from non-powdery mildew leaves in the dataset,"
        f" demonstrating its effectiveness in this task."
        )
    

    st.success(
        f"**Model performance (H1)** "
        F"\n\n The training of the model was conducted with various batch sizes, and it became evident"
        f" that a batch size of 15 yielded the highest accuracy"
        f" on the ** test_set**. Therefore, we can confidently conclude that the hypothesis(H1) has been validated based on this results"
        f""
        f"\n\n"
        f"\n\n - bach_size of 10 - 2s 17ms/step - loss: 0.0276 - accuracy: 0.9953"
        f"\n\n - **bach_size of 15 - 1s 24ms/step - loss: 0.0081 - accuracy: 0.9964 **"
        f"\n\n - bach_size of 20 - 2s 28ms/step - loss: 0.0451 - accuracy: 0.9882"
        f"\n\n - bach_size of 25 - 2s 40ms/step - loss: 0.0123 - accuracy: 0.9953"
        )
