import csv
import os
import requests
import shutil
import argparse

#parser = argparse.ArgumentParser(description='Tool to create a zip file of all images archived')
#parser.add_argument('-n', '--name', help='Path to csv file created by retrieve_msgs.py', default = 'temp.csv')
#parser.add_argument('-z','--zip', help = 'Name of output zip file', default = 'temp')

def make_zip():
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
		if(link[0] != "h"):
			continue
		r = requests.get(link, stream = True)
		path = 'img'+str(i)+'.jpg'
		if r.status_code == 200:
			with open(path, 'wb') as out_file:
				r.raw.decode_content = True
				shutil.copyfileobj(r.raw,out_file)
		i+= 1



def make_folder(dirname):
	if not os.path.exists(os.getcwd() + '/' +dirname):
		os.makedirs(os.getcwd() + '/'+dirname)


make_zip()