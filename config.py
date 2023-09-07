import os
from dotenv import load_dotenv


load_dotenv()



DISCORD_APPLICATION_ID = os.getenv("DISCORD_APPLICATION_ID")
DISCORD_PUBLIC_KEY = os.getenv("DISCORD_PUBLIC_KEY")


