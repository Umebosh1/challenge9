import csv

list1=["トップガン","リスキービジネス","マイノリティリポート"]
list2=["タイタニック","ザレヴェナント","インセプション"]
list3=["トレーニングデイ","マンオンファイア","フライト"]

with open("challenge4.csv","w",newline='',encoding="shift_jis") as f:
    w=csv.writer(f,delimiter=",")
    w.writerow(list1)
    w.writerow(list2)
    w.writerow(list3)
