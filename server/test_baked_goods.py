from app import app, most_expensive_baked_good

with app.app_context():
    most_expensive_baked_good()