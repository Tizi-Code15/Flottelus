#hasspass this scripts used to hash password on md5 
import hashlib, os
from dotenv import load_dotenv

load_dotenv()

initialpass = os.getenv("password")

def hashpass(initialpass):

    return hashlib.md5(initialpass.encode()).hexdigest()


hashedpass = hashpass(initialpass).upper()
