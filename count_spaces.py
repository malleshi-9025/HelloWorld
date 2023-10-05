# function to return the count of no of spaces in a string

# by accepting the input string as an argument
def countSpaces(inputString):
   
   # storing the count of the number of spaces in a given string
   spaces_count = 0

   # Traversing till the length of the string
   for index in range(0, len(inputString)):
   
      # checking whether each character of a string is blank/space or not
      if inputString[index] == " ":

         # incrementing the space value count by 1
         spaces_count += 1

   # returning the count of the number of spaces in an input string
   return spaces_count

# input string
inputString = "tutorialspoint is a best learning platform for coding"

# calling the above defined countSpaces() function by

# passing input string as an argument
print("Count of no of spaces in an input string:", countSpaces(inputString))
