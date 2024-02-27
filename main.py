import os
import time
from class_file import AccountCreation

# # # # # # # variables/lists # # # # # # #
store_inv = []
used_PIDs = []
user_acc = []
emp_acc = []
scheduleList = ['Monday: 10am - 9pm',
  'Tuesday: 10am - 9pm',
  'Wednesday: 10am - 9pm',
  'Thursday: 10am - 9pm',
  'Friday: 9am - 11pm',
  'Saturday: 8am - 11pm',
  'Sunday: 8am - 11pm']

# # # saving functions # # #
def user_account_file_write():
  f = open('user.acc', 'w')
  f.write(str(user_acc))
  f.close()
def employee_account_file_write():
  f = open('emp.acc', 'w')
  f.write(str(emp_acc))
  f.close()
def used_PIDs_file_write():
  f = open('used.PIDs', 'w')
  f.write(str(used_PIDs))
  f.close()
def store_inv_file_write():
  f = open('store.inv', 'w')
  f.write(str(store_inv))
  f.close()
try:
  f = open("store.inv", "r")
  store_inv = eval(f.read())
  f.close()
except:
  store_inv = []
  store_inv_file_write()
try:
  f = open("used.PIDs", "r")
  used_PIDs = eval(f.read())
  f.close()
except:
  used_PIDs = []
  used_PIDs_file_write()
try:
  f = open("user.acc", "r")
  user_acc = eval(f.read())
  f.close()
except:
  user_acc = []
  user_account_file_write()
try:
  f = open("emp.acc", "r")
  emp_acc = eval(f.read())
  f.close()
except:
  emp_acc = []
  employee_account_file_write()
# # # # # # # # # # # # # # # #
  
list_index = 0

admin_code = "admin" # change this later#
textSeperator = '==================================================================='
# # #
# # # # # # # functions # # # # # # #
def timeClear(t):
  time.sleep(t)
  os.system("clear")
def textSep():
  print(textSeperator)

def create_account(email, password):
  new_account = AccountCreation(email, password)
  if user_acc == []:
    user_acc.append(new_account.create_account())
    user_account_file_write()
  else:
    if any(account['email'] == email for account in user_acc):
      print("Email already in use")
      print(textSeperator)
      return True
    else:
      user_acc.append(new_account.create_account())
      user_account_file_write()
      return False

def returning_acc(email, password):
  if any(acc['email'] == email for acc in user_acc):
    for account in user_acc:
      if account['email'] == email:
        if account['password'] == password:
          print('Successfully logged in!')
          textSep()
          return False
        else:
          password_tries = True
          while password_tries is True:
            print('Incorrect password\n')
            timeClear(1)
            textSep()
            print(f'Email: {email}')
            password = input('Password: ')
            if account['password'] == password:
              print('Successfully logged in!')
              textSep()
              password_tries = False
              return False
            else:
              continue
          break
      else:
        continue
  else:
    print('Account not found')
    textSep()
    return True

def nextText():
  nextText = input('Press enter to continue: ')

def printMenu():
  print(textSeperator)
  print('Choose one of the following options:')
  print('''  1. Operating Hours
  2. PlaceHolder 2
  3. PlaceHolder 3
  4. Exit''')
  print(textSeperator)

def workingHours():
  timeClear(0.5)
  print(textSeperator)
  print('Here is our operating hours:')
  print(textSeperator)
  print()
  for i in scheduleList:
    print(i)
    print()
  print(textSeperator)
  nextText()

# # # # # # # M A I N # # # # # # #
# login stuffs #
textSep()
print('Hello, User!! Welcome to The Retail Store chatbot!!')
print()
print('Are you new or are you returning?')
returning = input('1. New\n2. Returning\n> ').lower()
os.system('clear')
print(textSeperator)

if returning == '1' or returning == 'new':
  creating_acc = True
  while creating_acc is True:
    os.system('clear')
    print(textSeperator)
    print('Welcome new user!!\n')
    print('Please enter your email and password to create an account!\n')
    new_acc_email = input('Email: ')
    new_acc_password = input('Password: ')
    new_acc = create_account(new_acc_email, new_acc_password)
    if new_acc is False:
      print('Account created successfully!')
      print(textSeperator)
      creating_acc = False
    elif new_acc is True:
      time.sleep(2)
      continue

elif returning == '2' or returning == 'returning':
  logging_in = True
  while logging_in is True:
    timeClear(2)
    textSep()
    returning_email = input('Email: ')
    returning_password = input('Password: ')
    logging_in = returning_acc(returning_email, returning_password)

# # # # # # Menu # # # # # #
using = True
while using == True:
  printMenu()
  menuChoice = input('What would you like to do?: ')
  print(textSeperator)
  if menuChoice == '1':
    workingHours()
    timeClear(1)
  elif menuChoice == '2':
    print('PlaceHolder 2')
    timeClear(1)
  elif menuChoice == '3':
    print('PlaceHolder 3')
    timeClear(1)
  elif menuChoice == '4':
    print('Exiting...')
    using = False