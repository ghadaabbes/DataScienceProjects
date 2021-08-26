### Description

Analysis of a dataset of the global average sea level change since 1880.  Data used to predict the sea level change through year 2050.



* matplotlib used to create a scatter plot using the "Year" column as the x-axis and the "CSIRO Adjusted Sea Level" column as the y-axix.
* The `linregress` function from `scipy.stats` used to get the slope and y-intercept of the line of best fit. It plots the line of best fit over the top of the scatter plot and go through the year 2050 to predict the sea level rise in 2050.
* Another line of best fit just using the data from year 2000 through the most recent year in the dataset. It goes through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.


Unit tests are written for you under `test_module.py`.

### Development

For development, use `main.py` to test. Run `main.py`.

### Testing 

Tests are imported from `test_module.py` to `main.py`. The tests will run automatically whenever you run the `main.py`.


* Data used in this project are imported from `epa-sea-level.csv`.
### Data Source
Global Average Absolute Sea Level Change, 1880-2014 from the US Environmental Protection Agency using data from CSIRO, 2015; NOAA, 2015.
https://datahub.io/core/sea-level-rise
