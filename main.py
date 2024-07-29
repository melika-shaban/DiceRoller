import random

from tkinter import *

window = Tk()

window.title("Dice Roller")

#the function below doesn't take any parameters. It works by first obtaining the type of dice it will be using by checking the integer that is stored in the rad_button_status, which is the same as the number of sides the dice has. Then, it returns a random integer between 1 and the highest valued side of that die (which is just the number of sides), to act as a "random die roll"

def dice_roller():
  dice = rad_button_status.get()
  return random.randint(1, dice)

#the function below doesn't take any parameters. It works by first creating a string containing the words "You rolled". If the show sum button isn't clicked, it will return the string with as many random dice rolls (using the dice_roller function) as specified in the text_box. Otherwise, it'll do the same thing but then also store the values in a list and also return the string with the sum of all the values in the list to show the sum of the numbers. 

def roll_dice_button():
  global another_label #i make it global so that later i can destroy the variable if it already exists (becaue otherwise everytime i clicked roll dice again it would be adding the new label on top of the old one and somemtimes you can see the old one)
  the_string = "You rolled " #original string
  if checkbox_status.get() == False: #checking if checkbox is NOT checked
    for x in range(0, int(a_textbox.get())): #repeating for as many number of dice we will be rolling by checking the contents of the number of dice textbox
      a_var = str(dice_roller()) #using the dice roller function
      the_string += a_var #adding the roll to the string
      if x != int(a_textbox.get()) - 1: #checking if we are at the last random roll 
        the_string += ", " #if not, we add a comma and space for proper formating
  else: #otherwise, the exact same thing happens will minimal exceptions:
    a_list = [] #we create an empty list
    for x in range(0, int(a_textbox.get())):
      a_var = dice_roller()
      a_list.append(a_var)
      the_string += str(a_var) #rather than turning the dice roll value to a string earlier we do so here so that we have no issues when we want to calculate the sum of the values later (because otherwise we would be calculating the sum of strings since we would be appending strings to our list)
      if x != int(a_textbox.get()) - 1: 
        the_string += ", "
    the_string += " = " #adding the equals symbol
    the_string += str(sum(a_list)) #adding the sum of the list items
  try: #if the label does already exist i destroy it
    another_label.destroy()
  except:
    pass
  another_label = Label(window, text = the_string) #creating a label with the string
  another_label.grid(row = 2, column = 2, columnspan = 3)


#below are the three labels, including the number of sides, number of dice and show sum label
label1 = Label(window, text = "Number of sides:")
label1.grid(row = 0, column = 0)

label2 = Label(window, text = "Number of dice:")
label2.grid(row = 1, column = 0)

label3 = Label(window, text = "Show sum")
label3.grid(row = 1, column = 3)

#our rolll dice button is beow

a_button = Button(window, text = "Roll dice", command = roll_dice_button)
a_button.grid(row = 2, column = 0)

#the textbox is below

a_textbox = Entry(window, width = 5)
a_textbox.grid(row = 1, column = 1)

a_textbox.insert(0, 2)

#creating an intvar to store the value of the radio button selected below

#radio buttons are below

rad_button_status = IntVar()

first_rad_button = Radiobutton(window, text = 4, variable = rad_button_status, value = 4)
first_rad_button.grid(row = 0, column = 1)

second_rad_button = Radiobutton(window, text = 6, variable = rad_button_status, value = 6)
second_rad_button.grid(row = 0, column = 2)

second_rad_button.select()

third_rad_button = Radiobutton(window, text = 8, variable = rad_button_status, value = 8)
third_rad_button.grid(row = 0, column = 3)

fourth_rad_button = Radiobutton(window, text = 12, variable = rad_button_status, value = 12)
fourth_rad_button.grid(row = 0, column = 4)

another_rad_button = Radiobutton(window, text = 20, variable = rad_button_status, value = 20)
another_rad_button.grid(row = 0, column = 5)

#creating a boolvar to identify if the box is checked or not (true vs false) below

#checkbutton is also created below

checkbox_status = BooleanVar()

checkbox = Checkbutton(window, variable = checkbox_status, command = lambda: print(checkbox_status.get()))
checkbox.grid(row = 1, column = 4)





mainloop()
