import pandas as pd
import altair as alt

# Load the dataset
data = pd.read_csv('larger_data.csv')

# Create a selection for filtering by education level
selection = alt.selection_point(
    fields=['education_level'],
    bind='legend'
)

# Create a scatter plot with interactive filtering
interactive_scatter_plot = alt.Chart(data).mark_point().encode(
    x='age:Q',
    y='income:Q',
    color=alt.Color('education_level:N', scale=alt.Scale(scheme='category10')),  # Color by education level
    tooltip=['age:Q', 'income:Q', 'education_level:N']  # Display additional info on hover
).add_params(
    selection
).transform_filter(
    selection
).properties(
    title='Interactive Scatter Plot of Age vs. Income'
)

# Save the plot as an HTML file
interactive_scatter_plot.save('interactive_scatter_plot.html')
