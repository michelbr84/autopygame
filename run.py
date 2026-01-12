# run.py
# Entry point script to run the Tetris-Style Game.
# It adds the src directory to sys.path and then imports and runs src.main.main()

import sys
import os

# Add the src directory (this file's parent directory) to the start of sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import the main function from src.main
from src.main import main

if __name__ == "__main__":
    main()