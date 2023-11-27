from connect import *

def getFilmsOfGenre(genre):
  dbCur.execute("SELECT * FROM tblFilms WHERE genre = ?", (genre,))
  return dbCur.fetchall()