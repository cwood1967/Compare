#%%
import numpy as np
import pandas as pd

from  hvplot.sample_data import us_crime
import hvplot.pandas
# %%

columns = ['Burglary rate', 'Larceny-theft rate', 'Robbery rate', 'Violent Crime rate']
us_crime.plot.violin(y=columns, group_label='Type',
                     value_label='Rate per 100k', invert=True)

# %%


# %%
crime = us_crime.read()
crime

# %%


# %%
cols = crime.columns
cols

# %%
crime.hvplot.scatter(x='Violent Crime rate', y='Burglary rate')

# %%
(24*7 - 130)/7

# %%
exit()

# %%
