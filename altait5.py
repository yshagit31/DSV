import pandas as pd
import altair as alt

data = pd.read_csv('larger_data.csv')

data_sample = data.sample(n=20, random_state=1)  

scatter_plot = alt.Chart(data_sample).mark_point(size=50, opacity=0.7).encode(
    x=alt.X('age:Q', scale=alt.Scale(domain=[20, 45])),  
    y=alt.Y('income:Q', scale=alt.Scale(domain=[45000, 90000])), 
    color=alt.Color('education_level:N', scale=alt.Scale(scheme='category10')),  
    tooltip=['age:Q', 'income:Q', 'education_level:N'] 
).properties(
    title='Scatter Plot of Age vs. Income by Education Level'
)

scatter_plot.save('scatter_plot_new.html')
