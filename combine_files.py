#Concatenate two files 
def combine_text_files(file1, file2, path):
    filenames = [file1, file2]
    with open(path, 'w', encoding ="utf-8") as outfile:
        for fname in filenames:
            with open(fname, encoding ="utf-8") as infile:
                for line in infile:
                    outfile.write(line)

#specify the path for the jw300 data
file_en_scraped = "./data/jw300/train.en"
file_sw_scraped = "./data/jw300/train.sw"

#specify the path for the opus data
file_en_opus = "./data/opus/GlobalVoices.en"
file_sw_opus = "./data/opus/GlobalVoices.sw"

#specify the path to save the merged data
path_en= "./data/merged/merged.en"
path_sw= './data/merged/merged.sw'

#Combine the english files
combine_text_files(file_en_scraped, file_en_opus, path_en)

#Combine the swahili files
combine_text_files(file_sw_scraped, file_sw_opus, path_sw)