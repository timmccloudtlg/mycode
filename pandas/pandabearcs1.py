 #!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Challenge Solution 01 - JSON to CSV"""

import pandas


# these following two lines are for writing to file
# use this when you are not rendering to a window
import matplotlib
matplotlib.use('Agg')

# create some graphs
import matplotlib.pyplot as plt




def main():

    # create a dataframe from json
    df = pandas.read_json("5movies.json")

    # writeout dataframe to CSV
    df.to_csv("5movies-translated-from-json.csv")

if __name__ == "__main__":
    main()
