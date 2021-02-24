##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
# name,email,year,month,day
# Test,test@email.com,1961,12,21
# [Fill this in!]

import csv

data = []
run = None

ask_first = input("Do you want to add people in the list of birthdays? (y/n)   ")
if ask_first == 'y':
    run = True

while run:
    name = input("Name:  ")
    email = input("Email:  ")
    year = input("Year:  ")
    month = input("Month:  ")
    day = input("Day:  ")
    data.append([name, email, year, month, day])
    continue_adding = input("Continue adding (y/n):   ")
    if continue_adding == 'n':
        run = False


with open('birthdays.csv', 'a', newline='') as birthday_file:
    for item in data:
        csv_writer = csv.writer(birthday_file)
        csv_writer.writerow(item)






