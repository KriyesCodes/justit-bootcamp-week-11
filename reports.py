from connect import *

def getFilmsOfGenre(genre):
  dbCur.execute("SELECT * FROM tblFilms WHERE genre = ?", (genre,))
  return dbCur.fetchall()

def getFilmsOfYear(releaseYear):
  dbCur.execute("SELECT * FROM tblFilms WHERE yearReleased = ?", (releaseYear,))
  return dbCur.fetchall()