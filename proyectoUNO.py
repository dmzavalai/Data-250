#%%
import pandas as pd
#%%
import altair as alt   
#%%
url = "https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv"
#%%
names_years = pd.read_csv(url)
#%%
question1 =(names_years
  .query ("name =='Daniel'")
  .filter(['year','Total'])
 )

#%%
chart = (alt.Chart(question1)
  .encode(
    x='year', 
    y='Total')
  .mark_bar()
)
chart

#%%
print (chart)
# %%
#---------TABLE 1-------
#%%
print(question1
  .head(5)
  .filter( ["year","name","Total"])
  .to_markdown(index=False))

#%%


#----------QUESTION 2------
# %%
question2 =(names_years
            .query ("name == 'Brittany'")
            .filter (['name', 'year','Total'])
)
#%%
chart2 = (alt.Chart(question2)
        .encode(
          x ='year',
          y = 'Total',
          color = 'name')
        .mark_line()
        )


chart2
# %%
#---------TABLE 2-------

print(question2
  
  .filter( ["year","name","Total"])
  .to_markdown(index=False))

#%%

#--------QUESTION 3--------

#%%
question3 = (names_years 
            .query  ("name in ('Mary','Martha','Peter','Paul')")
            .query ("year > 1920 and year < 2000")
            .filter (['name','year', 'Total'])
)

#%%
chart3 = (alt.Chart(question3)
        .encode (
           x = "year",
           y = "Total",
           color = 'name')
        .mark_line ()
        )
chart3

#%%


#--------TABLE 3----------
print(question3
  
  .filter( ["year","name","Total"])
  .to_markdown(index=False))

#%%
#--------Question 4-------

#%%
question4 =(names_years
  .query ("name =='Luke'")
  .filter(['year','Total'])
 )

 #%%
chart4 = (alt.Chart(question4)
  .encode(
    x='year', 
    y='Total')
  .mark_line()
)
chart4

#%%
print (chart4)

#------------TABLE 4------

print(question4
  
  .filter( ["year","name","Total"])
  .to_markdown(index=False))
