# config.py - Configuration settings for the application, such as API keys, network settings

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")  # Example API key
