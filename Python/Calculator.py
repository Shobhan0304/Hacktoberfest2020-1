#Menu Driven calculator on Python
while(True):
  x = int(input("Enter first number: "))
  y = int(input("Enter second number: "))
  print("Operators: + , - , * , /")
  print("Enter 0 to exit")
  z = input("Enter operator: ")
  
  if (z=='+'):
    print("Output = ",x+y)
  elif (z=='-'):
    print("Output = ",x-y)
  elif (z=='*'):
    print("Output = ",x*y)
  elif (z=='/'):
    print("Output = ",x/y)
  elif (z == '0'):
    print("End of program")
    break;
  else:
    print("Enter valid input")
