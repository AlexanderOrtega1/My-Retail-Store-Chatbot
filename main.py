import os
import time

# # # variables/lists # # #
storeinv = [2]
used_PIDs = [1]
user_acc = [{'alex1': '1234'}, {'alex2': '5678'}]
emp_acc = [{'Alex': '1234'}, {'Jack': '4321'}]
list_index = 0


admin_code = "admin" # change this later#
textSeperator = '==================================================================='

# # # functions # # #
def timeClear(t):
  time.sleep(t)
  os.system("clear")


# # # M A I N # # #
# login stuffs #
print(textSeperator)
print('Hello, User!! Welcome to The Retail Store chatbot!!')
print()
print('Are you new or are you returning?')
returning = input('1. New\n2. Returning\n> ').lower()
print(textSeperator)
os.system('clear')

if returning == '1' or returning == 'new':
  while True:
    print(textSeperator)
    print('Please create a username and password to continue.')
    print()
    username = input('Username: ')
    password = input('Password: ')
    print(textSeperator)
    for i in user_acc:
      if i in user_acc:
        print('This username alreay exists. Please try again.')
        timeClear(2)
        continue
      else:
        while True:
          print('Please confirm your username and password.')
          print()
          username_confirm = input('Username: ')
          password_confirm = input('Password: ')
          print(textSeperator)
          if username_confirm == username and password_confirm == password:
            os.system('clear')
            print(textSeperator)
            print(f'Welcome to the Retail Store chatbot, {username}!')
            user_acc.append(f'{username}: {password}')
            print(textSeperator)
            print(user_acc)
            break
          else:
            print('Your username or password is incorrect. Please try again.')
            print(textSeperator)
            continue
      
#elif returning == '2' or returning == 'returning':