from num2words import num2words
from word2number import w2n
import pandas as pd


word = "two thousand, two hundred and ninety-three".replace(",", "")


print(word)

num = w2n.word_to_num(word)

print(num)