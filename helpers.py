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

def formatColumnValues(title, year, rating, duration, genre, maxStringLength):
  title = str(title)
  year = str(year)
  rating = str(rating)
  duration = str(duration)
  genre = str(genre)

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

  return (title, year, rating, duration, genre)

# Takes a tuple containing the field names of the table, and a max string length and column width to format it to
# returns a string formatted to look like a table heading
def getTableHeadingFormatted(filmHeadings, maxStringLength, colWidth):
  if len(filmHeadings) != 6:
    raise Exception("Tuple length must be 6")
  else:
    title, year, rating, duration, genre = formatColumnValues(filmHeadings[1], filmHeadings[2], filmHeadings[3], filmHeadings[4], filmHeadings[5], maxStringLength)

  formattedString = "";

  for i in range(colWidth * len(filmHeadings)-1):
    formattedString += "_"
  formattedString += "\n"
  formattedString += "|{:^{max}}|{:^{max}}|{:^{max}}|{:^{max}}|{:^{max}}|".format(title, year, rating, duration, genre, max=colWidth)

  return formattedString
# Takes a film record tuple and a max string length and column width to format it to
#  returns a string formatted to look like a table row
def getTableRowFormattedFilmRecord(filmRecord, maxStringLength, colWidth):
  if len(filmRecord) != 6:
    raise Exception("Tuple length must be 6")
  else:
    title, year, rating, duration, genre = formatColumnValues(filmRecord[1], filmRecord[2], filmRecord[3], filmRecord[4], filmRecord[5], maxStringLength)

  return("|{:^{max}}|{:^{max}}|{:^{max}}|{:^{max}}|{:^{max}}|".format(title, year, rating, duration, genre, max=colWidth))

if __name__ == "__main__":
  print(getTableRowFormattedFilmRecord(db.readFilm(16)[0]), 15, 20)