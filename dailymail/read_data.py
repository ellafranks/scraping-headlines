import glob
import json
import pandas as pd
import re


def combine_json(path):
    for file in glob.glob(path):
        data = json.load(open(file))
    return data


def make_df(data):
    df = pd.DataFrame.from_dict(data, orient='index')
    df.url = df.url.apply(lambda x: re.findall('([^\/]+)(?=.html)', x)[0].replace('-', ' '))
    print(df.head())
    return df

