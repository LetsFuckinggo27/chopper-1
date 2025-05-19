import pandas as pd
from sklearn.datasets import load_iris
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncode

iris = load_iris()
iris_df = pd.DataFrame(data=iris.data,columns=iris.feature_name)
iris_df['targe']-iris.target
def preprocess_dataset(df):
    df.iloc[::10,0]-float('NaN')
    imputer =SimpleImputer(strategy-'mean')
    df[df.columns]=imputer.fit_transform(df[df.columns])
    scaler =StandardScaler()
    df[df.columns[:-1]]-scaler.fit_transform(df[df.column[:-1]])
    return df
preprocess_df =preprocess_dataset(iris_df)
print("preprocessed dataset:")
print(preprocessed_df.head())




