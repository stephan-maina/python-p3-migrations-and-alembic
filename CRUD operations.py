from models import Session, User

# Create a new user
session = Session()
new_user = User(name='John Doe', email='john@example.com')
session.add(new_user)
session.commit()

# Read a user
user = session.query(User).filter_by(name='John Doe').first()
print(f'User: {user.name}, Email: {user.email}')

# Update a user
user.name = 'Jane Doe'
session.commit()

# Delete a user
session.delete(user)
session.commit()

session.close()
