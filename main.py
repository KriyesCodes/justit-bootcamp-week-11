import CRUD, reports

mainMenuOptions = {
  1: "Add a film",
  2: "Delete a film",
  3: "Update a film",
  4: "Show all films",
  5: "View film reports",
  6: "Exit"
}

def getMainMenuText():
  text = "\nMAIN MENU\n"
  for key, value in mainMenuOptions.items():
    text = text + str(key) + ". " + value + "\n"
  return text

def getMainMenuInput():
  while True:
      print(getMainMenuText())
      try:
        choice = int(input("What would you like to do? "))
        if (choice in mainMenuOptions.keys()):
          return choice
        else:
          raise Exception()
      except:
        print("\nIncorrect input, enter the number correlating to your choice")

def RunMainMenu():
  mainMenuRunning = True

  while mainMenuRunning:
    print("Welcome to FilmFlix!")
    choice = getMainMenuInput()
    print(choice)
    mainMenuRunning = False


if __name__ == "__main__":
  RunMainMenu()