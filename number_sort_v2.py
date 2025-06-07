# IMPROVED NUMBER SORTER
# AUTHOR: JMW

from num2words import num2words
from word2number import w2n
import pandas as pd
import time



def log(printif:bool, *msg):
    if printif:
        print(*msg)


def num2word_list(numbers):
    words = []
    for num in numbers:
        words.append(num2words(num).replace(",", ""))
    return words


def word2num_list(words):
    nums = []
    for word in words:
        nums.append(w2n.word_to_num(word))
    return nums


def sort_numbers_alphabetically(start:int, end:int, logstate=True):
    log(logstate, f"attempting to alphabetically sort the numbers from {start}, to {end}:")
    
    numbers = list(range(start, end+1, 1))

    log(logstate, " > creating word list:")

    words = num2word_list(numbers)

    log(logstate, " > attempting to sort list:")
    words.sort()
    return words




if __name__ == '__main__':
    
    list_starts = []
    list_ends = []
    list_dt = []

    

    start = 0
    for i in range(50):

        try: 
            end = 10**i
            t_start = time.time()
            print("-"*60)
            print(f"New sorting range: {start} to 1e{i}")
            words = sort_numbers_alphabetically(start, end)
            print(" > creating number list:")
            nums = word2num_list(words)
            t_end = time.time()


            dt = t_end - t_start
            list_starts.append(start)
            list_ends.append(end)
            list_dt.append(dt)
            


            print(" > creating dataframe")
            df = pd.DataFrame({"index":list(range(start, end+1)), "number":nums, "words":words})

            filename = f"data/alphabetically_sorted_numbers_from_{start}_to_{end}.csv"
            print(f" > saving results to: {filename}")
            df.to_csv(filename, sep="\t", index=None)


            df2 = pd.DataFrame({"time_start":list_starts, "time_end":list_ends, "dt [s]":list_dt})
            filename2 = f"data/metadata.csv"
            df2.to_csv(filename2, sep="\t", index=None)

        except Exception as E:
            print(E)
            break

print(f"last attempted range: {start} to {end}")
print("DONE")