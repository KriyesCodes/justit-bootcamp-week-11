import CRUD as db, reports, helpers

def addFilmMenu():
  subMenuOptions = {
    0: "Exit",
    1: "Add a film"
  }
  print("Adding a film record")
  
  while True:
    choice = helpers.getMenuInput(subMenuOptions)
    match choice:
      case 0:
        print("Returning to main menu...\n")
        return
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
    choice = helpers.getMenuInput(subMenuOptions)
    match choice:
      case 0:
        print("Returning to main menu...\n")
        return
      case _:
        try:
          filmId = int(input("Enter the ID of the film to delete: "))

          db.deleteFilm(filmId)
          print(f"\nFilm with ID {filmId} has been deleted from the database")
        except Exception as e:
          print("\nInput is not in correct format, please try again")
          print(e)

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
  print("Updating a film record")

  while True:
    choice = helpers.getMenuInput(subMenuOptions)
    if choice == 0:
      print("Returning to main menu...\n")
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
            print("Something went wrong with the menu choice selection")
            raise Exception()
          
        db.updateFilm(filmId, filmFields[choice], newFieldValue)
        print(f"\nThe {filmFields[choice].lower()} of the film with ID {filmId} has been updated to {newFieldValue}")
      except Exception as e:
        print("\nInput is not in correct format, please try again")
        print(e)

def mainProgram():
  mainMenuOptions = {
    0: "Exit",
    1: "Add a film",
    2: "Delete a film",
    3: "Update a film",
    4: "View films",
    5: "View film reports"
  }

  while True:
    print("Welcome to FilmFlix!")
    choice = helpers.getMenuInput(mainMenuOptions)

    match choice:
      case 0:
        print("Thank you for using FilmFlix! Come again soon!")
        return
      case 1:
        addFilmMenu()
      case 2:
        deleteFilmMenu()
      case 3:
        continue
      case 4:
        continue
      case 5:
        continue
      case _:
        print("Something has gone wrong during main menu choice selection")

if __name__ == "__main__":
  mainProgram()
  exit()