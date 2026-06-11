import requests
import pandas as pd
from datetime import datetime

MAX_RECORDS_THRESHOLD = 500
MIN_RECORDS_THRESHOLD = 0
CRITICAL_ALERT = "alert"
DATE_FORMAT = "%Y-%m-%d"
VAT_RATE = 1.075
LOADING_FINISHED = "done"

def ingest(url, api_key, timeout):
    response = requests.get(url, headers={"Authorization": api_key}, timeout=timeout)
    data = response.json()
    return data

def transform(data):
    records = []
    for item in data["results"]:
        if item["v"] is not None:
            records.append({
                "value": float(item["v"]),
                "timestamp": datetime.now().strftime(DATE_FORMAT) #"%Y-%m-%d" was chosen because we only what the day of the ,month and year of that particular event
            })
    df = pd.DataFrame(records)
    df = df.dropna()
    df["value"] = df["value"] * VAT_RATE
    bad = []
    for index, row in df.iterrows():
        if row["value"] >MAX_RECORDS_THRESHOLD:
            bad.append(row)
    for index, row in df.iterrows():
        if row["value"] < MIN_RECORDS_THRESHOLD:
            bad.append(row)
    if len(bad) > MIN_RECORDS_THRESHOLD:
        print(CRITICAL_ALERT)
    return df

def load(df,output_path):
    with open(output_path, "w") as f:
        f.write(df.to_csv(index=False))
    print(LOADING_FINISHED)