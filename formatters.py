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
def getFormattedTableHeader(headerRowData, maxStringLength, colWidth):
  truncatedRowData = truncateRowValues(headerRowData, maxStringLength)

  formattedString = ""
  formattedString += getHorizontalTableLine(len(truncatedRowData), colWidth)

  for i in range(len(truncatedRowData)):
    formattedString += "|{:^{max}}".format(truncatedRowData[i], max=colWidth)
  formattedString += "|\n"

  formattedString += getHorizontalTableLine(len(truncatedRowData), colWidth)

  return formattedString

# Takes a tuple containing row values of the table, and a max string length and column width to format it to
#  returns a string formatted to look like a table row
def getFormattedTableRow(rowData, maxStringLength, colWidth):
  truncatedRowData = truncateRowValues(rowData, maxStringLength)

  formattedString = ""

  for i in range(len(truncatedRowData)):
    formattedString += "|{:^{max}}".format(truncatedRowData[i], max=colWidth)
  formattedString += "|"

  return formattedString

# def getTableFormatted(filmRecordList, columnWidth):
#   maxStringLength = columnWidth - 7
#   filmHeadings = ("Film ID", "Title", "Year Released", "Rating", "Duration", "Genre")
#   formattedString = getTableHeadingFormatted(filmHeadings, maxStringLength, columnWidth)
  
#   for i in range(len(filmRecordList)):
#     formattedString += getTableRowFormattedFilmRecord(filmRecordList[i], maxStringLength, columnWidth)
#     formattedString += "\n"
#   formattedString += getHorizontalTableLine(len(filmHeadings)-1, columnWidth)

#   return formattedString

if __name__ == "__main__":
  print(getFormattedTableRow(("FirstName", "LastName", "Long Credit Card Number"), 10, 20))