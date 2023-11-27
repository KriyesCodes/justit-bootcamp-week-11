from connect import *

def readAll():
  dbCur.execute("SELECT * FROM tblFilms")
  return dbCur.fetchall()

def addFilm(filmTitle, filmReleaseYear, filmRating, filmDuration, filmGenre):
  dbCur.execute("INSERT INTO tblFilms(title, yearReleased, rating, duration, genre) VALUES (?, ?, ? ,? ,?)",
              (filmTitle, filmReleaseYear, filmRating, filmDuration, filmGenre))
  dbCon.commit()