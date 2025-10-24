Practice Case Study: TechCorp Trial Signups

Scenario:
TechCorp tracks the daily number of users who sign up for their free trial. 
They recorded 40 days of data to analyze signup trends and need you to provide a descriptive analysis.

Data Set (N = 40 days):
trial_signups = [50, 52, 55, 55, 58, 60, 60, 60, 61, 62, 63, 64, 65, 65, 66, 68, 68, 70, 70, 71, 
                 72, 72, 73, 75, 75, 76, 78, 80, 80, 85, 88, 90, 92, 95, 100, 105, 110, 120, 140, 180]

------------------------------------------------------------
Task 1: Positional Statistics

Using the trial_signups data and your custom functions (min, max, sorted_data access), answer the following:

1. Range:
   - Calculate the range of the data.

2. Positional Values:
   - Calculate the value of the 10th smallest signup day.
   - Calculate the value of the 5th largest signup day.
   (Hint: Use Python's indexing on the sorted list.)

------------------------------------------------------------
Task 2: Measures of Central Tendency

Using your custom Python functions for central tendency (mean, median, mode):

1. Mean:
   - Calculate the mean (average) number of daily trial signups.

2. Median:
   - Calculate the median number of daily trial signups.

3. Mode:
   - Calculate the mode(s) of the daily trial signups.

4. Quantile:
   - Calculate the 75th percentile (p = 0.75) using your quantile function.

------------------------------------------------------------
Task 3: Visualization and Interpretation

1. Code the Bar Chart:
   - Create a frequency bar chart using Counter and plt.bar().
   - Set the x-axis to cover the full range of the data (e.g., 40 to 190).
   - Set the y-axis to a relevant maximum (Hint: The max frequency is 4).
   - Use clear titles and axis labels (e.g., "Daily Signups", "Number of Days").
   - Plot the result. (Do not share the code — just run it for your practice.)

2. Interpretation:
   Based on your calculated Mean, Median, and Mode, and the visualization you created:

   - Skewness:
     How would you describe the shape of the distribution (symmetric, right-skewed, or left-skewed)?

   - Outlier Impact:
     Which calculated statistic (Mean, Median, or Mode) is most influenced by the very high signup days (e.g., 140 and 180)?

   - Business Insight:
     If you were reporting the "typical" signup day to the CEO, which measure (Mean or Median) would you use, and why?
