#Concatenate two files 
def combine_text_files(file1, file2, path):
    filenames = [file1, file2]
    with open(path, 'w', encoding ="utf-8") as outfile:
        for fname in filenames:
            with open(fname, encoding ="utf-8") as infile:
                for line in infile:
                    outfile.write(line)

#specify the path for the scrapped data
file_en_scraped ="./data/new_aligned/english.en"
file_sw_scraped = "./data/new_aligned/swahili.sw"

#specify the path for the opus data
file_en_opus = "./data/opus/GlobalVoices.en.en"
file_sw_opus = "./data/opus/GlobalVoices.sw.sw"

#specify the path to save the merged data
path_en= "./data/opus/merged_en"
path_sw= './data/opus/merged_sw'

#Combine the english files
combine_text_files(file_en_scraped, file_en_opus, path_en)

#Combine the swahili files
combine_text_files(file_sw_scraped, file_sw_opus, path_sw)