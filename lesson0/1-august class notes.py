file_name './text_file.txt'
with open(file_name) as fd:
	for line_num, line in enumerate(fd.readllines(), 1):
		print(f'Line {line_num}: {line}', end='')

