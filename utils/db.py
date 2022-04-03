import sqlite3
DATABASE_DIRECTORY = "databases/names.sqlite"

def get_db():
  conn = sqlite3.connect(DATABASE_DIRECTORY)
  return conn