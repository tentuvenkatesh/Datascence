import time
print("QuickHealth Pro Max Interactive Symptom Checker")
print("Hello there! Let's check how you're doing today.")
Name = input("Enter your name: ")
gender = input("enter your generder: ")
Age = int(input("Enter your age: "))
City = input("Enter your city name: ")
print("Symptoms & Health Info")
time.sleep(3)
symptoms = input("Select all symptoms you're experiencing: ")
harder = input("which one is harder to manage: ")
temp = float(input("what is your body temperature: "))
num_days = int(input("Number of Days you’ve felt unwell: "))
smoke = bool(input("Do You smoke: "))
last_Sleep = int(input("how many hours you slept in the last night: "))
mood = input("what is your current mood: ")
his = bool(input("do you have any pre-existing problerms like diabetics,etc"))
print("Running health tracker")
print("Your Health Summary")
time.sleep(5)
if num_days <= 2 and temp <= 98 and last_Sleep>8:
    print("Low Risk: You're likely okay. Stay hydrated and rested.")
else:
    print("High risk")
print("Personalized Advice")
time.sleep(5)
if num_days <= 2 and temp <= 98 and last_Sleep>8:
    print("Manage your chronic conditions carefully during illness.")
else:
    print("Visit some docter")
print("Mental Wellness Tip")
time.sleep(5)
if num_days <= 2 and temp <= 98 and last_Sleep>8:
    print("Keep it up! Maybe share your positivity with someone else today.")
else:
    print("High risk")
