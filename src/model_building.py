from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import metrics
import numpy as np
import pickle
import joblib


x = pd.read_csv(r"C:\Users\Bipin\Downloads\Optimizing Testing Time for Mercedes-Benz\data\clean_data\x.csv")
y = pd.read_csv(r"C:\Users\Bipin\Downloads\Optimizing Testing Time for Mercedes-Benz\data\clean_data\y.csv")

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=50)

x_train.shape, y_train.shape

x_test.shape, y_test.shape

from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor,AdaBoostRegressor

gb = GradientBoostingRegressor()
gb.fit(x_train, y_train)

prediction=gb.predict(x_test)

gb.score(x_test,y_test)

gb.score(x_train,y_train)

# residual=y_test-prediction

print('MAE:',metrics.mean_absolute_error(y_test,prediction))
print('MSE:',metrics.mean_squared_error(y_test,prediction))
print('RMSE:',np.sqrt(metrics.mean_squared_error(y_test,prediction)))


# Save the model and the scaler
model_path = r'C:\Users\Bipin\Downloads\Optimizing Testing Time for Mercedes-Benz\model.pkl'

# Save the model using pickle
with open(model_path, 'wb') as file:
    pickle.dump(gb, file)