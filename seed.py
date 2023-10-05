from app import db, app
from models import Pet

ctx = app.app_context()
ctx.push()

db.drop_all()
db.create_all()