import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataFrame = pd.read_csv("Data.csv")

dataset = dataFrame.iloc[:, :].values


from sklearn.preprocessing import LabelEncoder

bonusEncoder = LabelEncoder()
dataset[:, 3] = bonusEncoder.fit_transform(dataset[:, 3])
