import csv
import os
import requests
import shutil

list_imgs = []
with open('temp.csv', newline='') as f:
	reader = csv.reader(f)
	for row in reader:
		if(row[3] != ""):
			list_imgs.append(row[3])
			#print(row[3])

f.close()
i = 0
for link in list_imgs:
	print(link)
	r = requests.get(link, stream = True)
	path = 'img'+str(i)+'.jpg'
	if r.status_code == 200:
		with open(path, 'wb') as out_file:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw,out_file)
	i+= 1
