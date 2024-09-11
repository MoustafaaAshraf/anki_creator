import genanki
import random
import sys
import os



# Function to read questions and answers from a file
def read_qa_from_file(filename):
    qa_pairs = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # Assuming questions and answers are separated by '|'
            question, answer = line.strip().split('|')
            qa_pairs.append((question, answer))
    return qa_pairs

def main(input_file):

    # Create a model (card type)
    my_model = genanki.Model(
        1607392319,
        'Simple Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ]
    )

    # Create a deck
    my_deck = genanki.Deck(
        2059400110,
        f'{input_file}'
    )

    # Read questions and answers from file
    input_path = os.path.join('input', input_file)
    qa_pairs = read_qa_from_file(input_path)

    # Create notes (cards) from file data
    for question, answer in qa_pairs:
        note = genanki.Note(
            model=my_model,
            fields=[question, answer])
        my_deck.add_note(note)

    # Create an APKG file
    output_filename = os.path.splitext(input_file)[0] + '.apkg'
    output_path = os.path.join('output', output_filename)
    genanki.Package(my_deck).write_to_file(output_path)

    print(f"Anki deck '{output_filename}' has been created successfully!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python -m src.main <input_filename>")
        sys.exit(1)
    
    main(sys.argv[1])