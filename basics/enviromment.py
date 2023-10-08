# Envirommental variables
# Michi von Ah - October 2023

# Import required modules
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

os.getenv('TEST') # Example output: Hello World!