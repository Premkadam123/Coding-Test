#1. Write a Python program to read a CSV file and display its contents.


#import csv
import csv

#
def read_csv(file_path):
    with open('D:\Demo\HR_Analytics.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

# Example usage
file_path = 'D:\Demo\HR_Analytics.csv'  # Replace with the path to your CSV file
read_csv(file_path) #read the file

