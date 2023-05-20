import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()

trends.build_payload(kw_list=["ChatGPT"])
data = trends.interest_by_region()
data = data.sort_values(by="ChatGPT", ascending=False)
data = data.head(10)
print(data)

data.reset_index().plot(x="geoName", 
                        y="ChatGPT", 
                        figsize=(15,12), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()