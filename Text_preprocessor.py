import re
import argparse
import unicodedata


def unicodeToAscii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'
        )                               # Normal Form Decomposed                # Nonspacing Mark

def normalizeString(s):
    s = unicodeToAscii(s.lower().strip())
    s = re.sub(r"([.!?])", r" \1", s)
    s = re.sub(r"[^a-zA-Z.!?]+", r" ", s)
    s = re.sub(r"\s+", r" ", s).strip()
    return s


def process_file(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as input_file:
        content = input_file.read()

    sentences = re.split(r'[.!?]', content)  # Split text into sentences

    normalized_sentences = []

    for sentence in sentences:
        normalized_sentence = normalizeString(sentence)
        if normalized_sentence:
            normalized_sentences.append(normalized_sentence)

    with open(output_filename, 'w', encoding='utf-8') as output_file:
        for normalized_sentence in normalized_sentences:
            output_file.write(normalized_sentence + '\n')

def main():
    parser = argparse.ArgumentParser(description="Preprocess a text file and save normalized sentences.")
    parser.add_argument("-input", dest="input_filename", required=True, help="Input file location")
    parser.add_argument("-output", dest="output_filename", required=True, help="Output file location")
    args = parser.parse_args()

    process_file(args.input_filename, args.output_filename)

if __name__ == "__main__":
    main()