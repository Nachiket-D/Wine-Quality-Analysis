import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

data = pd.read_csv("1613779-Red_wine_.csv")
data.head()
data.info()

data = data.iloc[:,1:]
print(data.head())
data.describe()
data.corr()['quality']
plt.figure(figsize=(10,10))
sns.heatmap(data.corr(),annot=True,linewidth=0.5,center=0,cmap='coolwarm')
plt.show()

plt.hist(data.quality,bins=6,alpha=0.5,histtype='bar',ec='black')
plt.title('Distribution of the Quality')
plt.xlabel('Quality')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(data['quality'],data['pH'],palette="GnBu_d")
plt.show()

sns.boxplot(x='quality',y='pH',data=data,palette='GnBu_d')
plt.title("Boxplot of Quality and pH")
plt.show()

ax = sns.boxplot(x='quality',y='alcohol',data=data,palette='GnBu_d')
plt.title("Boxplot of Quality and Alcohol")
plt.show()

sns.boxplot(x="quality",y="residual.sugar",data=data,palette="GnBu_d")
plt.title("Boxplot of Quality and residual sugar")
plt.show()

sns.boxplot(x="quality",y="density",data=data,palette="GnBu_d")
plt.title("Boxplot of Quality and Density")
plt.show()

sns.boxplot(x="quality",y="sulphates",data=data,palette="GnBu_d")
plt.title("Boxplot of Quality and Sulphates")
plt.show()

sns.boxplot(x="quality",y="chlorides",data=data,palette="GnBu_d")
plt.title("Boxplot of Quality and Chlorides")
plt.show()

sns.boxplot(x="quality",y="citric.acid",data=data,palette="coolwarm")
plt.title("Boxplot of Quality and Citric Acid")
plt.show()

sns.boxplot(x="quality",y="volatile.acidity",data=data,palette="coolwarm")
plt.title("Boxplot of Quality and Volatile Acidity")
plt.show()

sns.boxplot(x="quality",y="fixed.acidity",data=data,palette="coolwarm")
plt.title("Boxplot of Quality and Fixed Acidity")
plt.show()

sns.boxplot(x="quality",y="free.sulfur.dioxide",data=data,palette="coolwarm")
plt.title("Boxplot of Quality and Free Sulfur Dioxide")
plt.show()

sns.boxplot(x="quality",y="total.sulfur.dioxide",data=data,palette="coolwarm")
plt.title("Boxplot of Quality and Total Sulfur Dioxide")
plt.show()