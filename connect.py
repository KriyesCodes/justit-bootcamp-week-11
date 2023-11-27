import sqlite3 as sql # import sqlite3 module and assigned as alias 'sql'

# use sqlite(sql) module to create and/or connect to a database
dbCon = sql.connect("filmflix.db")


# create a cursor variable and assigned it to the cursor method to execute sql statements
dbCur = dbCon.cursor()