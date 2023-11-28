import CRUD as db

def getHorizontalTableLine(numberOfColumns, colWidth):
  formattedString = " ";

  for i in range(colWidth * numberOfColumns + numberOfColumns - 1):
    formattedString += "-"
  formattedString += "\n"
  return formattedString

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

  formattedString = ""
  formattedString += getHorizontalTableLine(len(filmHeadings)-1, colWidth)
  formattedString += "|{:^{max}}|{:^{max}}|{:^{max}}|{:^{max}}|{:^{max}}|\n".format(title, year, rating, duration, genre, max=colWidth)
  formattedString += getHorizontalTableLine(len(filmHeadings)-1, colWidth)

  return formattedString
# Takes a film record tuple and a max string length and column width to format it to
#  returns a string formatted to look like a table row
def getTableRowFormattedFilmRecord(filmRecord, maxStringLength, colWidth):
  if len(filmRecord) != 6:
    raise Exception("Tuple length must be 6")
  else:
    title, year, rating, duration, genre = formatColumnValues(filmRecord[1], filmRecord[2], filmRecord[3], filmRecord[4], filmRecord[5], maxStringLength)

  return("|{:^{max}}|{:^{max}}|{:^{max}}|{:^{max}}|{:^{max}}|".format(title, year, rating, duration, genre, max=colWidth))

def getTableFormatted(filmRecordList, columnWidth):
  maxStringLength = columnWidth - 7
  filmHeadings = ("Film ID", "Title", "Year Released", "Rating", "Duration", "Genre")
  formattedString = getTableHeadingFormatted(filmHeadings, maxStringLength, columnWidth)
  
  for i in range(len(filmRecordList)):
    formattedString += getTableRowFormattedFilmRecord(filmRecordList[i], maxStringLength, columnWidth)
    formattedString += "\n"
  formattedString += getHorizontalTableLine(len(filmHeadings)-1, columnWidth)

  return formattedString
if __name__ == "__main__":
  print(getTableFormatted(db.readAll(), 12))