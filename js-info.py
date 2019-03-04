#!/usr/bin/python
#coding:utf-8


import requests
import re
import jsbeautifier


def match(sr):
	f1 = open('js-read.txt', 'r') 
	line =0
	while True:
		lines = f1.readline() 
		if not lines:  
			break
		line += 1
		if sr.findall(lines):
			key=str(sr.findall(lines))
			fs.write('-'*50+'\n')
			fs.write("[*] on line : "+ str(line)+"--> "+key+'\n')
			fs.write(str(lines).strip('\r\n')+'\n\n')
			#report_line(key,line,lines)
			continue
	f1.close()
f2=open('js-url.txt','r')
for url in f2:
	url=url.strip('\r\n')		
	fs=open('result/'+str(url.split('/')[-1])+'.txt','w')
	try:
		r = requests.get(url)
		if r.status_code == 200:
			fsr=open('js-read.txt','w')
			fsr.write(jsbeautifier.beautify(r.text).encode('utf-8'))
			fsr.close()
			f=open('keyword.txt','r')
			for keyword in f:
				keyword=keyword.strip('\n\r')
				sr=re.compile(keyword,re.I)
				if sr.findall(r.text):
					match(sr)
			f.close()
		else:
			print ('[!]Can`t connect! '+url)
	except:
		print '[!]Error '+url
	print (url+'READED!')
	fs.close()
f2.close()

