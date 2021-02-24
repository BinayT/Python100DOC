##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
# name,email,year,month,day
# Test,test@email.com,1961,12,21
# [Fill this in!]

import csv
import pandas
import random
import datetime
import smtplib

# data = []
# run = None
#
# ask_first = input("Do you want to add people in the list of birthdays? (y/n)   ")
# if ask_first == 'y':
#     run = True
#
# while run:
#     name = input("Name:  ")
#     email = input("Email:  ")
#     year = input("Year:  ")
#     month = input("Month:  ")
#     day = input("Day:  ")
#     data.append([name, email, year, month, day])
#     continue_adding = input("Continue adding (y/n):   ")
#     if continue_adding == 'n':
#         run = False
#
#
# with open('birthdays.csv', 'a', newline='') as birthday_file:
#     for item in data:
#         csv_writer = csv.writer(birthday_file)
#         csv_writer.writerow(item)

letter_template = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
random_letter = random.choice(letter_template)

current_date = datetime.datetime.now()
month = current_date.month
day = current_date.day

birthday_file = pandas.read_csv('birthdays.csv')
today_birthday = birthday_file[(birthday_file['month'] == month) & (birthday_file['day'] == day)].values.tolist()

with open(f'letter_templates/{random_letter}', mode="r") as letter_file:
    letter = letter_file.read()
    letter_with_name = letter.replace('[NAME]', today_birthday[0][0])

connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user="emailhere@gmail.com", password='passwordhere')
connection.sendmail(from_addr="emailhere@gmail.com",
                    to_addrs=today_birthday[0][1],
                    msg=f"Subject:Happy Birthday {today_birthday[0][0]}\n\n{letter_with_name}")
connection.close()

# with open('birthdays.csv', newline='') as birthday_file:
#     file = csv.reader(birthday_file)
#     for item in file:
#         print(item)
