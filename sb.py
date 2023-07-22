import seaborn as sns
from matplotlib import pyplot as plt

fm = sns.load_dataset("fmri.csv")
print(fm.head())     # It gives first five records
print(fm.shape)      # (1064, 5)
sns.lineplot(x="timepoint", y="signal", data = fmri)
plt.show()  

sns.lineplot(x="timepoint", y="signal", data = fmri, hue = "event")
