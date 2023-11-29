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

def viewFilmsMenu():
  subMenuOptions = {
    0: "Exit",
    1: "View all information of all films",
    2: "View ID and specific column of all films"
  }
  filmFields = {
    1: "Title",
    2: "Year",
    3: "Rating",
    4: "Duration",
    5: "Genre"
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
          headerData = ("Film ID", filmFields[1], filmFields[2], filmFields[3], filmFields[4], filmFields[5])
          columnWidth = 20
          data = db.readAll()
        case 2:
          fieldChoice = helpers.getMenuInput(filmFields, "FIELDS")
          columnWidth = 40

          if fieldChoice in filmFields.keys():
            headerData = ("Film ID", filmFields[fieldChoice])
          else:
            raise Exception("Something went wrong with field choice selection")

          match fieldChoice:
            case 1:
              data = db.readFilmSpecificField("title")
            case 2:
              data = db.readFilmSpecificField("yearReleased")
            case 3:
              data = db.readFilmSpecificField("rating")
            case 4:
              data = db.readFilmSpecificField("duration")
            case 5:
              data = db.readFilmSpecificField("genre")
        case _:
          print("Something went wrong with the choice selection")

      if len(data) < 1:
        print("\nNo films were found")
      else:
        print(formatters.getTableFormatted(headerData, data, columnWidth))

def viewFilmReportsMenu():
  subMenuOptions = {
    0: "Exit",
    1: "View films of a specific genre",
    2: "View films from a specific year",
    3: "View films with a specfic age rating"
  }
  headerData = ("Film ID", "Title", "Year", "Rating", "Duration", "Genre")
  menuTitle = "VIEWING FILM REPORTS"

  while True:
    choice = helpers.getMenuInput(subMenuOptions, menuTitle)
    if choice == 0:
      print("\nReturning to main menu...")
      return
    else:
      try:
        match choice:
          case 1:
            fieldName = str(input("Enter the genre to filter by: "))
            data = reports.getFilmsOfGenre(fieldName)
          case 2:
            fieldName = int(input("Enter the year to filter by: "))
            data = reports.getFilmsOfYear(fieldName)
          case 3:
            fieldName = str(input("Enter the age rating to filter by: "))
            data = reports.getFilmsOfRating(fieldName)
          case _:
            print("Something went wrong with the choice selection")
            raise Exception()
          
        if len(data) < 1:
          print("\nNo films were found, try a different input")
        else:
          print(formatters.getTableFormatted(headerData, data, 20))
      except Exception as e:
        print("\nInput is not in correct format, please try again")

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
      case 5:
        viewFilmReportsMenu()
      case _:
        print("Something has gone wrong during main menu choice selection")

if __name__ == "__main__":
  mainProgram()
  exit()