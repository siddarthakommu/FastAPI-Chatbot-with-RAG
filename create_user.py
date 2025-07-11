from app.models.database import init_db, SessionLocal
from app.models.user import User
from app.utils.hashing import hash_password
import getpass


init_db()
db = SessionLocal()

username = input("Enter new username: ")
password = getpass.getpass("Enter password: ")

existing_user = db.query(User).filter(User.username == username).first()
if existing_user:
    print(f"❌ User '{username}' already exists.")
else:
    new_user = User(username=username, hashed_password=hash_password(password))
    db.add(new_user)
    db.commit()
    print(f"✅ User '{username}' created successfully!")

db.close()
