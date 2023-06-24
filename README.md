# Vietnamese News Classification Model

This project focuses on building a Vietnamese news classification model. The goal is to classify news articles into different categories based on their content. 

## Overview

The project consists of several steps: data crawling, preprocessing, feature extraction, and model training. 

1. Data Crawling: News data is crawled from a Vietnamese news website. The crawled data includes Category, Sub-category, Title, Description, and Content of each news article.

2. Preprocessing: The crawled data is preprocessed to clean and prepare it for further analysis. This includes removing irrelevant information, handling missing values, and applying tokenization to the Vietnamese text using the underthesea library.

3. Feature Extraction: Various feature extraction techniques are employed to convert the text data into numerical representations. The following techniques are used:
   - Bag of Words: This approach represents text as a collection of word frequencies.
   - TF-IDF (Term Frequency-Inverse Document Frequency): This technique assigns weights to words based on their importance in a document relative to the entire corpus.
   - PhoBERT: This is a state-of-the-art language model specifically designed for the Vietnamese language.

4. Model Training and Evaluation: Several classification models are trained and evaluated using the extracted features. The following models are used:
   - Naive Bayes
   - Support Vector Machines (SVM)
   - K-Nearest Neighbors (KNN)
   - Logistic Regression
   - Decision Tree
   - Random Forest

## Experiments

Experiments are conducted to evaluate the performance of each combination of feature extraction technique and classification model. Evaluation metrics such as accuracy, precision, recall, and F1-score are calculated to assess the classification results.

Based on the experiments, it was found that Logistic Regression with the Bag of Words approach and SVM with TF-IDF achieved the best classification results for the Vietnamese news data.

## Run Code


### Prerequisites

- Python [version]
- Required libraries and dependencies

### Installation

1. Clone the repository:
   ```
   git clone [repository URL]
   ```
   
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Usage

1. Prepare the dataset: [Provide instructions on how to prepare the dataset for training and evaluation]

2. Feature extraction: [Describe how to perform feature extraction using the chosen technique]

3. Model training: [Provide steps to train the chosen models]

4. Evaluation: [Explain how to evaluate the trained models]

### Examples

- [Provide example usage or code snippets]

## Contributing

Contributions to the project are welcome. If you would like to contribute, please follow the guidelines outlined in [CONTRIBUTING.md].

## License

[License information]

## Contact

For any inquiries or questions, please contact [EMAIL ADDRESS].


