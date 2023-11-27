import CRUD, reports

def getMainMenuText(mainMenuOptions):
  text = "\nMAIN MENU\n"
  for key, value in mainMenuOptions.items():
    text = text + str(key) + ". " + value + "\n"
  return text

def getMainMenuInput(mainMenuOptions):
  while True:
      print(getMainMenuText(mainMenuOptions))
      try:
        choice = int(input("What would you like to do? "))
        if (choice in mainMenuOptions.keys()):
          return choice
        else:
          raise Exception()
      except:
        print("\nIncorrect input, enter the number correlating to your choice")

def mainProgram():
  mainMenuOptions = {
  1: "Add a film",
  2: "Delete a film",
  3: "Update a film",
  4: "Show all films",
  5: "View film reports",
  6: "Exit"
  }
  
  programRunning = True

  while programRunning:
    print("Welcome to FilmFlix!")
    choice = getMainMenuInput(mainMenuOptions)
    programRunning = False


if __name__ == "__main__":
  mainProgram()