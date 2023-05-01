from datetime import date
import csv
import os
i = -1
def main():
    global i
    i += 1
    while True:
        value = first_page()
        if value == 1:
            create_eve_page(i)
        elif value == 2:
            show_eves_page(i)
        elif value == 3:
            break

def first_page():
    print("1. Create an event")
    print("2. Show current events")
    print("3. Log out")
    try:
        return int(input("Please Select: "))
    except ValueError:
        print("Please enter either 1, 2 or 3")

def create_eve_page(n):
    while True:
        try :
            name_of_eve = input("How do you want to name it? ")
            place_of_eve = input("Enter the location: ")
            date_of_eve_in = input("Enter the date in the following format YY-MM-DD: ")
            date_of_eve = date.fromisoformat(date_of_eve_in)
            with open(f"event_{n}.txt","a") as file:
                writer = csv.DictWriter(file, fieldnames = ["name", "place","date"])
                writer.writeheader()
                writer.writerow({"name":name_of_eve, "place" :place_of_eve, "date": date_of_eve})
            guest_list(f"event_{n}.txt")
            #return name_of_eve, place_of_eve, date_of_eve
        except ValueError:
            print("Something went wrong")


def guest_list(path):
    with open(path,"a") as file:
                writer = csv.DictWriter(file, fieldnames = ["Guest's list: "])
                writer.writeheader()
    while True:
        text = input("Guest's First name and last name, if None enter '>' ")
        if text == ">":
            main()
        else:
            with open(path,"a") as file:
                writer = csv.DictWriter(file, fieldnames = ["names"])
                writer.writerow({"names":text})


def show_eves_page(n):
    for i in range(n):
        with open(f"/workspaces/128981940/project/event_{i}.txt") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]
                place = row["place"]
                date = row["date"]
                print(i+1, name, place, date)
                break
    try:
        event = int(input("Select the event to get the details: "))
    except ValueError:
        print("Something Went Wrong")
    showing_selected_event(event - 1)

def showing_selected_event(index):
    os.system('cls' if os.name == 'nt' else 'clear')
    with open(f"/workspaces/128981940/project/event_{index}.txt") as file:
        for lines in file:
            print(lines, end= "")
    while True:
        _ = input("Press Enter to Continue ")
        break



if __name__ == "__main__":
    main()