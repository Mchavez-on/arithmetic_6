#   a114_divisible.py

# get two numbers from user
num_1 = int(input("Enter a number!"))
num_2 = int(input("Enter another number!")) 

while (num_1 % num_2 != 0):
  # inform user of result 
  print("The two numbers you selected do not divide to zero, try again!")
  # gather user input again
  num_1 = int(input("Enter a number!"))
  num_2 = int(input("Enter another number!")) 
  # inform user of result 
  print("Congratulations! the numbers", num_1, "and", num_2, "you have selected divide into zero.")
  
  
  


