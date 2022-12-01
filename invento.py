#%%
import numpy as np
#%%
import pandas as pd
#%%
import altair as alt
# data import

#%%
dat = pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/AER/Guns.csv")
 
#%%
esta = pd.DataFrame(dat)

#daniel = (esta.filter (["violent","murder","murder","male"],))

#print (daniel)
#%%
#--------Create new column named:ratios (divide one column / with another----)
otra = (esta.assign(ratios = lambda x:  x.violent / x.murder))

#%% print (otra)

daniel = (otra.filter (["violent","murder","murder","male","ratios"],))

