import os
import time
import class_file

# # # # # # # variables/lists # # # # # # #
store_inv = []
used_PIDs = []
user_acc = []
emp_acc = []
# # # saving functions # # #
def user_account_file_write():
  f = open('accounts.txt', 'w')
  f.write(str(user_acc))
  f.close()
def employee_account_file_write():
  f = open('accounts.txt', 'w')
  f.write(str(emp_acc))
  f.close()
def used_PIDs_file_write():
  f = open('accounts.txt', 'w')
  f.write(str(used_PIDs))
  f.close()
def store_inv_file_write():
  f = open('accounts.txt', 'w')
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

def create_account(email, password):
  new_account = AccountCreation(email, password)
  if user_acc == []:
    user_acc.append(new_account.create_account())
    user_account_file_write_file_write()
  else:
    if any(account['email'] == email for account in user_acc):
      print("Email already in use")
    else:
      user_acc.append(new_account.create_account())
      user_account_file_write()


# # # # # # # M A I N # # # # # # #
# login stuffs #
print(textSeperator)
print('Hello, User!! Welcome to The Retail Store chatbot!!')
print()
print('Are you new or are you returning?')
returning = input('1. New\n2. Returning\n> ').lower()
print(textSeperator)
os.system('clear')

if returning == '1' or returning == 'new':
  
      
#elif returning == '2' or returning == 'returning':