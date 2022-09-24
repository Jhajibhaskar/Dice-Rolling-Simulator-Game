import random
while True:
  print('Click  1.To Roll    2.To Exit ')
  input_user= int(input("What you want to do\n"))
  if input_user==1:
    number = random.randint(1,6)
    print("Dice Generated : ",number)
  else:
    break
