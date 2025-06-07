import pandas as pd
from tools import *

start = 0
end = 100000

numlen = len(str(end))


print("="*80)

df = pd.read_csv(f"data/alphabetically_sorted_numbers_from_{str(start)}_to_{str(end)}.csv", sep="\t")
print(f"Found list of alphabetically sorted numberws from {start} to {end}")

for index, row in df.iterrows():

    seq = BRIGHT_CYAN +  f"{str(row['index'])}th".ljust(numlen+4) + RESET + "-" + BRIGHT_BLUE + str(row['number']).rjust(numlen+4) + RESET + " <-> " + BRIGHT_YELLOW + str(row['words']) + RESET
    print(seq)



print("DONE")