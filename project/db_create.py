# project / db_reate.py

from view import db
from models import Task
from datetime import date

# create the database
db.create_all()

# insert the date
db.session.add(Task("Finish this tutorial", date(2020, 2, 21), 10, 1))
db.session.add(Task("Finish Real Python Course 2", date(2020, 3, 31), 10, 1))

db.session.commit()
