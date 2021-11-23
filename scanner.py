#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

def main():
	print("*****OKTA SCANNER*****")
	name = input("Enter company name: ")
	response = send_req(name)
	title = title_ex(response.text)
	output = title_checker(title)
	if output == 1:
		print(name + " uses Okta")
	else:
		print(name + " does not use Okta")

def send_req(nm):
	url = 'http://'+nm+'.okta.com'
	print("[*] Sending request")
	r = requests.get(url)
	print("[*] Getting response")
	return r

def title_ex(txt):
	soup = BeautifulSoup(txt, 'html.parser')
	for title in soup.find_all('title'):
		return title.get_text()

def title_checker(title):
	if title != "Sign In":
		return 1
	else:
		return 0

if __name__ == "__main__":
	main()
