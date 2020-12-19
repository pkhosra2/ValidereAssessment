import pandas as pd
import numpy as np
import math
import os
from uncertainties import ufloat_fromstr, nominal_value


class DistillationCalculator(object):

    def __init__(self, volume1, volume2):
        self.volume1 = volume1
        self.volume2 = volume2

    def get_data(self):

        # creating our file path for the csv file taken from 'CrudeMonitor.ca'
        path = os.path.dirname(os.path.abspath(__file__))
        file_directory = path + '/crudes/crudecomp.CSV'

        # turning our csv file in the directory into a pandas DataFrame
        df = pd.read_csv(file_directory, header=1)

        # df = df.drop(0)                                    # dropping the first row in the given dataFrame
        df.drop(df.columns[-3:], axis=1, inplace=True)     # dropping the last 3 columns that have NaN
        df = df.dropna()                                   # dropping the NaN rows

        # grabbing the names of the two oils in question
        oil_names = [col for col in df.columns[1:]]

        oil1_df = df[oil_names[0]]
        oil2_df = df[oil_names[1]]

        # we need to check to see if both series of oils in the df are of equal length
        if len(oil1_df) == len(oil2_df):

            for index in df.index:
                # for each value in the first oil and second Series, we will first convert from string to float and the
                # only take the nominal value from each cell, this will be one of our simplifications
                # NOTE: if there doesn't exist a temperature that the oil is evaporated beyond the previous %,
                # we can assume that there is no further evaporation that can be done and we can assign the previous
                # temperature

                try:
                    df.at[index, oil_names[0]] = nominal_value(ufloat_fromstr(oil1_df[index]))
                except ValueError:
                    df.at[index, oil_names[0]] = df.at[index-1, oil_names[0]]
                try:
                    df.at[index, oil_names[1]] = nominal_value(ufloat_fromstr(oil2_df[index]))
                except ValueError:
                    df.at[index, oil_names[1]] = df.at[index-1, oil_names[1]]

        data = df.to_numpy()

        return data, oil_names

    def getDistilationProfile(self, volume1, volume2):

        """
        This method retrieves the clean data and corresponding oil_names from the csv file in the project directory and
        prints out the respective oil mixture temperatures at the necessary percentage buckets

        :param volume1: the volume of the first oil the user has specificed in percentage
        :param volume2: the volume of the second oil the user has specified in percentage
        :return: None
        """

        data, oil_names = self.get_data()
        print("The resulting Disillation temperatures for {oil_1} and {oil_2} are the following:\n"
              .format(oil_1=oil_names[0], oil_2=oil_names[1]))

        for array in data:
            temp = math.floor(array[-1]*volume2 + array[-2]*volume1)
            print("{mass_value} : {temp}".format(mass_value=array[0], temp=temp))

    def main(self):
        self.getDistilationProfile(self.volume1, self.volume2)


if __name__ == "__main__":

    print("Starting Distillation Profile Calculator...\n")
    print("Please enter two values for the two oils, please make sure the values add up to 100 in percentage\n")

    while True:
        try:
            volume1 = int(input("Please input the volume desired in % for the first oil\n"))
            try:
                volume2 = int(input("Please input the volume desired in % for the second oil\n"))
                if (volume1 + volume2) % 100 != 0:
                    print("Please provide two numbers that add up to 100, starting over...\n")
                    continue
                break
            except:
                print("Please enter a numeric value for second oil, starting over...\n")
        except:
            print("Please enter a numeric value\n")

    # converting the user inputted percentages into fraction that will be used later on in the program
    volume1 = int(volume1)/100
    volume2 = int(volume2)/100

    client = DistillationCalculator(volume1, volume2)
    client.main()

