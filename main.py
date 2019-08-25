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



# Show the MENU and ask the user to input
def menu():
    print(MENU)
    userinput = input(">>>")
    return userinput


# Use at allplaces fun: to sort the list with key
def taken(elem):
    return elem[3]


# Show all places from list of places.csv file
# Sort the places by unvisited place
# Count visited place
def allplaces(sperate_places_list):
    for i in range(len(sperate_places_list)):
        sperate_places_list.sort(key=taken)
        if sperate_places_list[i][3] == "n":
            print(
                "*{}. {:<8} in {:<11} priority {}.".format(i + 1, sperate_places_list[i][0], sperate_places_list[i][1],
                                                           sperate_places_list[i][2]))
        else:
            print(
                " {}. {:<8} in {:<11} priority {}.".format(i + 1, sperate_places_list[i][0], sperate_places_list[i][1],
                                                           sperate_places_list[i][2]))
    print("")
    want_to_visit = count_visit()
    if want_to_visit > 0:
        print(" {} places. You still want to visit {} places.".format(len(sperate_places_list), want_to_visit))
    else:
        print(" {} places. No places left to visit. Why not add some more?".format(len(sperate_places_list)))
    print("")


# Use at allplaces fun: to count visit or not
def count_visit():
    want_to_visit = 0
    for i in range(len(sperate_places_list)):
        if sperate_places_list[i][3] == "n":
            want_to_visit += 1
    return want_to_visit


# Add new places to list of place.csv file
# Validate user input
def add_places():
    new_name = input("Name :")
    while not new_name:
        print("Input can not be blank")
        new_name = input("Name :")

    new_country = input("Country :")
    while not new_country:
        print("Input can not be blank")
        new_country = input("Country :")

    # Check user input blank or non-digit or underzero
    new_priority = priority_check()
    str_priority = str(new_priority)
    new_place_lists = [new_name, new_country, str_priority, "n"]
    sperate_places_list.append(new_place_lists)
    print("{} in {} (priority{}) added to Travel Tacker".format(new_name, new_country, new_priority))
    print("")


# Use at add_places fun: to check user input priority
def priority_check():
    valid = False
    while not valid:
        try:
            new_priority = int(input("Priority: "))
            while new_priority <= 0:
                print("Number must be more than 0.")
                new_priority = int(input("Priority: "))
                valid = True
            valid = True
        except ValueError:
            print("Invalid input, please enter a valid number.")
    return new_priority


# Mark user visited place at list of places.csv file
def mark_visisted():
    try:
        want_to_visit = count_visit()
        if want_to_visit > 0:
            visited_place = int(input("Enter the number of a place to mark as visited :"))
            while visited_place <= 0:
                print("Number must be greater than zero")
                visited_place = int(input("Enter the number of a place to mark as visited :"))
            if visited_place <= len(sperate_places_list):
                visited_place -= 1
                if sperate_places_list[visited_place][3] != "v":
                    sperate_places_list[visited_place][3] = 'v'
                    print("{:<8} in {:<11} visited!".format(sperate_places_list[visited_place][0],
                                                            sperate_places_list[visited_place][1]))
                else:
                    print("That place is already visited")
            else:
                print("Invalid place number")
        else:
            print("No Unvisited Places")
    except ValueError:
        print("Invalid input; enter a valid number!")
        mark_visisted()
