# Anki Deck Creator

A tool to generate Anki decks for efficient studying using AI-generated question-answer pairs.

## Overview

This project helps create Anki decks from text files containing question-answer pairs. It's designed to streamline the process of converting AI-generated content into study materials.

## Input Format

The input text files should be formatted as follows:

question|answer
question|answer
question|answer

## Usage

1. Prepare your input text file with question-answer pairs.
2. Run the script to process the file and generate an Anki deck.
3. Import the generated deck into Anki for studying.

## Requirements

- Python 3.x
- Anki desktop application

## Installation

1. Ensure you have Python 3.10 or later installed on your system.

2. Install Poetry if you haven't already. Follow the instructions at https://python-poetry.org/docs/#installation

3. Clone this repository:
   ```
   git clone https://github.com/yourusername/anki-creator.git
   cd anki-creator
   ```

4. Install the project dependencies using Poetry and the provided Makefile:
   ```
   make install
   ```

This will set up the project with all necessary dependencies using Poetry and Python 3.10+.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT

