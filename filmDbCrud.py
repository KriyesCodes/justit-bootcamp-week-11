from connect import *

def readAll():
  dbCur.execute("SELECT * FROM tblFilms")
  return dbCur.fetchall()