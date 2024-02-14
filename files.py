import main as ma

try:
  f = open("accounts.txt", "r")
  ma.storeinv = eval(f.read())
  f.close()
except:
  ma.storeinv = []
  
try:
  f = open("accounts.txt", "r")
  ma.used_PIDs = eval(f.read())
  f.close()
except:
  ma.used_PIDs = []

try:
  f = open("accounts.txt", "r")
  ma.user_acc = eval(f.read())
  f.close()
except:
  ma.user_acc = []

try:
  f = open("accounts.txt", "r")
  ma.emp_acc = eval(f.read())
  f.close()
except:
  ma.emp_acc = []