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

# Main Function including other many functions
def main():
    userinput = menu()
    while userinput != "q":
        if userinput == "l":
            allplaces(sperate_places_list)
            userinput = menu()
        elif userinput == "a":
            add_places()
            userinput = menu()
        elif userinput == "m":
            allplaces(sperate_places_list)
            mark_visisted()
            userinput = menu()
        else:
            print("Invalid menu choice")
            userinput = menu()

    # Write all changes data to csv file / remove ',' at the end of line
    database = open(DATAFILE, "w")
    for newdata in sperate_places_list:
        for dataset in newdata:
            if dataset == "n" or dataset == "v":
                dataset.replace(",", '')
                database.write(dataset)
            else:
                database.write(dataset + ",")

        database.write("\n")
    database.close()

    print("{} places saved to {}".format(len(sperate_places_list), DATAFILE))
    print("Have a nice day :)")
    sys.exit()


