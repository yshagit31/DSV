import pandas as pd
import altair as alt

# Load the dataset
data = pd.read_csv('data.csv')

# Display the first few rows of the dataset
print(data.head())

# Create a scatter plot
scatter_plot = alt.Chart(data).mark_point().encode(
    x='age',  # Replace with your column name
    y='income',  # Replace with your column name
    color='gender'  # Optional: Replace with your column name for color coding
)

# Save the plot as an HTML file
scatter_plot.save('scatter_plot.html')
