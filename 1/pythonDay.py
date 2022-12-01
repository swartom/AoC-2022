totals = list()
with open("data.txt",'r') as elves:
    for elf in elves.read().strip().split("\n\n") :
        totals.append(sum(int(calories) for calories in elf.split("\n")))
    
totals.sort()
print(f"First Answer: {totals[-1]}")
print(f"Second Answer: {sum(totals[-3:])}")