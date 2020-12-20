#**Validere Coding Assessment**

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

##Step 3:
The user inputs their choices for the % values of the two oils in question.
This part of the program will have tests written to catch values that are not numeric and total 
percentages that do not amount to 100%. 

##Step 4:
Once the volumes have been obtained, the main of the program runs a method `getData()` that will retrieve the
CSV file from the specified location and attempt to parse it. Here, the program will test to see if the 
CSV is put in the proper directory and if the CSV is in the correct formatting, raising an exception for each.
The necessary transformations are then done to drop an NaN columns and rows. Furthermore, the program makes sure that
the length of data for both oils matches before continuing the program to ensure no data is missing. 

The final part of transformation comes by converting the uncertainties of the temperatures into `ufloat` values 
using the `uncertainties` python module and simplifying them by only taking their nominal values, as shown by 
simplifications `1`. An assumption made at this step is that any missing temperature data for any oil for a particular 
% of mass will take on the value of the previous highest temperature. This is further outlined in Assumptions `1`. 


**----SIMPLIFICATIONS----**
#### 1. 
The two oils will be taken as their respective nominal values only. This is done by using the `nominal` package. 


**----ASSUMPTIONS----**
####1. 
If there doesn't exist a temperature that the oil is evaporated beyond the previous %,
we will assume that there is no further evaporation that can be done, and we can assign the previous highest temperature
to it. This is done using the index of the dataframe records for each of the two oils in question. 

###**Requirements**

The following python modules/packages were used to run this program:

`numpy = 1.19.3`
`pandas = 1.1.5`
`uncertainties = 3.1.5`

