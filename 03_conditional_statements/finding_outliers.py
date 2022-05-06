# Program checks if a number is an outlier in the dataset and set the variable "outlier" to be True if its is.

upper_limit = 91
lower_limit = 24
outlier = False
number = 8

if number > upper_limit:
    outlier = True
if number < lower_limit:
    outlier = True
if outlier == True:
    print(f"{number} is an outlier")