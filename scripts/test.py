from dailymail import gather_headlines
from dailymail.gather_headlines import generate_urls
from dailymail.read_data import combine_json, make_df


if __name__ == '__main__':
    # generate_urls('/Users/ella.franks/PycharmProjects/news-headlinesProject/data/')
    make_df(
        combine_json('/Users/ella.franks/PycharmProjects/news-headlinesProject/data/*json'))