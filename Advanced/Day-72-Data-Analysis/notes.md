## Learning Points & Summary
Learning notes. We have:

- Used `.groupby()` to explore the number of posts and entries per programming language
- Converted strings to **Datetime**  objects `with to_datetime()` for easier plotting
- Reshaped our DataFrame by converting categories to columns using `.pivot()`
- Used `.count()` and `isna()` `.values.any()` to look for NaN values in our DataFrame, which we then replaced using `.fillna()`
- Created (multiple) line charts using `.plot()` with a for-loop
- Styled our charts by changing the size, the labels, and the upper and lower bounds of our axis.
- Added a legend to tell apart which line is which by colour
- Smoothed out our time-series observations with `.rolling()` `.mean()` and plotted them to better identify trends over time.

