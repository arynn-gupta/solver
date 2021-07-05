#!/usr/bin/env python3

import os
from os import system

try :
	from PIL import Image
except ModuleNotFoundError:
	system("pip3 install pillow")

try :
	import pytesseract as pt 
except ModuleNotFoundError:
	system("pip3 install pytesseract")
	import pytesseract as pt 

try :
	system('cls')
except:
	pass
print('\033[92m'+"	               __               ")
print("	   _________  / /   _____  _____")
print("	  / ___/ __ \/ / | / / _ \/ ___/")
print("	 (__  ) /_/ / /| |/ /  __/ /    ")
print("	/____/\____/_/ |___/\___/_/ @aryan")
print("                                "+'\u001b[0m')

def main(): 
	print('\u001b[36m'+'Renaming images .... ')
	path = "copy_images_here"
	tempPath = "img_to_text"
	for count, filename in enumerate(os.listdir(path)): 
		if count<10 :
			dst = "0" + str(count) + ".jpg"
		else :
			dst = str(count) + ".jpg"
		src = os.path.join(path, filename )
		dst = os.path.join(path, dst )
		os.rename(src, dst) 
	print('Converting images to text .....'+'\u001b[0m')
	for imageName in os.listdir(path): 
		inputPath = os.path.join(path, imageName) 
		img = Image.open(inputPath) 
		text = pt.image_to_string(img, lang ="eng")
		imagePath = imageName[0:-4] 
		fullTempPath = os.path.join(tempPath,imagePath+".txt") 
		file = open(fullTempPath, "w") 
		file.write(text) 
		file.close()  
	print('\u001b[31;1m'+"\nEnter exit to exit"+'\u001b[0m')
	while(1) :
		search_str = input('\u001b[37m'+"\nEnter keywords to search : "+'\u001b[0m').lower()
		print('\u001b[0m'+' ')
		if (search_str == 'exit') :
			print('\u001b[31;1m'+'Deleting files .... '+'\u001b[0m')
			for filename in os.listdir(path):
				os.remove(os.path.join(path,filename))
			for filename in os.listdir(tempPath):
				os.remove(os.path.join(tempPath,filename))
			quit()
		else :
			search_list = list(search_str.split(" ")) 
			answer = []
			for textName in os.listdir(tempPath):
				fullTempPath = os.path.join(tempPath,textName) 
				file = open(fullTempPath, "r") 
				for li in search_list:
					if li in file.read().lower() :
						answer.append(textName)
				file.close() 
			try :
				res = max(set(answer), key = answer.count)
			except :
				print('\u001b[36m'+"No file found with such keyword"+'\u001b[0m')
				continue
			answer = list(dict.fromkeys(answer))
			try:
				system("start copy_images_here/"+res[0:-4]+".jpg")
			except:
				pass
			for li in answer :
				print('\u001b[36m'+li[0:-4]+".jpg"+'\u001b[0m')

if __name__ == '__main__': 
	main() 