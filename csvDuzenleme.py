import pandas as pd

data = pd.read_csv("yorumlar.csv", names=["Yorum", "Puan"], delimiter=" ")
data = data.drop_duplicates()
data = data.sort_values(by="Puan", ascending=False)
data.to_csv("yorumlar.csv", sep=" ")