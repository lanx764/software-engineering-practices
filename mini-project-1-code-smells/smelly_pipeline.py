# Original smelly code — do not modify

import requests
import pandas as pd
from datetime import datetime

def d(u, k, t, r, o, l, c):
    response = requests.get(u, headers={"Authorization": k}, timeout=t)
    data = response.json()
    records = []
    for item in data["results"]:
        if item["v"] is not None:
            item["v"] = float(item["v"])
            item["ts"] = datetime.now().strftime("%Y-%m-%d")
            records.append(item)
    df = pd.DataFrame(records)
    df = df.dropna()
    df["v"] = df["v"] * 1.075
    df2 = pd.DataFrame(records)
    df2 = df2.dropna()
    df2["v"] = df2["v"] * 1.075
    bad = []
    for index, row in df.iterrows():
        if row["v"] > 500:
            bad.append(row)
    # for index, row in df.iterrows():
    #     if row["v"] < 0:
    #         bad.append(row)
    if len(bad) > 0:
        print("alert")
    with open(o, "w") as f:
        f.write(df.to_csv(index=False))
    print("done")

def d(u, k, t, r, o, l, c):
    response = requests.get(u, headers={"Authorization": k}, timeout=t)
    data = response.json()
    records = []
    for item in data["results"]:
        if item["v"] is not None:
            item["v"] = float(item["v"])
            item["ts"] = datetime.now().strftime("%Y-%m-%d")
            records.append(item)
    df = pd.DataFrame(records)
    df = df.dropna()
    df["v"] = df["v"] * 1.075
    with open(o, "w") as f:
        f.write(df.to_csv(index=False))
    print("done")