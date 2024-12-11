# Mercedes-Benz Greener Manufacturing

## Overview
This project is part of the Kaggle competition **Mercedes-Benz Greener Manufacturing**, hosted by Daimler. The goal is to reduce the time cars spend on the test bench by optimizing a dataset representing various feature permutations of Mercedes-Benz cars. The ultimate aim is to develop machine learning models that predict testing time while maintaining Daimler's high standards of efficiency and safety.

**Competition Link:** [Mercedes-Benz Greener Manufacturing](https://www.kaggle.com/competitions/mercedes-benz-greener-manufacturing/data)

---

## Problem Statement
The challenge is to tackle the curse of dimensionality and optimize the car testing process. By predicting the time it takes for cars to pass testing, we aim to achieve faster testing times and reduce carbon dioxide emissions without compromising standards.

---

## Dataset
The dataset contains various car features and the target variable `y`, representing the time it takes to pass testing. It includes:
- Categorical features (e.g., `X0`, `X1`, etc.)
- Numerical features (e.g., `X380`, `X382`, etc.)

### Data Preprocessing Steps:
1. Encoding categorical variables using `LabelEncoder`.
2. Standardizing numerical features with `StandardScaler`.
3. Splitting the data into training and testing sets (80/20 split).

---

## Models and Results
The following models were trained and evaluated:

### 1. **Ridge Regression**
- **Test Score (R²):** 0.524
- **Train Score (R²):** 0.597
- **MAE:** 5.595
- **MSE:** 71.053
- **RMSE:** 8.429

### 2. **Random Forest Regressor**
- **Test Score (R²):** 0.486
- **Train Score (R²):** 0.908
- **MAE:** 5.910
- **MSE:** 77.426
- **RMSE:** 8.799

### 3. **Gradient Boosting Regressor**
- **Test Score (R²):** 0.573
- **Train Score (R²):** 0.628
- **MAE:** 5.235
- **MSE:** 63.872
- **RMSE:** 7.992

### 4. **Support Vector Regressor (SVR)**
- **Test Score (R²):** 0.449 (after scaling)
- **Train Score (R²):** 0.459 (after scaling)
- **MAE:** 5.779
- **MSE:** 82.322
- **RMSE:** 9.073

---

## Insights
- **Gradient Boosting Regressor** achieved the best performance with the highest test R² (0.573) and lowest RMSE (7.992).
- Feature scaling had minimal impact on most models except SVR, which improved significantly after scaling.
- Random Forest showed a strong overfitting tendency with a significant gap between train and test R².

---

## Technologies Used
- **Python Libraries:** pandas, numpy, sklearn, seaborn, matplotlib
- **Models:** Ridge Regression, Random Forest, Gradient Boosting, SVR

---

## Steps to Run the Code
1. Clone the repository or download the dataset from the Kaggle competition link.
2. Install the required Python libraries using:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn
   ```
3. Run the notebook or script in your preferred Python environment.
4. Evaluate the models and compare the results.

---

## Future Work
- Experiment with hyperparameter tuning for Gradient Boosting and SVR to improve performance further.
- Explore feature engineering techniques to reduce dimensionality and enhance prediction accuracy.
- Try advanced algorithms like XGBoost and LightGBM for potentially better results.

---

## Acknowledgments
- Dataset provided by Daimler for the Kaggle competition.
- Hosted on [Kaggle](https://www.kaggle.com/competitions/mercedes-benz-greener-manufacturing/data).
