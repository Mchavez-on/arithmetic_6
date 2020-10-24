#   a114_divisible.py

# get two numbers from user
num_1 = int(input("Enter a number!"))
num_2 = int(input("Enter another number!")) 
def get_user_numbers():
  num_1 = int(input("Enter a number!"))
  num_2 = int(input("Enter another number!"))

# loop whle the numbers are not divisible (the remainder is 0)
rem = num_1 % num_2
def divide_user_numbers():
  rem = num_1 % num_2 


while (rem != 0):
  # inform user of result 
  print("The two numbers you selected do not divide to zero, try again!")
  get_user_numbers()
  divide_user_numbers()
  if (rem == 0):
    break
print("Congratulations! the numbers you have selected divide into zero.")
  
  
  
  # gather user input again
  
# inform user of result 
