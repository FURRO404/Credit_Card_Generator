#====================FURRO404====================#
#Credit_Card_Generator.py
#Caution: This can be used for malicious purposes
#Im not liable for your actions
import random
import datetime
import time
#-------------------#
#Lists And User Input
list1 = []
list2 = []

user_input = str(input("Type in a credit card you would like\n - (1) Visa \n - (2) MasterCard \n - (3) Discover \n - (4) American Express \nCommand ~ "))
time1 = int(input("\nHow many credit cards do you want: "))
#-----------------------------------------------------------------------#    
if user_input == "1":
    for i in range(0,time1):
        l = list1.clear()
        p = list2.clear()
        for i in range(0,16):
            n = random.randint(0,9)
            list1.append(n)
        for i in range(0,3):
            o = random.randint(0,9)
            list2.append(o)

        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2030, 12, 31)

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)

        print("")
        print("Your credit card number:", list1)

        print("Your cve:", list2)

        print("The expiration date:", random_date)
        time.sleep(1)
#----------------------------------------------------------#    
elif user_input == "2":
    for i in range(0,time):
        for i in range(0,16):
            n = random.randint(0,9)
            list1.append(n)
        for i in range(0,3):
            o = random.randint(0,9)
            list2.append(o)

        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2030, 12, 31)

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)

        print("")
        print("Your credit card number:", list1)

        print("Your cve:", list2)

        print("The expiration date:", random_date)
        time.sleep(1)
#----------------------------------------------------------#    
elif user_input == "3":
    for i in range(0,time):
        for i in range(0,16):
            n = random.randint(0,9)
            list1.append(n)
        for i in range(0,3):
            o = random.randint(0,9)
            list2.append(o)

        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2030, 12, 31)

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)

        print("")
        print("Your credit card number:", list1)

        print("Your cve:", list2)

        print("The expiration date:", random_date)
        time.sleep(1)
#----------------------------------------------------------#    
elif user_input == "4":
    for i in range(0,time):
        for i in range(0,16):
            n = random.randint(0,9)
            list1.append(n)
        for i in range(0,3):
            o = random.randint(0,9)
            list2.append(o)

        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2030, 12, 31)

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)

        print("")
        print("Your credit card number:", list1)

        print("Your cve:", list2)

        print("The expiration date:", random_date)
        time.sleep(1)
#----------------------------------------------------------#    
else:
    print("It seems like you misunderstood, please try again and read the instructions carefully!")
#====================FURRO404====================#
