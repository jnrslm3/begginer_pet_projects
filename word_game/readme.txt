Word Guess Game with Web Scraped Word Bank
This is a Python-based word guessing game where players try to guess a randomly chosen word within a limited number of attempts. The game provides feedback on correct, misplaced, and incorrect letters, similar to Wordle.

Features:
Dynamic Word List: Words are scraped from a website containing the 1000 most common English words.
Intelligent Feedback: Identifies correctly placed letters, misplaced letters, and incorrect guesses.
Limited Attempts: Players have five chances to guess the correct word.
Replay Option: The game allows players to restart after each round.
How It Works:
The scrap.py script scrapes words from a website and stores them in words.txt.
The main.py script reads these words and selects one randomly for the guessing game.
Players enter a word of the same length, and the game provides hints about the word structure.
This project combines Python programming, web scraping (BeautifulSoup), and game logic in an interactive experience. 🚀