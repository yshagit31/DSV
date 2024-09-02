import pandas as pd
import altair as alt

# Load the dataset
data = pd.read_csv('larger_data.csv')

# Sample a subset of the data to reduce congestion for scatter plot
data_sample = data.sample(n=20, random_state=1)

# Scatter Plot
scatter_plot = alt.Chart(data_sample).mark_point(size=50, opacity=0.7).encode(
    x=alt.X('age:Q', scale=alt.Scale(domain=[20, 45])),
    y=alt.Y('income:Q', scale=alt.Scale(domain=[45000, 90000])),
    color=alt.Color('education_level:N', scale=alt.Scale(scheme='category10')),
    tooltip=['age:Q', 'income:Q', 'education_level:N']
).properties(
    title='Scatter Plot of Age vs. Income by Education Level',
    width=300,
    height=300
)

# Bar Chart: Count of Education Levels
bar_chart = alt.Chart(data).mark_bar(size=40).encode(
    x=alt.X('education_level:N', title='Education Level', axis=alt.Axis(labelAngle=-45)),
    y=alt.Y('count()', title='Count'),
    color=alt.Color('education_level:N', scale=alt.Scale(scheme='category10'))
).properties(
    title='Count of Education Levels',
    width=300,
    height=300
)

# Histogram: Distribution of Ages
histogram = alt.Chart(data).mark_bar().encode(
    x=alt.X('age:Q', bin=True, title='Age'),
    y=alt.Y('count()', title='Count'),
    color=alt.Color('education_level:N', scale=alt.Scale(scheme='category10'))
).properties(
    title='Distribution of Ages',
    width=300,
    height=300
)

# Box Plot: Income by Education Level
box_plot = alt.Chart(data).mark_boxplot(size=40).encode(
    x=alt.X('education_level:N', title='Education Level'),
    y=alt.Y('income:Q', title='Income'),
    color=alt.Color('education_level:N', scale=alt.Scale(scheme='category10'))
).properties(
    title='Income by Education Level',
    width=300,
    height=300
)

# Line Chart: Average Income by Age
line_chart = alt.Chart(data).mark_line().encode(
    x=alt.X('age:Q', title='Age'),
    y=alt.Y('average(income):Q', title='Average Income'),
    color=alt.Color('education_level:N', scale=alt.Scale(scheme='category10'))
).properties(
    title='Average Income by Age',
    width=300,
    height=300
)

# Heatmap: Age vs. Income with Count
heatmap = alt.Chart(data).mark_rect().encode(
    x=alt.X('age:Q', bin=alt.Bin(maxbins=30), title='Age'),
    y=alt.Y('income:Q', bin=alt.Bin(maxbins=30), title='Income'),
    color=alt.Color('count()', scale=alt.Scale(scheme='viridis'), title='Count')
).properties(
    title='Heatmap of Age vs. Income',
    width=300,
    height=300
)

# Combine charts into a grid with spacing adjustments
combined_chart = alt.vconcat(
    alt.hconcat(scatter_plot, bar_chart, spacing=20),  # Add spacing between charts in a row
    alt.hconcat(histogram, box_plot, spacing=20),
    alt.hconcat(line_chart, heatmap, spacing=20),
    spacing=40  # Add spacing between rows
).properties(
    title='Combined Visualizations',
    width=650
).configure_title(
    fontSize=16
)

# Save the combined chart as an HTML file
combined_chart.save('combined_plots.html')
