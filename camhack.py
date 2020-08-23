import requests, re, os, time
import pycountry
from termcolor import colored
from os import system

#Author: Justin Karl Salimbagat
#Date Created: 08/22/2020

os.system('clear')
while True:
	for i in range(2):
		print(colored("Loading...", "green"))
		time.sleep(0.3)
		os.system('clear')
		print(colored("lOading..", "green"))
		time.sleep(0.3)
		os.system('clear')
		print(colored("loAding.:", "green"))
		time.sleep(0.3)
		os.system('clear')
		print(colored("loaDing...", "green"))
		time.sleep(0.3)
		os.system('clear')
		print(colored("loadIng...", "green"))
		time.sleep(0.3)
		os.system('clear')
		print(colored("loadiNg..", "green"))
		time.sleep(0.3)
		os.system('clear')
		print(colored("loadinG.", "green"))
		time.sleep(0.3)
		os.system('clear')
		print(colored("loadiNg..", "green"))
		time.sleep(0.3)
		os.system('clear')
		print(colored("loadIng.", "green"))
		time.sleep(0.3)
		os.system('clear')
		print(colored("loaDing..", "green"))
		time.sleep(0.3)
		os.system('clear')
		print(colored("loAding...", "green"))
		time.sleep(0.3)
		os.system('clear')
		print(colored("lOading..", "green"))
		time.sleep(0.3)
		os.system('clear')
	
	print(colored("•~~~•~~~•~~~•~~~•~~~•~~~•~~~•~~~•~~~•~~~•~~~•~~~•~~~•", "red"))
	print(colored("[ + ] Developed by: Justin Karl Salimbagat", "yellow"))
	print(colored("[ + ] Facebook Profile: https://www.facebook.com/leah.berenio", "yellow"))
	print(colored("[ + ] My Github: https://www.github.com/justinkarl", "yellow"))
	print(colored("•~~~•~~~•~~~•~~~•~~~•~~~•~~~•~~~•~~~•~~~•~~~•~~~•~~~•", "red"))
	print(colored("[ + ] Tool Name: Cam Hack", "yellow"))
	print(colored("[ + ] Github Repo: https://www.github.com/justinkarl/camhack", "yellow"))
	print(colored("•~~~•~~~•~~~•~~~•~~~•~~~•~~~•~~~•~~~•~~~•~~~•~~~•~~~•", "red"))
	
	country_name = (input(colored("\n\nEnter country name$", "yellow")))
	country = pycountry.countries.get(name=country_name).alpha_2
	try:
		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}
		for page in range(0, 82):
			url = ("https://www.insecam.org/en/bycountry/"+country+"?page="+str(page))
			res = requests.get(url, headers=headers)
			cam_ip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
			count = 0
			
		for _ in cam_ip:
			h = cam_ip[count]
			print(colored(h, "yellow"))
			f = open('logs.txt', 'a')
			f.write(f'{cam_ip}'+'\n')
			f.close()
				
			count += 1
			
	except:
		print(colored("\nOops..! Something went wrong :(\nPlease check you internet connection,\nor the country you input is invalid,\nPlease try again later.", "red"))
		
	input = input(colored("\n\nDo u want to scan again? [Y/N]", "yellow"))
	if input == "n" or input == "N" or input == "No":
		os.system('clear')
		country_name = ""
		break
