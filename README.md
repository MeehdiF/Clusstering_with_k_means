# Online Retail Product Clustering

Description

This project involves clustering products from an online retail dataset based on key features such as price, quantity, and country. By utilizing the K-Means clustering algorithm, the aim is to group similar products together to better understand purchasing patterns and product categories.

Dataset

 • Name: Online Retail Dataset
 • Source: UCI Machine Learning Repository (https://archive.ics.uci.edu/ml/index.php)
 • Features Used:
 • Quantity: Number of products sold.
 • UnitPrice: Price of each product.
 • Country: Country of transaction (encoded numerically).

Steps Involved

 1. Data Cleaning:
 • Removed irrelevant columns such as InvoiceNo and Description.
 • Handled missing values by removing rows with null values.
 • Encoded categorical features (e.g., Country) into numerical values using LabelEncoder.
 2. Data Normalization:
 • Standardized the dataset using StandardScaler to improve the performance of the clustering algorithm.
 3. Clustering Algorithm:
 • Implemented K-Means with 3 clusters (n_clusters=3).
 • Assigned cluster labels to each product.
 4. Visualization:
 • Attempted 2D visualization of clustered data using scatter plots.
 • Explored insights into how products are grouped based on their features.

Key Results

 • Products were grouped into 3 clusters:
 • Cluster 1: Low-priced products with high sales volume.
 • Cluster 2: Products sold in specific countries with moderate pricing.
 • Cluster 3: High-priced products with low sales volume.
 • Further analysis revealed patterns in pricing and sales for each group.

Limitations

 • Visualization of high-dimensional data was limited due to reducing features to 2D.
 • Number of clusters was selected manually; future iterations could use methods like Elbow Method or Silhouette Score for optimization.

Requirements

 • Python 3.x
 • Libraries:

numpy  
pandas  
matplotlib  
scikit-learn  
openpyxl  



How to Run

 1. Clone the repository:

git clone https://github.com/Meehdif/Clusstering_with_k_means.git
cd online-retail-clustering


 2. Install the dependencies:

pip install -r requirements.txt


 3. Run the script:

python clustering.py



Future Work

 • Implement dimensionality reduction techniques like PCA or t-SNE for better visualization.
 • Explore advanced clustering methods (e.g., DBSCAN or Hierarchical Clustering) for comparison.
 • Use automated techniques for determining the optimal number of clusters.

Author

 • Mehdi
