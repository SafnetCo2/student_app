from app import app, db, Profile

with app.app_context():
    # Create the database and the database table
    db.create_all()

    # Insert sample data
    if not Profile.query.first():  # Check if the table is empty
        sample_profile = Profile(first_name='Josephine', last_name='Ivi', age=30)
        db.session.add(sample_profile)
        db.session.commit()

    print("Database tables created and sample data inserted!")
