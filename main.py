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
  text = "\n"
  for key, value in mainMenuOptions.items():
    text = text + str(key) + ". " + value + "\n"
  return text

