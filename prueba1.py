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

#---Create a varibale for the URL---
#%%
col_list = pd.DataFrame(dat)
#%%



#--------DROP Column ----- PRINT SOLO 5
#%%
##hola = col_list.drop("Unnamed: 0", axis=1)

#%%

#-------filter by criteria in a column
#esta = (col_list.query ('state == "Idaho"' ))

#%%
#--------Create new column named:ratios (divide one column / with another----)
otra = (col_list.assign(ratios = lambda x:  x.violent / x.murder))
print (otra)


#%%
#todo = (hola
#     .query ("state == 'Idaho'")
 #     .filter(['violent','murder','state','year'])
#)

#%%
#chart =( alt.Chart(todo)
#    .encode(
#     x ='murder',
 #     y ='state',)
 #   .mark_line()
#    )
  

 
 
# %%
#print (chart)
# %%

#hola
#hola2
