import warnings
warnings.simplefilter(action='ignore', category=FutureWarning) # ignore warnings

from fcmeans import FCM # Fuzzy C-Means Algorithm implementation in Python
from seaborn import scatterplot as scatter # building a scatterplot of data
from matplotlib import pyplot as plt # plotting the scatterplot
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np # data processing and normalization (e.g. arrays, np.linalg.norm)

# ask the user for input and handle miss input
feature = input("What feature are you comparing to price?\nbrand, price, cpu_man, cpu_freq, cpu_type, n_cores, cache_size, ram_size, ssd_size, display_tech, px_res, nits, width, g_card, bat_cap, bat_dur, ac_a_power, os, fingerprint\n")

lst = ["brand", "price", "cpu_man", "cpu_freq", "cpu_type", "n_cores", "cache_size", "ram_size", "ssd_size", "display_tech", "px_res", "nits", "width", "g_card", "bat_cap", "bat_dur", "ac_a_power", "os", "fingerprint"]

if feature not in lst:
    print("Invalid input! Make sure that your input is one of: brand, price, cpu_man, cpu_freq, cpu_type, n_cores, cache_size, ram_size, ssd_size, display_tech, px_res, nits, width, g_card, bat_cap, bat_dur, ac_a_power, os, fingerprint")
    exit(1)

# load the data
df = pd.read_csv('DATASET_FINAL.csv')
# create an empty array that will hold the values for 2 columns, price and another feature. This array liiks like: [[price1, price2, ..., price70],[other_feature1, other_feature2, ..., other_feature70]]
a = np.empty([2,70])
# normalize the price column
norm = np.max(df['price'])
normal_price = df['price']/norm
# fill the values of the empty array previously created
a[0] = normal_price
a[1] = df[feature]

# conditions to normalize unnormalized data
if feature == 'ssd_size':
    a[1] = df[feature]/10
elif feature == 'display_tech':
    a[1] = df[feature]/8
elif feature == 'price':
    a[1] = normal_price
else:
    pass

# transpose a to create an array with 70 rows and 2 columns where first column has the price data and the second coumn has data from another feature; array composition: [[normal_price1, other_feature1], [normal_price2, other_feature2], ..., [normal_price70, other_feature70]] 
X = np.transpose(a)

# fit the fuzzy-c-means
fcm = FCM(n_clusters=2)
fcm.fit(X)

# outputs
fcm_centers = fcm.centers
fcm_labels  = fcm.u.argmax(axis=1)

# plot result
f, axes = plt.subplots(1, 2)
f.tight_layout(pad = 3)
plt.setp(axes, xlim=(-0.15, 1.15), ylim=(-0.15, 1.15))
for ax in axes:
    ax.set(adjustable='box', aspect='equal')
scatter(X[:,0], X[:,1], ax=axes[0])
scatter(X[:,0], X[:,1], ax=axes[1], hue=fcm_labels)
scatter(fcm_centers[:,0], fcm_centers[:,1], ax=axes[1], marker='s', color='r', s=50)
f.suptitle(feature, size=16)
for ax in axes.flat:
    ax.set(xlabel="price", ylabel=feature)

# save the graph as a jpg image in images2 folder, indicating we used 2 clusters
save_path = 'images2/'+feature+'_price.jpg'
plt.savefig(save_path, format='jpg')

plt.show()