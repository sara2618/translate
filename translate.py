from googletrans import Translator
import sys

#read files
input_file = sys.argv[1]
output_file = sys.argv[2]

data = open(input_file, 'r', encoding = sys.stdin.encoding) 
data_lines = data.readlines()

list = []

#preprocess data
for line in data_lines:
	line = line.replace('\n', '')
	line = line.replace('- ', '')
	tmp_list = [x.strip() for x in line.split('.')]
	list += tmp_list

translator = Translator()

#translate and write files
with open(output_file, 'w') as text_file:
	for item in list:
		tmp = translator.translate(item, dest='zh-TW')
		text_file.write(item + '.' + '\n')
		text_file.write(tmp.text + '\n')
		text_file.write('\n')

text_file.close()