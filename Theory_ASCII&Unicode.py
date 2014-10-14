#Tony K.
#Theory ASCII & Unicode Task 1
#30/09/2014

print("This programm converts between Text and ASCII")

user_input = input("Do you want to convert ASCII or Text: ")

if user_input == ASCII:
    user_input_ascii = input("Please enter the ascii number you want to transfer: ")    

elif user_input == Text:
    user_input_Text = input("Please enter the text you want to conver: ")
    text = ord(user_input_Text)
    print("This is the value converter: {0} ".format(text))

else:
    print("You have entered the wrong text")


