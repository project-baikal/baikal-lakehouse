import requests
import json
import boto3
from dagster import asset, Output, MetadataValue
import os

s3 = boto3.client("s3")
BUCKET_NAME = 'project-baikal'
PREFIX = "poc_data/bronze/country/"

COUNTRIES = ["canada", "mexico", "china", "japan", "costa"]

@asset
def country_data_to_s3():
    results = []
    for country in COUNTRIES:
        url = f"https://restcountries.com/v3.1/name/{country}"
        resp = requests.get(url)
        resp.raise_for_status()

        data = resp.json()[0]
        key = f"{PREFIX}{country}.json"
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=key,
            Body=json.dumps(data),
            ContentType="application/json"
        )
        results.append({"country": country, "s3_key": key})

    return results
