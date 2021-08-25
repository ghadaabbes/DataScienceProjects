Visualization of time series data using a line chart, bar chart, box plots, Pandas, Matplotlib, and Seaborn to visualize a dataset containing the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03. The data visualizations will help you understand the patterns in visits and identify yearly and monthly growth.

Tasks:
* Setting the index to the "date" column.
* Cleanning the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
* Creating a `draw_line_plot` function that uses Matplotlib to draw a line chart "examples/Figure_1.png". The title "Daily freeCodeCamp Forum Page Views 5/2016-12/2019". The label on the x axis should be "Date" and the label on the y axis should be "Page Views".
* Creating a `draw_bar_plot` function that draws a bar chart  "examples/Figure_2.png". It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of "Months". On the chart, the label on the x axis is "Years" and the label on the y axis is "Average Page Views".
* Creating a `draw_box_plot` function that uses Searborn to draw two adjacent box plots  "examples/Figure_3.png". These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be "Year-wise Box Plot (Trend)" and the title of the second chart should be "Month-wise Box Plot (Seasonality)". Make the month labels on bottom start at "Jan" and the x and x axis are labeled correctly.

For each chart,I used a copy of the data frame. Unit tests are written under `test_module.py`.

### Development

For development, you can use `main.py` to test. Run `main.py`.

### Testing 

I imported the tests from `test_module.py` to `main.py`. The tests will run automatically whenever you run `main.py`.

