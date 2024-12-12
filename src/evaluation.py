from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor,AdaBoostRegressor
from sklearn import metrics
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split

x = pd.read_csv(r"C:\Users\Bipin\Downloads\Optimizing Testing Time for Mercedes-Benz\data\clean_data\x.csv")
y = pd.read_csv(r"C:\Users\Bipin\Downloads\Optimizing Testing Time for Mercedes-Benz\data\clean_data\y.csv")

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=50)

x_train.shape, y_train.shape

x_test.shape, y_test.shape

# Define the path to the model file
model_path = r'C:\Users\Bipin\Downloads\Optimizing Testing Time for Mercedes-Benz\model.pkl'

# Load the Gradient Boosting model


gb = pickle.load(open(model_path, 'rb'))
# Example: Use the loaded model for predictions
# Assuming you have test data in a DataFrame `x_test`
# x_test = ... (Load or preprocess your test data)
y_pred = gb.predict(x_test)

prediction=gb.predict(x_test)

gb.score(x_test,y_test)

gb.score(x_train,y_train)

# residual=y_test-prediction

print('MAE:',metrics.mean_absolute_error(y_test,prediction))
print('MSE:',metrics.mean_squared_error(y_test,prediction))
print('RMSE:',np.sqrt(metrics.mean_squared_error(y_test,prediction)))

