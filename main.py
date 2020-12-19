
import json, requests
import pandas as pd
import csv
import math
import os


class DistillationCalculator(object):

    def __init__(self, volume1, volume2):
        self.volume1 = volume1
        self.volume2 = volume2

    def get_data(self):

        path = os.path.dirname(os.path.abspath(__file__))
        file_directory = path + '/crudes/crudecomp.CSV'

        df = pd.read_csv(file_directory)

        # grabbing the names of the two oils in question
        oil_name_1 = df['Unnamed: 1'].values[0]
        oil_name_2 = df['Unnamed: 2'].values[0]

        df = df.drop(0)                                     # dropping the first row in the given dataFrame
        df.drop(df.columns[-3:], axis=1, inplace=True)      # dropping the last 3 columns that have NaN
        df = df.dropna()                                    # dropping the NaN rows

    def getDistilationProfile(self, volume1, volume2):

        data = self.get_data()

        volume_total = volume1 + volume2

        return volume_total

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

    volume1 = int(volume1)/100
    volume2 = int(volume2)/100

    client = DistillationCalculator(volume1, volume2)
    client.main()

