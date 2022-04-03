from .db import get_db
from random import choice

def post_name(id, name, family_name = None):
  db = get_db()
  cur = db.cursor()
  if family_name != None:
    cur.execute("INSERT INTO names(id, name, family_name) VALUES = (?,?,?)", [id, name, family_name])
  else:
    cur.execute("INSERT INTO names(id, name) VALUES = (?,?)", [id, name])
  db.commit()
  return True

def update_name(id, family_name):
  db = get_db()
  cursor = db.cursor()
  statement = "UPDATE names SET family_name = ? WHERE id = ?"
  cursor.execute(statement, [family_name, id])
  db.commit()
  return True

def get_random_name():
  db = get_db()
  cur = db.cursor()
  cur.execute("SELECT * FROM names")
  return True