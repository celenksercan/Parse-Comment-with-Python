from textblob import TextBlob as tb
import pandas as pd
import csv

df = pd.read_csv("yorumlar.csv")

karsilastirmaliCsv = open("karsilastirmali.csv", "w", newline='')
writer = csv.writer(karsilastirmaliCsv, delimiter=",")
index = 0

for yorum, puan in df.to_numpy():
    blobTurkish = tb(yorum)
    blobEnglish = blobTurkish.translate(to="en")
    hesaplananPuan = round(blobEnglish.sentiment.polarity, 1)
    print(yorum,puan,hesaplananPuan)
    writer.writerow([puan, hesaplananPuan])
    index = index+1

karsilastirmaliCsv.close()