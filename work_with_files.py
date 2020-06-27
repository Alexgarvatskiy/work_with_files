#file creation
with open('alex.txt', mode='w', encoding='utf-8') as f:
	f.write('date | Name')

#write to file
with open('alex.txt', mode='a', encoding='utf-8') as f:
	f.write('\n05.08.92  Alex',)


#write to file
with open('alex.txt', mode='a',encoding='utf-8') as f:
	f.write('\n09.09.97 Anna\n')

#read to file
with open('alex.txt', mode='r', encoding='utf-8') as f:
	for line in f:
		line = line.upper()
		line = line.replace('\n','')
		print(line)