#import packages
import numpy as np
import random

#Reading the texts files
sw_file = open("./data/opus/merged_sw","r", encoding = "utf-8").read()
en_file = open("./data/opus/merged_en","r", encoding = "utf-8").read()

#convert text to list by splittig using empty lines
sw_list = sw_file.split("\n\n")
en_list = en_file.split("\n\n")


#append the shuffled items in a new list
sw_lst_new = []
en_lst_new = []
lst = np.arange(len(sw_list)) #arange the list
random.shuffle(lst) #shuffle the indices
for idx in lst:
    sw_lst_new.append(sw_list[idx])
    en_lst_new.append(en_list[idx])

#write into .txt files
with open("./data/new_aligned/shuffled_en.txt", "w", encoding ='utf-8') as output:
    for item in en_lst_new:
        output.write(str(item)+'\n\n')
        
with open("./data/new_aligned/shuffled_sw.txt", "w", encoding ='utf-8') as output:
    for item in sw_lst_new:
        output.write(str(item)+'\n\n')
