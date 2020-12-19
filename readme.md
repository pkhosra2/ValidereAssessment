# Validere Coding Asssessment

Given the parameters of the problem the goal of this problem is
to predict the Distillation Profile of combining any two oils 
together at a given % of volume.

### Step 1:
The first step is two understand the data we will be working with.
Namely, we will locate the proper location on the 'CrudeMonitor.ca'
website to pull the necessary Distillation Profiles for our two
oils of choice.

### Step 2:
Next we need to develop a model that will ultimately provide us with
the temperature of the oil mixture. As described, the Distillation
profile is a snapshot of a function that take a percentage as input
and outputs a corresponding temperature.

This knowledge can be leveraged and used to create a simple model
that will use the temperature of each oil at a given volume percentage as an 
inputs to calculate the average temperature of the given oils.


----SIMPLIFICATIONS----
### 1. 
The two oils will be taken as their respective medians, lower, and upper limits


----ASSUMPTIONS----


