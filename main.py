
import pandas as pd
import numpy as np
import csv
import os
from uncertainties import ufloat, ufloat_fromstr, nominal_value

class DistillationCalculator(object):

    def __init__(self, volume1, volume2):
        self.volume1 = volume1
        self.volume2 = volume2

    def get_data(self):

        path = os.path.dirname(os.path.abspath(__file__))
        file_directory = path + '/crudes/crudecomp.CSV'

        # turning our csv fiel in the directory into a pandas DataFrame
        df = pd.read_csv(file_directory)

        # grabbing the names of the two oils in question
        oil_name_1 = df['Unnamed: 1'].values[0]
        oil_name_2 = df['Unnamed: 2'].values[0]

        df = df.drop(0)                                     # dropping the first row in the given dataFrame
        df.drop(df.columns[-3:], axis=1, inplace=True)      # dropping the last 3 columns that have NaN
        df = df.dropna()                                    # dropping the NaN rows

        oil1_df = df['Unnamed: 1']
        oil2_df = df['Unnamed: 2']

        # we need to check to see if both series of oils in the df are of equal length
        if len(oil1_df) == len(oil2_df):

            for index in df.index:
                # for each value in the first oil and second Series, we will first convert from string to float and the
                # only take the nominal value from each cell, this will be one of our simplifications
                try:
                    df.at[index, 'Unnamed: 1'] = nominal_value(ufloat_fromstr(oil1_df[index]))
                except ValueError:
                    df.at[index, 'Unnamed: 1'] = 0
                try:
                    df.at[index, 'Unnamed: 2'] = nominal_value(ufloat_fromstr(oil2_df[index]))
                except ValueError:
                    df.at[index, 'Unnamed: 2'] = 0

        data = df.to_numpy()

        return data

    def getDistilationProfile(self, volume1, volume2):

        """
        :param volume1: the volume of the first oil the user has specificed in percentage
        :param volume2: the volume of the second oil the user has specified in percentage
        :return: approximate temperature of distillation of the mixture of oils at various mass % values
        """

        data = self.get_data()

        temperature = volume1 + volume2

        return temperature

    def main(self):
        self.getDistilationProfile(self.volume1, self.volume2)


if __name__ == "__main__":
    print("Starting Distilation Profile Calculator...\n")
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

