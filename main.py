import collections

file = open("texto.txt", "r", encoding = "utf-8").readlines()

first_name = []
for i in file:
  first_name.append(i.split()[0])

count = collections.Counter(first_name)

print(count)

