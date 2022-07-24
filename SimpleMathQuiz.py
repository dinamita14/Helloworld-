name = input("Hello user! Please enter your name: ")
print(name+", would you like to play a math quiz?")
choose = input("Yes or No?: ")
if choose == "Yes":
   q1 = input("4+4=")
   if q1 == "8":
      print("That is correct!")
   else:
      print("That is incorrect")
   q2 = input("5-10=")
   if q2 == "-5":
      print("Good job!")
   else:
      print("That is incorrect")
   q3 = input("5*2=")
   if q3 == "10":
      print("Fantastic!")
      print("That's all of the questions! Thank you for playing!")
   else:
      print("That is incorrect")
      print("That's all of the questions! Thank you for playing!")
elif choose == "No":
      print("Thank you see you again!")
else:
      print("Invalid entry")



