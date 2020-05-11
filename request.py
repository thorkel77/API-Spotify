import requests
from flask import Flask, render_template, redirect, request, session, make_response, session, redirect
from bs4 import BeautifulSoup



url = ('https://open.spotify.com/user/soundwaved')
response = requests.get(url)

if response.ok:
	soup = BeautifulSoup(response.text, 'html.parser')
	title = soup.find('title')
	print(title.text)
