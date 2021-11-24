#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

def send_req(nm):
	url = 'http://'+nm+'.okta.com'
	print("[*] Sending request")
	r = requests.get(url)
	print("[*] Getting response")
	return r

def title_ex(txt):
	soup = BeautifulSoup(txt, 'html.parser')
	print("[*] Processing response")
	for title in soup.find_all('title'):
		return title.get_text()

def title_checker(title):
	if title != "Sign In":
		return 1
	else:
		return 0

def main():
	print("*****OKTA SCANNER*****")
	while 1:
		print("********USAGE*********")
		print("OPTION 1: Company Lookup")
		print("OPTION 2: List processing")
		print("OPTION Q: Quit")
		opt = input("> ")
		if opt.lower() == 'q':
			print("[*] Exiting")
			break
		elif int(opt) == 1:
			name = input("Enter company name: ")
			response = send_req(name)
			title = title_ex(response.text)
			output = title_checker(title)
			if output == 1:
				print(name + " uses Okta")
			else:
				print(name + " does not use Okta")
		elif int(opt) == 2:
			print("[*] Option 2 selected")
		print("*")
		print("*")
		print("*")
if __name__ == "__main__":
	main()
