"""
sample_demo.py
-------------------------------------------------------------------------
A lightweight demonstration script for evaluating skin cancer images (BCC vs. SCC)
using a deep convolutional neural network backbone (e.g., Xception).

Note: Full training scripts and model weights will be released upon paper publication.
-------------------------------------------------------------------------
"""

import argparse
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.xception import preprocess_input
from tensorflow.keras.preprocessing import image

# Define Class Labels
CLASS_NAMES = ['Basal Cell Carcinoma (BCC)', 'Squamous Cell Carcinoma (SCC)']
IMAGE_SIZE = (299, 299)


def load_and_preprocess_image(img_path: str):
    """
    Loads and preprocesses an input skin lesion image for inference.
    """
    print(f"[INFO] Loading image from: {img_path}")
    img = image.load_img(img_path, target_size=IMAGE_SIZE)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    # Xception-specific preprocessing (scales pixels between -1 and 1)
    preprocessed_img = preprocess_input(img_array)
    return preprocessed_img


def run_demo_inference(img_path: str, model_path: str = None):
    """
    Simulates model inference on a single test image.
    """
    preprocessed_img = load_and_preprocess_image(img_path)

    if model_path:
        print(f"[INFO] Loading model checkpoint from: {model_path}")
        model = tf.keras.models.load_model(model_path)
        prediction_prob = model.predict(preprocessed_img)[0][0]
    else:
        print("[INFO] No model path provided. Running dummy inference for demonstration...")
        # Placeholder probability for demo execution
        prediction_prob = float(np.random.uniform(0.70, 0.95))

    predicted_class = CLASS_NAMES[1] if prediction_prob >= 0.5 else CLASS_NAMES[0]
    confidence = prediction_prob if predicted_class == CLASS_NAMES[1] else (1.0 - prediction_prob)

    print("\n" + "=" * 45)
    print("           INFERENCE RESULTS           ")
    print("=" * 45)
    print(f" Predicted Class : {predicted_class}")
    print(f" Confidence Score : {confidence * 100:.2f}%")
    print("=" * 45 + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Skin Cancer Classification Demo")
    parser.add_argument("--image", type=str, required=True, help="Path to the input skin lesion image")
    parser.add_argument("--model", type=str, default=None, help="Path to trained model file (.h5 or .keras)")

    args = parser.parse_args()
    run_demo_inference(args.image, args.model)
