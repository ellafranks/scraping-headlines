from dailymail.gather_headlines import generate_urls
from dailymail.read_data import make_df, combine_json_files


def execute(path):
    # generate_urls(path)
    data = combine_json_files(path + '*json')
    df = make_df(data)
    print(df.head())
    return df


if __name__ == '__main__':
    # generate_urls('/Users/ella.franks/PycharmProjects/news-headlinesProject/data/')
    execute('/Users/ella.franks/PycharmProjects/news-headlinesProject/data/')
