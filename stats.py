from collections import defaultdict


def get_num_words(text: str) -> int:
  return len(text.split())


def get_num_characters(text: str) -> dict[str, int]:
  freq: dict[str, int] = defaultdict(int)

  for c in text:
    freq[c.lower()] = freq[c.lower()] + 1

  return freq


def sort_on_freq(items: dict[str, str | int]) -> int:
  return items["num"]


def get_sorted_frequencies(char_freq: dict[str, int]) -> list[dict[str, str | int]]:
  freqs : list[dict[str, str | int]]= []

  for (ch, freq) in char_freq.items():
    freqs.append({"char": ch, "num": freq})
  
  freqs.sort(reverse=True, key=sort_on_freq)
  return freqs
  
