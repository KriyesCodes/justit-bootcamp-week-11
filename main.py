import CRUD as db, reports, helpers, formatters

def addFilmMenu():
  subMenuOptions = {
    0: "Exit",
    1: "Add a film"
  }
  menuTitle = "ADDING A FILM RECORD"
  
  while True:
    choice = helpers.getMenuInput(subMenuOptions, menuTitle)
    if choice == 0:
      print("\nReturning to main menu...")
      return
    else:
      match choice:
        case 1:
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
        case _:
          print("Something went wrong with the choice selection")

def deleteFilmMenu():
  subMenuOptions = {
    0: "Exit",
    1: "Delete a film"
  }
  menuTitle = "DELETING A FILM RECORD"

  while True:
    choice = helpers.getMenuInput(subMenuOptions, menuTitle)
    if choice == 0:
      print("\nReturning to main menu...")
      return
    else:
      match choice:
        case 1:
          try:
            filmId = int(input("Enter the ID of the film to delete: "))

            db.deleteFilm(filmId)
            print(f"\nFilm with ID {filmId} has been deleted from the database")
          except Exception as e:
            print("\nInput is not in correct format, please try again")
            print(e)
        case _:
          print("Something went wrong with the choice selection")

def updateFilmMenu():
  subMenuOptions = {
    0: "Exit",
    1: "Update a film's title",
    2: "Update a film's release year",
    3: "Update a film's age rating",
    4: "Update a film's duration",
    5: "Update a film's genre"
  }
  filmFields = {
    1: "Title",
    2: "YearReleased",
    3: "Rating",
    4: "Duration",
    5: "Genre"
  }
  menuTitle = "UPDATING A FILM RECORD"

  while True:
    choice = helpers.getMenuInput(subMenuOptions, menuTitle)
    if choice == 0:
      print("\nReturning to main menu...")
      return
    else:
      try:
        filmId = int(input("Enter the ID of the film to update: "))
        match choice:
          case 1:
            newFieldValue = str(input("Enter the updated title: "))
          case 2:
            newFieldValue = int(input("Enter the updated yelease year: "))
          case 3:
            newFieldValue = str(input("Enter the updated age rating: "))
          case 4:
            newFieldValue = int(input("Enter the updated duration in minutes: "))
          case 5:
            newFieldValue = str(input("Enter the updated genre: "))
          case _:
            print("Something went wrong with the choice selection")
            raise Exception()
          
        db.updateFilm(filmId, filmFields[choice], newFieldValue)
        print(f"\nThe {filmFields[choice].lower()} of the film with ID {filmId} has been updated to {newFieldValue}")
      except Exception as e:
        print("\nInput is not in correct format, please try again")
        print(e)

def viewFilmsMenu():
  subMenuOptions = {
    0: "Exit",
    1: "View all films"
  }
  menuTitle = "VIEWING FILMS"
  
  while True:
    choice = helpers.getMenuInput(subMenuOptions, menuTitle)
    if choice == 0:
      print("\nReturning to main menu...")
      return
    else:
      match choice:
        case 1:
          print(formatters.getTableFormatted(db.readAll(), 20))
        case _:
          print("Something went wrong with the choice selection")

def mainProgram():
  mainMenuOptions = {
    0: "Exit",
    1: "Add a film",
    2: "Delete a film",
    3: "Update a film",
    4: "View films",
    5: "View film reports"
  }
  print("\nWelcome to FilmFlix!")
  menuTitle = "MAIN MENU"

  while True:  
    choice = helpers.getMenuInput(mainMenuOptions, menuTitle)

    match choice:
      case 0:
        print("\nThank you for using FilmFlix! Come again soon!\n")
        return
      case 1:
        addFilmMenu()
      case 2:
        deleteFilmMenu()
      case 3:
        updateFilmMenu()
      case 4:
        viewFilmsMenu()
      case _:
        print("Something has gone wrong during main menu choice selection")

if __name__ == "__main__":
  mainProgram()
  exit()