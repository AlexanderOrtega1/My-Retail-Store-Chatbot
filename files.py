import main as ma

try:
  f = open("accounts.txt", "r")
  ma.user_acc = eval(f.read())
  f.close()
except:
  ma.user_acc = []