import csv
import random
import sys

def main():
    # List to hold the rows of the CSV file
    data = []

    # Open the CSV file for reading
    with open("/home/nathan/Documents/MinesWork/CSCI565/PA_Graph/lasftm_asia/lastfm_asia_edges.csv", 'r') as file:
        csv_reader = csv.reader(file)  # Create a CSV reader object
        for row in csv_reader:
            data.append(row) 
        
    with open(sys.argv[1], 'w') as file:
        # Iterate through each row in the CSV file
        for i, dat in enumerate(data):
            random_number = random.randint(1, 100)
            file.write(f"{dat[0]} {dat[1]} {random_number} 0.0001\n")

if __name__ == "__main__":
    main()