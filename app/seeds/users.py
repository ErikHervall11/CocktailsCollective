from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password',
        first_name='Demo', last_name='User',
        profile_image='https://cocktail-collective.s3.us-west-1.amazonaws.com/bartender.jpg'
    )
    marnie = User(
        username='marnie', email='marnie@aa.io', password='password',
        first_name='Marnie', last_name='Smith',
        profile_image='https://cocktail-collective.s3.us-west-1.amazonaws.com/bartender.jpg'
    )
    bobbie = User(
        username='bobbie', email='bobbie@aa.io', password='password',
        first_name='Bobbie', last_name='Brown',
        profile_image='https://cocktail-collective.s3.us-west-1.amazonaws.com/bartender.jpg'
    )
    john = User(
        username='john', email='john@aa.io', password='password',
        first_name='John', last_name='Doe',
        profile_image='https://cocktail-collective.s3.us-west-1.amazonaws.com/bartender.jpg'
    )
    jane = User(
        username='jane', email='jane@aa.io', password='password',
        first_name='Jane', last_name='Doe',
        profile_image='https://cocktail-collective.s3.us-west-1.amazonaws.com/bartender.jpg'
    )
    alice = User(
        username='alice', email='alice@aa.io', password='password',
        first_name='Alice', last_name='Wonderland',
        profile_image='https://cocktail-collective.s3.us-west-1.amazonaws.com/bartender.jpg'
    )
    bob = User(
        username='bob', email='bob@aa.io', password='password',
        first_name='Bob', last_name='Builder',
        profile_image='https://cocktail-collective.s3.us-west-1.amazonaws.com/bartender.jpg'
    )
    charlie = User(
        username='charlie', email='charlie@aa.io', password='password',
        first_name='Charlie', last_name='Brown',
        profile_image='https://cocktail-collective.s3.us-west-1.amazonaws.com/bartender.jpg'
    )
    dave = User(
        username='dave', email='dave@aa.io', password='password',
        first_name='Dave', last_name='Johnson',
        profile_image='https://cocktail-collective.s3.us-west-1.amazonaws.com/bartender.jpg'
    )
    eve = User(
        username='eve', email='eve@aa.io', password='password',
        first_name='Eve', last_name='Smith',
        profile_image='https://cocktail-collective.s3.us-west-1.amazonaws.com/bartender.jpg'
    )

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(john)
    db.session.add(jane)
    db.session.add(alice)
    db.session.add(bob)
    db.session.add(charlie)
    db.session.add(dave)
    db.session.add(eve)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()
