import requests
from playsound import playsound
import json

f=open('all_links.json')
link=json.load(f)
url=link['links']['audio_link']
playsound(url)

f.close


