import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd

#-1 -0.6 -0.2 0.2 0.4 1
def aralikDonustur(x):
    if x >= -1 and x < -0.6:
        return 1
    elif x >= -0.6 and x < -0.2:
        return 2
    elif x >= -0.2 and x < 0.2:
        return 3
    elif x >= 0.2 and x < 0.6:
        return 4
    elif x >= 0.6 and x <= 1:
        return 5

df = pd.read_csv("karsilastirmali.csv")
df["analizPuan"] = df["analizPuan"].apply(aralikDonustur)


puan5 = df[df["orjinalPuan"] == 5]
print(puan5.describe())

puan4 = df[df["orjinalPuan"] == 4]
print(puan4.describe())

puan3 = df[df["orjinalPuan"] == 3]
print(puan3.describe())

puan2 = df[df["orjinalPuan"] == 2]
print(puan2.describe())

puan1 = df[df["orjinalPuan"] == 1]
print(puan1.describe())

sns.scatterplot(data=puan5, x=range(0, 707), y="analizPuan")
plt.show()
sns.scatterplot(data=puan4, x=range(0, 203), y="analizPuan")
plt.show()
sns.scatterplot(data=puan3, x=range(0, 48), y="analizPuan")
plt.show()
sns.scatterplot(data=puan2, x=range(0, 15), y="analizPuan")
plt.show()
sns.scatterplot(data=puan1, x=range(0, 17), y="analizPuan")
plt.show()
