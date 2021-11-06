sw_file = "./data/aligned/swahili.sw"
en_file = "./data/aligned/english.en"


sw_file_gv = "./data/opus/GlobalVoices.sw"
en_file_gv = "./data/opus/GlobalVoices.en"

sw_file_jw = "./data/jw300/train.sw"
en_file_jw= "./data/jw300/train.en"

sw_file_m ="./data/merged/merged.sw"
en_file_m = "./data/merged/merged.en"

sw_file_s ="./data/shuffled/train.sw"
en_file_s = "./data/shuffled/train.en"


def count_number_of_lines(filepath):
    file = open(filepath, 'r', encoding =  "utf-8")
    line_count = 0
    for line in file:
        if line !='\n':
            line_count +=1
    file.close()

    print('The file', filepath.rsplit('/', 1)[-1], 'has', line_count, 'lines')

count_number_of_lines(sw_file)
count_number_of_lines(en_file)
count_number_of_lines(sw_file_gv)
count_number_of_lines(en_file_gv)
count_number_of_lines(sw_file_jw)
count_number_of_lines(en_file_jw)
count_number_of_lines(sw_file_m)
count_number_of_lines(en_file_m)
count_number_of_lines(sw_file_s)
count_number_of_lines(en_file_s)

print(30782+872007)


'''
The file swahili.sw has 3666 lines
The file english.en has 3665 lines
The file GlobalVoices.sw has 30782 lines
The file GlobalVoices.en has 30782 lines
The file train.sw has 872007 lines
The file train.en has 872007 lines
The file merged.sw has 902789 lines
The file merged.en has 902789 lines
902789
'''