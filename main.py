"""
Name : Kyaw Phyo Aung
Date : 23.7.2019
Program Details : Travel Tacker
Github link : www.github.com/
"""
import sys

print("Travel Tracker 1.1 - by Kyaw Phyo Aung")
MENU = """Menu:
L - List places
A - Add new place
M - Mark a place as visited
Q - Quit
"""
DATAFILE = "places.csv"
database = open(DATAFILE, "r")
places = database.readlines()
place = [i.replace("\n", '') for i in places]
database.close()

# All data from csv file is stored in sperate_places_list as nested list
sperate_places_list = []
for i in range(len(place)):
    sperate_places_list.append(place[i].split(','))

