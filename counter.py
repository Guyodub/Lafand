
sw_file = open("./data/aligned/swahili.sw","r", encoding = "utf-8").read()
en_file = open("./data/aligned/english.en","r", encoding = "utf-8").read()

counter = 0
  
sw_list = sw_file.split("\n")
en_list = en_file.split("\n")
  
for i in sw_list:
    if i:
        counter += 1
print("Number of lines in swahili file")
print(counter)
counter = 0

for i in en_list:
    if i:
        counter += 1
print("Number of lines in english file")
print(counter)