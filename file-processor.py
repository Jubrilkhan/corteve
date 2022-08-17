from os import listdir, walk
from os.path import isfile, join

onlyfiles = [f for f in listdir('./code-challenge-template/wx_data') if isfile(join('./code-challenge-template/wx_data', f))]


for infile in onlyfiles:
	matrix = []
	data = infile[:7]
	infile_dir_path = './code-challenge-template/wx_data/'+ infile 
	with open(infile_dir_path, 'r') as fin:
		for line in fin:
			matrix.append(line.strip().split())
	for row in matrix:
		row.append(data)
	outfile = './code-challenge-template/wx_data2/' + infile
	with open(outfile, 'w') as fout:
		for row in matrix:
			fout.write((' ').join(row) + '\n')

