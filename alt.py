import altair as alt
import pandas as pd

# Sample Data
data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [2, 3, 5, 7, 11],
    'category': ['A', 'B', 'A', 'B', 'A']
})

# Create Scatter Plot
chart = alt.Chart(data).mark_point().encode(
    x='x',
    y='y',
    color='category'
)

chart.show()
