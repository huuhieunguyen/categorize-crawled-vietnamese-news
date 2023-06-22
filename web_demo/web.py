import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from utils.util import preprocess
import joblib
import seaborn as sns
import os

# Path to the folder containing the feature extraction joblib files
extractor_path = "./extractor"
countVR_path = "countVR"
tfidf_path = "tf_idf"

# Concatenate the folder path with the subfolder directory
countVR_full_path = os.path.join(extractor_path, countVR_path)
tfidf_full_path = os.path.join(extractor_path, tfidf_path)

# Get the list of files in the folder
countVR_files = os.listdir(countVR_full_path)
tfidf_files = os.listdir(tfidf_full_path)

# Path to the folder containing the model joblib files
model_path = "./model_ckpt"

# Get the list of files in the model folder
model_files = os.listdir(model_path)
#########################################################################################################

# function to retrieve a key by its corresponding value in a dict
def get_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None

# Define the available input options and corresponding meaning
input_options = {
    'All': 'Đầy đủ bài báo',
    'Title': 'Tiêu đề ',
    'Description': 'Mô tả',
    'Content': 'Nội dung'
}
# Define the available feature exraction options and corresponding meaning
feature_extract_options = {
    'tf_idf': 'TF-IDF',
    'countVR': 'Bag of words',
}
# Define the available training model options and corresponding meaning
model_options = {
    'svm': 'Support Vector Machine',
    'logistic': "Logistics Regression"
}
##########################################################################
# Set Streamlit app configuration
st.set_page_config(page_title='Phân loại tin tức 🇻🇳')

# Display the title and description
st.title('Phân loại tin tức tiếng Việt 🇻🇳')
st.write('Nhập văn bản để phân loại và chọn loại đầu vào và mô hình dự đoán')

# Get the input type
input_type = st.selectbox('Chọn loại đầu vào', list(input_options.values()))
selected_input = get_key_by_value(input_options, input_type)

###########################################################################

# Filter the extraction files based on the selected input type
countVR_filtered_files = [file for file in countVR_files if selected_input.lower() in file.lower()]
tfidf_filtered_files = [file for file in tfidf_files if selected_input.lower() in file.lower()]

extraction_filtered_files = countVR_filtered_files + tfidf_filtered_files

# Let the user choose the desired feature extraction
extraction_type = st.selectbox('Chọn trích xuất đặc trưng', list(feature_extract_options.values()))

extraction_selected = get_key_by_value(feature_extract_options, extraction_type)

# load feature extraction model
if "countVR" in extraction_selected:
    extraction_selected = [model_filtered for model_filtered in extraction_filtered_files if "count" in model_filtered]
else:
    extraction_selected = [model_filtered for model_filtered in extraction_filtered_files if "idf" in model_filtered]

try:
    # Try loading countVR vectorizer
    exec_path = os.path.join(countVR_full_path, extraction_selected[0])
    vectorizer = joblib.load(exec_path)
except:
    # Load tf-idf as fallback
    exec_path = os.path.join(tfidf_full_path, extraction_selected[0])
    vectorizer = joblib.load(exec_path)
############################################################################

# Get user input
input_text = st.text_area('Nhập văn bản vào đây', height=100)

# Preprocess the input text
preprocessed_text = preprocess(input_text)

# apply vectorizer
input_vectorized = vectorizer.transform([preprocessed_text])
############################################################################

# Load model
# Filter the files based on the selected input type
model_filtered_files = [file for file in model_files if selected_input.lower() in file.lower()]

if "Bag" in extraction_type:
    selected_model = [model_filtered for model_filtered in model_filtered_files if "count" in model_filtered]
else:
    selected_model = [model_filtered for model_filtered in model_filtered_files if "idf" in model_filtered]

# Let the user choose the desired model
# model_selected_option = st.selectbox('Mô hình huấn luyện tương ứng', selected_model, disabled=True)
model_selected_option = selected_model[0]

for key_model in model_options.keys():
    if key_model in model_selected_option:
        model_displayed = model_options[key_model]

# st.subheader(f'Mô hình huấn luyện tương ứng: {model_selected_option.split(".")[0]}')
st.subheader(f'Mô hình huấn luyện tương ứng: {model_displayed}')

# Try loading model
exec_model_path = os.path.join(model_path, model_selected_option)
model = joblib.load(exec_model_path)

# Add a submit button
submit_button = st.button('Xác nhận')

# Check if the submit button is clicked
if submit_button:
    # Display the predicted category
    predict_label = model.predict_proba(input_vectorized)

    pred_value, pred_label = zip(*sorted(zip(predict_label[0], model.classes_), reverse=True))
    pred_label = list(pred_label)
    pred_value = list(pred_value)

    st.subheader(f'Dự đoán là: {pred_label[0]}, {pred_value[0]*100:.2f}%')

    fig = plt.figure(figsize=(8,4))
    ax = sns.barplot(x=pred_value, y=pred_label, alpha=0.8, errwidth=0)
    plt.xticks(rotation=45)
    ax.bar_label(ax.containers[0], fmt='%.3f')
    plt.title("Biểu đồ xác suất")

    # Add figure in streamlit app
    st.pyplot(fig)