import sys

from stats import get_num_words, get_num_characters, get_sorted_frequencies

def get_book_text(file: str):
  with open(file, "r") as f:
    content = f.read()
    return content


def print_report(book: str, word_count: int, frequencies: list[dict[str, str | int]]):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book}...")

  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")

  print("--------- Character Count -------")
  for freq in frequencies:
    if freq["char"].isalpha():
      print(f'{freq["char"]}: {freq["num"]}')


def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_name = sys.argv[1]
  book_content = get_book_text(book_name)
  nb_words = get_num_words(book_content)
  char_freq = get_num_characters(book_content)
  sorted_freq = get_sorted_frequencies(char_freq)
  
  print_report(book_name, nb_words, sorted_freq)


if __name__ == "__main__":
  main()