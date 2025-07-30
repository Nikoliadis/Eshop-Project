from app import create_app, db
from app import models  # This ensures all tables are recognized

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ Database tables created.")
