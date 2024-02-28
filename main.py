import os
import time
import random
from class_file import AccountCreation

# # # # # # # variables/lists # # # # # # #
store_inv = []
used_PIDs = []
user_acc = []
emp_acc = []
store_money = []
scheduleList = ['Monday: 10am - 9pm',
  'Tuesday: 10am - 9pm',
  'Wednesday: 10am - 9pm',
  'Thursday: 10am - 9pm',
  'Friday: 9am - 11pm',
  'Saturday: 8am - 11pm',
  'Sunday: 8am - 11pm']

# # # product creation class # # #
class ProductCreation:
  #constructor method used to instantiate any new class
  def __init__(self, type, price, total):
    newPID = True
    self.product_id = random.randint(1000,5000)  # new attribute added
    while newPID is True:
      self.product_id = random.randint(1000,5000)
      if self.product_id not in used_PIDs:
        used_PIDs.append(self.product_id)
        used_PIDs_file_write()
        newPID = False
    self.type = type
    self.price = price
    self.total = total

  def features(self):
    return {"product_id":self.product_id,
            "type":self.type,
            "price":self.price,
            "total":self.total
            }
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
def store_money_file_write():
  f = open('store.money', 'w')
  f.write(str(store_money))
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
try:
  f = open("store.money", "r")
  store_money = eval(f.read())
  f.close()
except:
  store_money = []
  store_money_file_write()
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
def nextText():
  nextText = input('Press enter to continue: ')

def create_account(email, password):
  new_account = AccountCreation(email, password)
  if user_acc == []:
    user_acc.append(new_account.create_account())
    user_account_file_write()
    return False
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
def create_emp_account(email, password):
  new_account = AccountCreation(email, password)
  if emp_acc == []:
    emp_acc.append(new_account.create_account())
    employee_account_file_write()
    return False
  else:
    if any(account['email'] == email for account in emp_acc):
      print("Email already in use")
      print(textSeperator)
      return True
    else:
      emp_acc.append(new_account.create_account())
      employee_account_file_write()
      return False
def returning_emp_acc(email, password):
  if any(acc['email'] == email for acc in emp_acc):
    for account in emp_acc:
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

def print_customer_Menu():
  textSep()
  print('Choose one of the following options:')
  print('''  1. Operating Hours
  2. Store Inventory
  3. Return an item
  4. Purchase an item
  5. Exit''')
  textSep()
def print_employee_Menu():
  textSep()
  print('Choose one of the following options:')
  print('''  1. Store Inventory
  2. Store Balance
  3. Add a product
  4. Remove a product
  5. Exit''')
  textSep()

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
def display_inventory():
  textSep()
  print("\n **Elite 101 Retail Store Inventory**")
  for product in store_inv:
      textSep()
      for key, value in product.items():            
        print(f"{key}:{value}")          
  textSep()
  nextText()
def returning_product():
  to_return_index = -1
  textSep()
  print('\n**Returning Item**\n')
  textSep()
  try:
    PID = int(input('Enter the Product ID number: '))
  except ValueError:
    PID = 0
  for i, product in enumerate(store_inv):
    if store_inv[i]['product_id'] == PID:
      to_return_index = i
      break
  if to_return_index == -1:
    print('Product ID not found')
  else:
    returned_product = store_inv[to_return_index]
    store_inv.pop(to_return_index)
    returned_product['total'] += 1
    store_inv.append(returned_product)
    store_inv_file_write()

    store_money[0] -= returned_product['price']
    store_money_file_write()
    print('Successfully returned item')
    timeClear(2)
def purchasing_product():
  to_purchase_index = -1
  textSep()
  print('\n**Purchasing Item**\n')
  textSep()
  try:
    PID = int(input('Enter the Product ID number: '))
  except ValueError:
    PID = 0
  for i, product in enumerate(store_inv):
    if store_inv[i]['product_id'] == PID:
      to_purchase_index = i
      break
  if to_purchase_index == -1:
    print('Product ID not found')
  else:
    returned_product = store_inv[to_purchase_index]
    store_inv.pop(to_purchase_index)
    returned_product['total'] -= 1
    store_inv.append(returned_product)
    store_inv_file_write()

    store_money[0] += returned_product['price']
    store_money_file_write()
    print('Successfully purchased item')
    timeClear(2)

def display_store_balance():
  textSep()
  print(f'\nStore Balance: ${store_money[0]}\n')
  textSep()
  nextText()
def add_new_product():    
  print("\n **Adding A New Product To The Inventory**")
  textSep()
  type = input("Enter a type(Shoes, Jacket,...): ").capitalize()
  try:
      price = float(input("Enter a price: "))
  except ValueError:
      price = 0.0
  try:
      total = int(input("Enter a total: "))
  except ValueError:
      total = 0.0

  if price > 0 and total > 0:
      new_product = ProductCreation(type, price, total)      
      store_inv.append(new_product.features())
      display_inventory()
      store_inv_file_write()

  else:
      print(
          "Invalid Price or/and Total. Product not Added to the Inventory ")
def remove_product():  
  to_delete_index = -1
  display_inventory()
  print("\n **Removing A Product From The Inventory**")
  textSep()
  try:
    PID = int(input("Enter Product ID Number to Remove: "))
  except ValueError:
    PID = 0
  for i, product in enumerate(store_inv):           
    if store_inv[i]["product_id"] == PID:
        to_delete_index = i
        break

  if to_delete_index == -1:
    print("This is not in the inventory. Try again.")
  else:       
    store_inv.pop(to_delete_index)
    print("Product was successfully removed from the store inventory.")
    store_inv_file_write()
    used_PIDs.pop(to_delete_index)
    used_PIDs_file_write()
    
# # # # # # # M A I N # # # # # # #
# login stuffs #
textSep()
print('Hello, User!! Welcome to The Retail Store chatbot!!')
print()
print('Are you new or are you returning?')
returning = input('1. New\n2. Returning\n> ').lower()
os.system('clear')
print(textSeperator)
employee = False
if returning == '1' or returning == 'new':
  employee = False
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
      timeClear(1)
    elif new_acc is True:
      time.sleep(2)
      continue
elif returning == '2' or returning == 'returning':
  employee = False
  logging_in = True
  while logging_in is True:
    os.system('clear')
    textSep()
    returning_email = input('Email: ')
    returning_password = input('Password: ')
    logging_in = returning_acc(returning_email, returning_password)
    timeClear(1)
elif returning == admin_code:
  print('Welcome Employee!!\n')
  print('Are you new or returning?')
  returning_employee = input('1. New\n2. Returning\n> ').lower()
  os.system('clear')
  if returning_employee == '1' or returning_employee == 'new':
    employee = True
    creating_acc = True
    while creating_acc is True:
      os.system('clear')
      print(textSeperator)
      print('Welcome new user!!\n')
      print('Please enter your email and password to create an account!\n')
      new_acc_email = input('Email: ')
      new_acc_password = input('Password: ')
      new_acc = create_emp_account(new_acc_email, new_acc_password)
      if new_acc is False:
        print('Account created successfully!')
        print(textSeperator)
        creating_acc = False
        employee = True
        timeClear(1)
      elif new_acc is True:
        time.sleep(2)
        continue
  elif returning_employee == '2' or returning_employee == 'returning':
    employee = True
    logging_in = True
    while logging_in is True:
      os.system('clear')
      textSep()
      returning_email = input('Email: ')
      returning_password = input('Password: ')
      logging_in = returning_emp_acc(returning_email, returning_password)
      timeClear(1)
  
# # # # # # Menu # # # # # #
if employee is False:
  using = True
  while using is True:
    print_customer_Menu()
    menuChoice = input('What would you like to do?: ')
    textSep()
    if menuChoice == '1':
      timeClear(1)
      workingHours()
      timeClear(1)
    elif menuChoice == '2':
      timeClear(1)
      display_inventory()
      timeClear(1)
    elif menuChoice == '3':
      timeClear(1)
      returning_product()
      timeClear(1)
    elif menuChoice == '4':
      timeClear(1)
      purchasing_product()
      timeClear(1)
    elif menuChoice == '5':
      print('Exiting...')
      using = False
    else:
      print('Invalid Option')

elif employee is True:
  using = True
  while using is True:
    print_employee_Menu()
    menuChoice = input('What would you like to do?: ')
    textSep()
    if menuChoice == '1':
      timeClear(1)
      display_inventory()
      timeClear(1)
    elif menuChoice == '2':
      timeClear(1)
      display_store_balance()
      timeClear(1)
    elif menuChoice == '3':
      timeClear(1)
      add_new_product()
      timeClear(1)
    elif menuChoice == '4':
      timeClear(1)
      remove_product()
      timeClear(1)
    elif menuChoice == '5':
      print('Exiting...')
      using = False
    else:
      print('Invalid input')