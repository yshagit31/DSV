import pandas as pd
import altair as alt
import os

# Load the dataset
data = pd.read_csv('larger_data.csv')

# Sample a subset of the data to reduce congestion for scatter plot
data_sample = data.sample(n=20, random_state=1)

# Create a directory to save the plots
output_dir = 'plots'
os.makedirs(output_dir, exist_ok=True)

# Scatter Plot
scatter_plot = alt.Chart(data_sample).mark_point(size=50, opacity=0.7).encode(
    x=alt.X('age:Q', scale=alt.Scale(domain=[20, 45])),
    y=alt.Y('income:Q', scale=alt.Scale(domain=[45000, 90000])),
    color=alt.Color('education_level:N', scale=alt.Scale(scheme='category10')),
    tooltip=['age:Q', 'income:Q', 'education_level:N']
).properties(
    title='Scatter Plot of Age vs. Income by Education Level'
)
scatter_plot.save(os.path.join(output_dir, 'scatter_plot.html'))

# Bar Chart: Count of Education Levels
bar_chart = alt.Chart(data).mark_bar(size=40).encode(  # Adjusted bar size
    x=alt.X('education_level:N', title='Education Level', axis=alt.Axis(labelAngle=-45)),  # Rotate labels for better readability
    y=alt.Y('count()', title='Count'),
    color=alt.Color('education_level:N', scale=alt.Scale(scheme='category10'))
).properties(
    title='Count of Education Levels',
    width=500,
    height=300
).configure_axis(
    labelFontSize=12,
    titleFontSize=14
).configure_title(
    fontSize=16
).configure_bar(
    stroke='black',
    strokeWidth=0.5
)
bar_chart.save(os.path.join(output_dir, 'bar_chart.html'))

# Histogram: Distribution of Ages
histogram = alt.Chart(data).mark_bar().encode(
    x=alt.X('age:Q', bin=True, title='Age'),
    y=alt.Y('count()', title='Count'),
    color=alt.Color('education_level:N', scale=alt.Scale(scheme='category10'))
).properties(
    title='Distribution of Ages'
)
histogram.save(os.path.join(output_dir, 'histogram.html'))

# Box Plot: Income by Education Level with spacing
box_plot = alt.Chart(data).mark_boxplot(size=40).encode(
    x=alt.X('education_level:N', title='Education Level'),
    y=alt.Y('income:Q', title='Income'),
    color=alt.Color('education_level:N', scale=alt.Scale(scheme='category10'))
).properties(
    title='Income by Education Level',
    width=500,
    height=300
).configure_axis(
    labelFontSize=12,
    titleFontSize=14
).configure_title(
    fontSize=16
).configure_boxplot(
    median={'color': 'red', 'size': 2},  # Customize the median line color and size
    box={'color': 'blue', 'opacity': 0.6},  # Customize the box color and opacity
    outliers={'color': 'black'}  # Customize the outliers color
)
box_plot.save(os.path.join(output_dir, 'box_plot.html'))

# Line Chart: Average Income by Age
line_chart = alt.Chart(data).mark_line().encode(
    x=alt.X('age:Q', title='Age'),
    y=alt.Y('average(income):Q', title='Average Income'),
    color=alt.Color('education_level:N', scale=alt.Scale(scheme='category10'))
).properties(
    title='Average Income by Age'
)
line_chart.save(os.path.join(output_dir, 'line_chart.html'))

# Heatmap: Age vs. Income with Count
heatmap = alt.Chart(data).mark_rect().encode(
    x=alt.X('age:Q', bin=alt.Bin(maxbins=30), title='Age'),
    y=alt.Y('income:Q', bin=alt.Bin(maxbins=30), title='Income'),
    color=alt.Color('count()', scale=alt.Scale(scheme='viridis'), title='Count')
).properties(
    title='Heatmap of Age vs. Income'
)
heatmap.save(os.path.join(output_dir, 'heatmap.html'))
