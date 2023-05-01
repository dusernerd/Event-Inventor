import re
import csv
import sys
import logged_in
from pyfiglet import Figlet


figlet = Figlet()
font_name = "digital"
figlet.setFont(font = font_name)

def main():

    while True:
        value = welcome_page()
        if value == 1:
            entered = login_page()
            #print(*entered)
            ver_email = verify_user_email(entered[0])
            ver_password = verify_user_password(entered[1])
            if ver_email == True and ver_password == True:
                print("Entered seccessfully")
                print(figlet.renderText("Welcome to Event-Inventor"))
                logged_in.main()
            else:
                print("User not found")



        if value == 2:
            values = signup_page()
            verified = verify_user_email_sign_up(values[1])
            if verified == False:
                signup_page()
            else:
                store_user_data(*values)
                print("Your account is successfully registered")
        if value == 3:
            sys.exit("Your program is closed")

def welcome_page():
    print("\t--------Welcome to Event-Inventor--------")
    print("1. Log in")
    print("2. Create an account")
    print("3. Exit")

    while True:
        try:
            option = int(input("Please Enter the Coresponding Digit: "))
            if option != 1 and option !=2 and option !=3:
                print("Please select either 1, 2 or 3")
                continue
            return option

        except ValueError:
            print("Please select either 1, 2 or 3")
            continue
        except EOFError:
            print("\nThe process is killed")
            break

def login_page():
    print("\t\t----Login page----")
    while True:
        try:
            email = input("Email: ")
            password = input("Password: ")
            return email,password
        except ValueError:
            print("Incorrect format, Try again")
            pass



def signup_page():
    print("\t\t----------Sign Up----------")
    while True:
        try:
            full_name = input("Please Enter your First Name and Last Name: ")
            break
        except ValueError:
            print("Not a Correct Format")
            continue
        except EOFError:
            print("\nThe process is killed")
            break
    while True:
        try:
            email = input("Please Enter your Email Address: ")
            if re.fullmatch(r"(\w\.?)+@(\w+\.)?\w+\.com",email, re.IGNORECASE):
                break
            print("Invalid Format, Type Again")
            continue
        except ValueError:
            print("Not a Correct Format")
            continue
        except EOFError:
            print("\nThe process is killed")
            break
    while True:
        try:
            password = input("Please Enter your password must have at least 8 characters with at least 1 digit: ")
            if len(password) < 8 or not re.fullmatch(r".*\d+.*",password):
                print("Invalid Format, Type Again")
                continue
            break
        except ValueError:
            print("Not a Correct Format")
            continue
        except EOFError:
            print("\nThe process is killed")
            break

    try:
        return full_name, email, password
    except UnboundLocalError:
        print("Wrong number of value")
def verify_user_email_sign_up(e):
    while True:
        try:
            with open("/workspaces/128981940/project/user_data.txt") as file:
                for line in file:
                    if e in line:
                        print("User already exists")
                        return False

            return True
        except FileNotFoundError:
            print("No such a file")
            pass
def store_user_data(fname, e, p):
     try:
        with open("user_data.txt", "a") as file:
            writer = csv.DictWriter(file, fieldnames = ["email", "password", "name"])
            writer.writerow({"email":e, "password": p, "name" : fname })

     except FileNotFoundError:
        print("No such a file")
        pass


#def login_page(e, p):
 #   while True:
  #      try:
   #         e = input("Email: ")
    #        p = input("Password: ")
     #       verify_user_email(e)
      #      verify_user_password(p)
#
 #       except ValueError:
  #          print("Wrong email or password, try again")
   #         pass

def verify_user_email(email):
    try:
        with open("/workspaces/128981940/project/user_data.txt", "r") as file:
            reader = csv.DictReader(file)
            for lines in reader:
                em = lines["email"]
                if email in em:
                    return True
            return False
    except FileNotFoundError:
        print("File not found")
def verify_user_password(password):
    with open("/workspaces/128981940/project/user_data.txt") as file:
        reader = csv.DictReader(file)
        for lines in reader:
            pass_w = lines["password"]
            if password in pass_w:
                return True
        return False




if __name__ == "__main__":
    main()