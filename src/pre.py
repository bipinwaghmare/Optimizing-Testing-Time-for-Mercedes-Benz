import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import LabelEncoder

# df=pd.read_csv('/content/drive/MyDrive/All Projects/ML/Mercedes Benz Dataset Project/train.csv')
df = pd.read_csv(r'C:\Users\Bipin\Downloads\Optimizing Testing Time for Mercedes-Benz\data\train.csv.zip')
df



df_obj = df.select_dtypes(include='object')

le=LabelEncoder()
for i in df_obj.columns:
  df_obj[i]=le.fit_transform(df_obj[i])

df = df.drop(columns=df_obj.columns)

df.drop(columns=['ID'],axis=1,inplace=True)

data = pd.concat([df_obj,df],axis=1)

data.isnull().sum()

data.duplicated()

y = df['y']

x = data.drop('y',axis=1)
y=df['y']

from sklearn.preprocessing import StandardScaler

xcols=x.columns
sc=StandardScaler()
x_transformed=sc.fit_transform(x)
x=pd.DataFrame(x_transformed,columns=xcols)
x.head()

import os

# Define paths to the existing folders
folder = r'C:\Users\Bipin\Downloads\Optimizing Testing Time for Mercedes-Benz\data\clean_data'

# Save x and y as CSV files
x.to_csv(os.path.join(folder, 'x.csv'), index=False)
y.to_csv(os.path.join(folder, 'y.csv'), index=False)

print("Data saved successfully to the specified folders!")

joblib.dump(sc, r'C:\Users\Bipin\Downloads\Optimizing Testing Time for Mercedes-Benz\scaler.pkl')

     

