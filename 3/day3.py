totals = ""
with open("input.txt") as f:
    for rucksack in f.read().strip().split("\n"):
        totals += ("".join(filter(lambda a : a != None,set(map(lambda a : a if (a in rucksack[-len(rucksack)//2 :]) else None, rucksack[:len(rucksack)//2 ])))))
# Got input now sum!
sum = sum(list(map( lambda char : (ord(char)-96 if ord(char) > 96 else ord(char)-64+26),totals)))
print(f"First Answer: {sum}")
