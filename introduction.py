#%%
import pandas as pd
#%%
import altair as alt   
#%%

url = "https://raw.githubusercontent.com/byuidatascience/data4python4ds/master/data-raw/mpg/mpg.csv"
#%%
mpg = pd.read_csv(url)
#%%



#%%
chart = (alt.Chart(mpg)
  .encode(
    x='displ', 
    y='hwy')
  .mark_circle()
)
chart

#%%
print (chart)
#%%

print(mpg
  .head(5)
  .filter(["manufacturer", "model","year", "hwy","displ"])
  .to_markdown(index=False))
# %%

