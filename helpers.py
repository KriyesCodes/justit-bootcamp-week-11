import CRUD as db

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

# This takes a film record tuple and returns a string with all the data in the tuple in a table row format
def getTableRowFormattedFilmRecord(filmRecord):
  maxStringLength = 15
  colWidth = 20
  if len(filmRecord) != 6:
    raise Exception("Tuple length must be 6")
  else:
    title = str(filmRecord[1])
    year = str(filmRecord[2])
    rating = str(filmRecord[3])
    duration = str(filmRecord[4])
    genre = str(filmRecord[5])

    if len(title) > maxStringLength:
      title = title[0:maxStringLength]+"..."
    if len(year) > maxStringLength:
      year = year[0:maxStringLength]+"..."
    if len(rating) > maxStringLength:
      rating = rating[0:maxStringLength]+"..."
    if len(duration) > maxStringLength:
      duration = duration[0:maxStringLength]+"..."
    if len(genre) > maxStringLength:
      genre = genre[0:maxStringLength]+"..."

  return("|{:^{max}}|{:^{max}}|{:^{max}}|{:^{max}}|{:^{max}}|".format(title, year, rating, duration, genre, max=colWidth))

if __name__ == "__main__":
  print(getTableRowFormattedFilmRecord(db.readFilm(16)[0]))