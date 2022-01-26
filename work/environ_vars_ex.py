import os
from dotenv import load_dotenv

load_dotenv()
is_admin = bool(os.environ.get('ADMIN'))
print(is_admin, type(is_admin))