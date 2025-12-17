## DS10 – Machine Learning Models on Iris Dataset

### Dataset
- The Iris dataset is a standard multi-class classification dataset containing 150 samples, four numerical features, and three balanced target classes.
- Its simplicity and balance make it suitable for evaluating both distance-based and tree-based machine learning algorithms.
  
---

## Question 1: K-Nearest Neighbours (Easy)

### Model Description
- K-Nearest Neighbours (KNN) is an instance-based learning algorithm that classifies data points based on the majority class of their nearest neighbors.

### Reasoning
- KNN was chosen because it is a simple, non-parametric, distance-based algorithm that performs well on small and well-separated datasets like Iris.
- Since KNN relies on distance computation, feature scaling is necessary to prevent bias toward features with larger numeric ranges.
- The value of K was varied from 1 to 25 to study the bias–variance trade-off.
- Lower values of K may lead to overfitting, while higher values can oversmooth decision boundaries.
- Validation accuracy was used to select the optimal K that generalizes well.
- Accuracy, F1-score, and ROC-AUC were reported as the dataset is balanced and multi-class.

---

## Question 2: Decision Tree using Entropy (Moderate)

### Model Description
- Decision Trees classify data by recursively splitting features based on an impurity measure, forming a tree-like structure.

### Reasoning
- A Decision Tree was selected due to its interpretability and ability to capture non-linear relationships between features.
- The entropy criterion was used to follow the ID3 algorithm’s information gain principle.
- The max_depth hyperparameter was tuned to control model complexity and avoid overfitting.
- Shallow trees may underfit the data, while deeper trees tend to memorize training samples.
- Validation accuracy was used to determine the optimal depth value.
- Accuracy and F1-score were used as evaluation metrics because the dataset has balanced classes.

---

## Question 3: ID3-Style Pruning using Validation Set (Hard)

### Model Description
- ID3 is a greedy decision tree algorithm that uses entropy to select the best feature at each split.

## Reasoning
- A full decision tree was initially trained to illustrate overfitting through high training accuracy and lower validation accuracy.
- ID3-style pruning was simulated by restricting the maximum depth of the tree using a validation set.
- Multiple depth values were evaluated to analyze the training–validation performance gap.
- The depth that achieved the highest validation accuracy with reduced overfitting was selected.
- Pruning improves generalization by reducing variance and simplifying the model.
- The final pruned tree was visualized to improve interpretability and explain decision-making.

---

## To install all the required dependencies:
### Run the following command:
- pip install -r requirements.txt


### Dataset Used : 
- The experiments use the Iris dataset obtained from Kaggle:
- Dataset Link: https://www.kaggle.com/datasets/uciml/iris

### Instructions:
- Download the dataset from the link above.
- Extract the file.
- Place Iris.csv in the project root directory before running the code.