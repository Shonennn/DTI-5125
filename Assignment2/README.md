# Gutenberg Sampler

A Python program that takes a sufficient sample of Gutenberg's digital books, creates random samples of 200 partitions of each book, and makes sure each partition has 100 words. The program also generalizes the process to work with multiple books, maintains the label for each text segment, and uses Regular Expressions and Pandas to manipulate and serialize the data.

## Requirements

- `nltk`
- `pandas`
- `re`

## Usage

1. Download the program by cloning or downloading the repository.
2. Install the required packages by running `pip install -r requirements.txt`
3. Run the program by executing `python main.py`

The program will download the specified books from Project Gutenberg, create random samples of 200 partitions of each book, and save the resulting data in a CSV file named `book_samples.csv`.

## Configuration

The list of book IDs to download can be modified in the `main.py` file. The default books are:
- 'melville-moby_dick.txt'
- 'austen-emma.txt'
- 'shakespeare-hamlet.txt'

You can also change the number of samples to be created, the size of each sample, and the pattern to be searched using regular expressions.

## Results

The program will create a CSV file containing the following columns:

- `text`: the text of the sample
- `label`: the label of the book it belongs to
- `matches`: the matches found using regular expressions

## Note

This is an example code and it should be customized to suit your specific needs.

Please let me know if you have any questions or if there is anything else that I can help you with.
