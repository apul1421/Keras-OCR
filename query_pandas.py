import pandas as pd

# Assuming you already have a DataFrame named df_lineLocations

# Filter the DataFrame
filtered_df = df_lineLocations[df_lineLocations['line'] == 0]

# Group by cumSum and calculate the desired values
grouped_df = filtered_df.groupby('cumSum').agg(
    SegmentOrder=('rowLoc', lambda x: x.index.min()),
    SegmentStart=('rowLoc', 'min'),
    Height=('rowLoc', lambda x: x.max() - x.min())
).reset_index()

# Add the SegmentOrder column
grouped_df['SegmentOrder'] = grouped_df.index + 1

# Print the resulting DataFrame
print(grouped_df)
