import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools



loc = '28.644800,77.216721,500km'
df_coord = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(
    'geocode:"{}"'.format(loc)).get_items(), 6000))[['date', 'content']]


# print(df_coord)
print("DONE!")
df_coord.to_csv('twitter_data.csv')