from connect import *

def readAll():
  dbCur.execute("SELECT * FROM tblFilms")
  return dbCur.fetchall()

def readFilm(filmId):
  dbCur.execute("SELECT * FROM tblFilms WHERE filmID = ?", (filmId))
  return dbCur.fetchall()

def addFilm(filmTitle, filmReleaseYear, filmRating, filmDuration, filmGenre):
  dbCur.execute("INSERT INTO tblFilms(title, yearReleased, rating, duration, genre) VALUES (?, ?, ? ,? ,?)",
              (filmTitle, filmReleaseYear, filmRating, filmDuration, filmGenre))
  dbCon.commit()

def updateFilm(filmId, fieldName, fieldValue):
  fieldName = fieldName.lower()
  if (fieldName == 'title'):
    query = "UPDATE tblFilms SET title = ? WHERE filmID = ?"
  elif (fieldName == 'yearreleased'):
    query = "UPDATE tblFilms SET yearReleased = ? WHERE filmID = ?"
  elif (fieldName == 'rating'):
    query = "UPDATE tblFilms SET rating = ? WHERE filmID = ?"
  elif (fieldName == 'duration'):
    query = "UPDATE tblFilms SET duration = ? WHERE filmID = ?"
  elif (fieldName == 'genre'):
    query = "UPDATE tblFilms SET genre = ? WHERE filmID = ?"
  else:
    raise Exception("Field name given does not match any in the database table")
  
  dbCur.execute(query, (fieldValue, filmId))
  dbCon.commit()

def deleteFilm(filmId):
  dbCur.execute("DELETE FROM tblFilms WHERE filmID=?", (filmId,))
  dbCon.commit()


if __name__ == "__main__":
  print("CRUD.py run directly")