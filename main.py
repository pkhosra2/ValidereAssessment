import math
import json, requests
import time
from constants import evap_percentage, cm_url


class DistillationCalculator(object):

    def __init__(self, url):
        self.url = url

    def scrapeCrudeMonitor(self,url):
        try:
            response = requests.get(url)
        except requests.exceptions.SSLError:    # Happens when too many requests are made in a short period of time
            print('Going to sleep now:')        # This means it will just wait until it is successful again
            time.sleep(30)
            print('Awake again: Retrying api call')
            continue

        print(response.json())


    def getDistilationProfile(self, cm_url, percentage_evaporated):

        dist_profile1, distprofile2 = self.scrapeCrudeMonitor(cm_url)

        return temperature



def main(self):

    # 1. We need to develop a model that will give us an approximate distillation profile of the mixture of the two
#   oils with specified volumes\
    # 2. Collect Data pulled from 'Crude Montior' for a random set of two oils, clean the data and pass the values to
    # method created in step 1
    # Unit Test the method created using proper standards

    self.getDistilationProfile(cm_url)

if __name__ == "__main__":
    print("Starting Distilation Profile Calculator...")
    DistillationCalculator(cm_url).main()