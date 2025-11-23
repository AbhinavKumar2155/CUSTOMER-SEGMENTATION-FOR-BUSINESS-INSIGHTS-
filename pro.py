import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
df = pd.read_excel("STP.xlsx")
print(df.describe())
print(df.info())
print(df.isnull().sum())
df.drop_duplicates(subset=['Customer ID'])
df['Purchase History'] = pd.to_datetime(df['Purchase History'], errors='coerce')
df['Year'] = df['Purchase History'].dt.year
avg_coverage_by_year = df.groupby('Year')['Coverage Amount'].mean().dropna()
plt.figure(figsize=(10, 6))
avg_coverage_by_year.plot(kind='bar', color='skyblue')
plt.title('Average Coverage Amount by Year')
plt.xlabel('Year')
plt.ylabel('Average Coverage Amount')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

sns.pairplot(df,hue='Insurance Products Owned')
plt.show()

y=df.groupby('Geographic Information')['Coverage Amount'].sum()
plt.bar(y.index,y.values)
plt.xticks(rotation=35)
plt.yscale('log')
plt.title("Region Wise Total Coverage Amount")
plt.xlabel("State")
plt.ylabel("Coverage Amount")
plt.show()

z=df.groupby('Occupation')['Premium Amount'].mean()
plt.plot(z.index,z.values,marker='o',color='red')
plt.title("Occupation wise Premium Amount")
plt.xlabel("Occupation")
plt.ylabel("Avg Premium Amount")
plt.show()

corr=df.corr(numeric_only=True)
sns.heatmap(corr,annot=True,cmap='coolwarm',fmt='.2f')
plt.show()

features = [
    'Age', 'Income Level', 'Coverage Amount', 'Premium Amount',
    'Gender', 'Marital Status', 'Education Level', 'Occupation'
]

data = df[features].copy()
categorical_cols = ['Gender', 'Marital Status', 'Education Level', 'Occupation']
for col in categorical_cols:
    data[col] = LabelEncoder().fit_transform(data[col])
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)
kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_data)

cluster_summary = df.groupby('Cluster')[['Age', 'Income Level', 'Coverage Amount', 'Premium Amount']].mean()
print(cluster_summary)

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
components = pca.fit_transform(scaled_data)
df['PCA1'] = components[:, 0]
df['PCA2'] = components[:, 1]

# Scatter plot
sns.set(style="whitegrid")
sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='Cluster', palette='Set2')
plt.title("Customer Segments (PCA View)")
plt.show()
pca = PCA(n_components=2)
components = pca.fit_transform(scaled_data)

df['PCA1'] = components[:, 0]
df['PCA2'] = components[:, 1]

# Plot clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='Cluster', palette='Set2', s=60)
plt.title("Customer Segments Based on Clustering (PCA Projection)")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.grid(True)
plt.show()


x = df['Preferred Communication Channel'].value_counts()

#import matplotlib.pyplot as plt

plt.pie(x.values,labels=x.index,autopct='%1.1f%%',explode=[0.03]*len(x))
plt.title("Customers' Preferred Mode of Communication")
plt.axis('equal')
plt.tight_layout()
plt.show()

