# script to view the correlation matric of our data shown as a heatmap plot
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # plotting
import seaborn as sns # contains the heatmap function that returns a subplot

# read the data from csv file and save it in a dataframe
df = pd.read_csv('DATASET_FINAL.csv')
# remove the column named no as it is just for indexing
df.pop('no')
# print 5 first entries for the dataframe
print(df.head())
# define a correlation matrix for the data using the Pearson's method
corr = df.corr(method='pearson')
# print the 5 first entries of the correlation matrix
corr.head()
# create a heatmap subplot
ax = sns.heatmap(corr, linewidths=1)
# show the subplot
plt.show()