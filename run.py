import app
from app import myapp_obj
from app.models import db

app.myapp_obj.run(debug=True)

with myapp_obj.app_context():
    db.create_all()

