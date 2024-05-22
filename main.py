# ------------------------------------------------------------------------------------------------------------------
# INTRODUCTION

# Every year, American high school students take SATs, which are standardized tests intended to measure literacy, 
# numeracy, and writing skills. There are three sections - reading, math, and writing, each with a maximum score of 
# 800 points. These tests are extremely important for students and colleges, as they play a pivotal role in the 
# admissions process.

# Analyzing the performance of schools is important for a variety of stakeholders, including policy and education
# professionals, researchers, government, and even parents considering which school their children should attend.

# You have been provided with a dataset called schools.csv, which is previewed below.

# You have been tasked with answering three key questions about New York City (NYC) public school SAT performance.


# Import pandas
import pandas as pd

# Read the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# -------------------------------------------------------------------------------------------------------------------
# QUESTION 1: Which NYC schools have the best math results?

# The best math results are at least 80% of the *maximum possible score of 800* for math.
best_math_results = schools["average_math"] >= .8 * 800

# Columns to show
cols_to_subset_avg_math = ["school_name", "average_math"]

# Save the results in a pandas DataFrame and sort it by "average_math" in descending order.
best_math_schools = schools.loc[best_math_results, cols_to_subset_avg_math].sort_values("average_math", ascending=False)

# -------------------------------------------------------------------------------------------------------------------
# QUESTION 2: What are the top 10 performing schools based on the combined SAT scores?
# The combined SAT score refers to the sum of the scores from: Math, Reading, and Writing.

# Create new "total_SAT" column
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]

# Columns to show
cols_to_subset_total_sat = ["school_name", "total_SAT"]

# Save the results as a pandas DataFrame with results ordered by "total_SAT" in descending order.
schools_total_sat_srt = schools.loc[:, cols_to_subset_total_sat].sort_values("total_SAT", ascending=False)

# Find top 10 SAT score schools
top_10_schools = schools_total_sat_srt.head(10)