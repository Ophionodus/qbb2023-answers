#!/usr/bin/env python

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-03-07/numbats.csv'
numbats = pd.read_csv(url)

#----------------------Seasons-------------------------
# summer = numbats.loc[numbats['month'].isin(['Dec', 'Jan', 'Feb']), :]
# autumn = numbats.loc[numbats['month'].isin(['Mar', 'Apr', 'May']), :]
# winter = numbats.loc[numbats['month'].isin(['Jun', 'Jul', 'Aug']), :]
# spring = numbats.loc[numbats['month'].isin(['Sep', 'Oct', 'Nov']), :]

# data = {'summer':len(summer), 'autumn':len(autumn), 'winter':len(winter), 'spring':len(spring)}


# names = list(data.keys())
# values = list(data.values())


# plt.bar(range(len(data)), values, tick_label=names)
# plt.xlabel("Season")
# plt.ylabel("Number of Numbat Sightings")
# plt.title("Numbat Sightings are More Common in Warmer Seasons")
# plt.show()

#-------------------Rain---------------------------------
# plt.hist(numbats.loc[:, 'prcp'], bins=25)
# plt.xlabel("Rain in Millimeters on Day of Sighting")
# plt.ylabel("Number of Numbat Sightings")
# plt.title("Numbat Sightings are Less Common When it is Raining")
# plt.show()

#------------------Time of Day------------------
# values, bins, bars = plt.hist(numbats.loc[:, 'hour'], bins=24)
# plt.xlabel("Time of Day in Hours-Post-Midnight")
# plt.ylabel("Number of Numbat Sightings")
# plt.title("Numbats are Active in the Early Afternoon")
# plt.bar_label(bars, fontsize=10, color='navy')
# plt.show()