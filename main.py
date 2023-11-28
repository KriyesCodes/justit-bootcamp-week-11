import CRUD as db, reports

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

def addFilmMenu():
  subMenuOptions = {
    0: "Exit",
    1: "Add a film"
  }
  print("Adding a film record")
  
  while True:
    choice = getMenuInput(subMenuOptions)
    match choice:
      case 0:
        print("Returning to main menu...\n")
        break
      case _:
        try:
          filmTitle = str(input("Enter film title: "))
          filmReleaseYear = int(input("Enter the year this film released: "))
          filmRating = str(input("Enter age rating for this film, for example PG: "))
          filmDuration = int(input("Enter the film duration in minutes: "))
          filmGenre = str(input("Enter the main genre of this film: "))

          db.addFilm(filmTitle, filmReleaseYear, filmRating, filmDuration, filmGenre)
          print(f"\n{filmTitle} has been added to the database")
        except Exception as e:
          print("\nInput is not in correct format, please try again")
          print(e)


def deleteFilmMenu():
  subMenuOptions = {
    0: "Exit",
    1: "Delete a film"
  }
  print("Deleting a film record")

  while True:
    choice = getMenuInput(subMenuOptions)
    match choice:
      case 0:
        print("Returning to main menu...\n")
        break
      case _:
        try:
          filmId = int(input("Enter the ID of the film to delete: "))

          db.deleteFilm(filmId)
          print(f"\nFilm with ID {filmId} has been deleted from the database")
        except Exception as e:
          print("\nInput is not in correct format, please try again")
          print(e)


def mainProgram():
  mainMenuOptions = {
  1: "Add a film",
  2: "Delete a film",
  3: "Update a film",
  4: "View films",
  5: "View film reports",
  6: "Exit"
  }
  
  programRunning = True

  while programRunning:
    print("Welcome to FilmFlix!")
    choice = getMenuInput(mainMenuOptions)
    programRunning = False


if __name__ == "__main__":
  deleteFilmMenu()