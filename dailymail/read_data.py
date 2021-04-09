import glob
import json
import pandas as pd
import re
import uuid

from utils import url_to_headline


def combine_json_files(path):
    full_dict = {}
    for file in glob.glob(path):
        data = json.load(open(file))
        for _, values in data.items():
            full_dict[uuid.uuid4()] = values
    return full_dict


def make_df(data):
    df = pd.DataFrame.from_dict(data, orient='index')
    df['headline'] = df.url.apply(url_to_headline)
    df['url'] = df.url.apply(lambda x: 'dailymail.co.uk' + x)
    return df
