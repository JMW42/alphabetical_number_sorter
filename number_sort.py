from num2words import num2words
from word2number import w2n
import pandas as pd

max_num = 1e1 # aximum number to be counted to from 0 on (both edges inclusiv)


# itterate over numbers and sort them
for i in range(10):
    max_num = 1*10**(i)
    max_num = int(max_num)

    print(f"sorting the numbers from 0 to {max_num}")

    numbers = list(range(max_num+1)) # list of numbers
    words = [] # list for written word names of numbers

    # generate word list
    for num in numbers:
        words.append(num2words(num).replace(",", ""))

    word_sorted = sorted(words) # sort words alpahbetically

    # print results
    #+print(words)
    #print(word_sorted)
    print("sorted numbers:")

    numbers_sorted = []
    for word in word_sorted:
        #print(word, end=", ")
        num = w2n.word_to_num(word)
        numbers_sorted.append(num)
        print(f"({num}, {word})", end=", ")

    print(f"\n length of list {len(numbers_sorted)}")

    print("\n saving results to csv ....")
    index =[s + "th" for s in list(map(str, numbers)) ]

    df = pd.DataFrame({"index":index, "words":word_sorted, "numbers": numbers_sorted})
    df.to_csv(f"data/alphabetically_sorted_numbers_from_0_to_{str(max_num)}.csv", sep="\t", index=None)
