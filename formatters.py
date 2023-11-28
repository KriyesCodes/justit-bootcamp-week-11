import CRUD as db

def getHorizontalTableLine(numberOfColumns, colWidth):
  formattedString = " ";

  for i in range(colWidth * numberOfColumns + numberOfColumns - 1):
    formattedString += "-"
  formattedString += "\n"
  return formattedString

# Truncates a column value to a max string length appended with "..." and returns it
def truncateColumnValue(columnValue, maxStringLength):
  if maxStringLength <= 3:
    raise Exception("Max string length must be greater than 3 to account for elipses")
  columnValue = str(columnValue)
  if (len(columnValue) > maxStringLength):
    columnValue = columnValue[0:(maxStringLength-3)]+"..."
  return columnValue

# Truncates all row values in a rowData tuple to a max string length appended with "..." and returns the row
def truncateRowValues(rowData, maxStringLength):
  returnList = []

  for i in range(len(rowData)):
    returnList.append(truncateColumnValue(rowData[i], maxStringLength))

  return tuple(returnList)

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
  print(truncateRowValues(("Test", 10000, "This is a very long string for testing", 9999999999999999999), 10))