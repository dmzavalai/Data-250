#%%
import pandas as pd
#%%
import altair as alt
#%%
import numpy as ny
#%%

url = "https://raw.githubusercontent.com/byuidatascience/data4missing/master/data-raw/flights_missing/flights_missing.json"
#%%

data = pd.read_json (url)

#%%
print (data.head(2))

#%%-------------------Question 1------------------------------
daniel = (data
    .groupby (['airport_code'])
    .agg(total_flights = ('num_of_flights_total',sum),
    total_delays = ('num_of_delays_total',sum),
    total_delay_min = ('minutes_delayed_total',sum)
)
    .assign(delay_percentage = lambda x: round(((x.total_delays/x.total_flights)*100),2)
                  , avg_delay_time_hrs = lambda x: round(((x.total_delay_min /
x.total_delays)/60),3)
                  )
            .reset_index()
 
)
print(daniel.head(5))





#which airport has the worst
#total # fligjts
#toal # of delayed flights 
#proportion of delayed flights
#average delay time in hours


# %%


#------------------Question 2------------------------------------

# What is the best month to fly? - 

month = (data
    .groupby (["month"])
    .agg(total_flights = ('num_of_flights_total',sum),
    total_delays = ('num_of_delays_total',sum))
    .drop ("n/a")
    .assign(delay_percentage = lambda x: round(((x.total_delays/x.total_flights)*100),2))
)
print (month)

#--------------------- CHART 2----------------------------------
#%%
chart2 = (alt.Chart (month)
.encode(
    x='month', 
    y='delay_percentage')
.mark_bar()

)
chart2

#%%
print (chart2)
#%%

bars_month = (alt.Chart(month, title='Flights Delay Perentage', width = 400)
            .encode(
                  x = alt.X('month',
                        sort = ['month']),
                  y = alt.Y(
                  'delay_percentage',
                  scale = alt.Scale(domain = [0,100]), title = "Delay Percentage"),
                  color = alt.condition(
                        alt.datum.delay_percentage >= 24, alt.value('red'),
                        alt.value('steelblue')
                  ))
            .mark_bar()
            )
martin = ("Martin")

daniel = ("hola)")
