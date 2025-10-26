from __future__ import division
from collections import Counter
import matplotlib.pyplot as plt



#Data Set (N = 40 days):
trial_signups = [50, 52, 55, 55, 58, 60, 60, 60, 61, 62, 63, 64, 65, 65, 66, 68, 68, 70, 70, 71,
                 72, 72, 73, 75, 75, 76, 78, 80, 80, 85, 88, 90, 92, 95, 100, 105, 110, 120, 140, 180]


"""Task 1: Positional Statistics"""
#1. Range: - Calculate the range of the data.
trial_count = Counter(trial_signups)
max_signups = max(trial_count)
min_signups = min(trial_signups)
range_data = max_signups -min_signups
print(f"The range of the data is: {range_data}")

#2. Positional Values:- Calculate the value of the 10th smallest signup day.
#Calculate the value of the 5th largest signup day. """

sorted_data = sorted(trial_signups)
tenth_smallest_signups = sorted_data[9]
print(f"The 10th smallest signup day is: {tenth_smallest_signups}")
fifth_largest_signups = sorted_data[-5]
print(f"The 5th largest signup day is: {fifth_largest_signups}")

"""Task 2: Measures of Central Tendency"""
#1. Mean:- Calculate the mean (average) number of daily trial signup

def mean(x):
    return sum(x) / len(x)
print(f"The mean(average) # of daily trial signups: {mean(trial_signups)}")

#2. Median:- Calculate the median number of daily trial signups.
def median(v):
    """This finds the middle most number or the average of the middle most numbers"""
    n=len(v)
    sorted_d = sorted(v)
    midpoint = n//2
    if n % 2 == 1:
        return sorted_d[midpoint]
    else:
        lo = midpoint
        hi = midpoint - 1
        return (sorted_d[lo]+sorted_d[hi])/2
print(f"The median daily trial signup is: {median(trial_signups)}")

#3. Mode:- Calculate the mode(s) of the daily trial signups.
def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [trial for trial, count in counts.items()
            if count == max_count ]
print(f"the most freq trial signup is: {mode(trial_signups)}")


#4. Quantile-Calculate the 75th percentile (p = 0.75) using your quantile function.
def quantile(x,p):
    n =len(x)
    p_index = int(p * len(x))
    return sorted(x)[p_index]
print(f"The 75th percentile: {quantile(sorted_data, 0.75)}" )

"""Task 3: Visualization and Interpretation"""
xs = range(181)
ys = [trial_count[x] for x in xs]
plt.bar(xs, ys, color='skyblue', edgecolor ='black', width=1.0)
plt.axis([41, 181,0, 4])
plt.title('Frequency of Daily trial Signups')
plt.xlabel('Daily Signups')
plt.ylabel('Number of Days(Frequency)')
median_value = median(trial_signups)
mean_value = mean(trial_count)
plt.axvline(median_value, color='red', linestyle='--', linewidth=2, label=f"Median = {median_value:.2f}")
plt.axvline(mean_value, color='blue', linestyle='--', linewidth=2, label=f"Mean = {mean_value:.2f}")
plt.legend()
plt.show()
plt.savefig('histogram_trial_signups.png')


#Task 3: Interpretation (Written Answers)
"""The frequency bar chart below illustrates the distribution of the daily trial signups. It shows that most days have signups 
concentrated between 50 and 80, with a few days having significantly higher signups."""


"""Interpretation Skewness:The distribution is Right-Skewed (or positively skewed). This is evident because the long tail
 of the distribution extends to the right (higher values), and the measures of central tendency follow the relationship:
 Mode (60) < Median (71.5) < Mean (78.225)}
 Outlier Impact:The calculated statistic being most influenced by the very high signup days (140 and 180) is the Mean. 
 The mean is calculated using the value of every single data point, so extreme values pull the average toward them. The median and mode are less affected by these outliers."""


"""Business Insight:If reporting the "typical" signup day to the CEO, I would use the Median (71.5).
Reasoning: The median is resistant to outliers. Since the data is significantly right-skewed by a few very high signup days, the Mean (approx 78)
 is pulled higher and overstates what a common or typical day looks like. The Median (71.5) provides a more accurate representation of the central 
 value that separates the lower 50% of days from the upper 50%."""