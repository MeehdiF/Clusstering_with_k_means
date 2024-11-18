# STEPS FOR MACHINE LEARNING
## Step 0: Import the necessary libraries
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans 
from sklearn.datasets._samples_generator import make_blobs 
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder




## Step 1: Import Data
file = pd.read_excel("Online Retail.xlsx")
file.head()




## Step 2: Clean the Data
#['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country']
n_file = file.drop(['CustomerID', 'InvoiceNo', 'StockCode', 'InvoiceDate', 'CustomerID', "Description"], axis='columns')
n_file.head()
n_file.shape
#to see how many null values I have
print(sum(n_file.isnull().values.ravel()))
#Drop row that contain null value
n_file = n_file.dropna(axis='index')
n_file.dtypes
n_file.groupby("Country").mean()
#Conver "Country" data to number
label_encoder = LabelEncoder()
n_file["Country"] = label_encoder.fit_transform(n_file["Country"])




## Step 3: Normalize the data
X = n_file.values[:,1:]
X = np.nan_to_num(X)
Clus_dataSet = StandardScaler().fit_transform(X)
Clus_dataSet




## Step 4: Create a Model
clusterNum = 3
k_means = KMeans(init = "k-means++", n_clusters = clusterNum, n_init = 12)
k_means.fit(X)
labels = k_means.labels_




## Step 5: Cluster the data
# add to new file that I made it in step 2
n_file["Clus"] = labels
n_file.groupby('Clus').mean()
## add to orginal file
file["Clus"] = labels
file.groupby('Clus').first()
file.head(5)



## Step 6: visualization
#It is not working very well but still I used it
area = np.pi * ( X[:, 1])**2  
plt.scatter(X[:, 0], X[:, 1], s=area, c=labels.astype(np.float64), alpha=0.5)
plt.xlabel('UnitPrice', fontsize=18)
plt.ylabel('Quantity', fontsize=16)
#Althogh it's not working well, I'm did that 
plt.show()