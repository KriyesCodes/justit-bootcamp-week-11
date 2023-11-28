def getMenuText(menuOptions):
  text = "\nMENU\n"
  for key, value in menuOptions.items():
    text = text + str(key) + ". " + value + "\n"
  return text

def getMenuInput(menuOptions):
  while True:
      print(getMenuText(menuOptions))
      try:
        choice = int(input("What would you like to do? "))
        if (choice in menuOptions.keys()):
          return choice
        else:
          raise Exception()
      except:
        print("\nIncorrect input, enter the number correlating to your choice")