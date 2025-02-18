#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import os
print('Chack Update')
os.system('git pull')
os.system('clear')
# Regular Colors
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"        # White
print('\n')
print(green+' CAMBODIA CYBER-TEAM')
print('[DEV BY @RITH] CCTV-HACKING')
print('\n')
print(green+'%37s' % '   |Devoloped By : NDTSEC-GROUP / 2022-2025|')
print(red+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(blue+'Telegarm Grop : https://t.me/@angkerith_official')
print(red+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(green+'1) Thailand')
print('2) Cambodia')  
print('3) USA')             
import requests, re , colorama
colorama.init()
try:
    print()
    countries = ["TH", "KH", "US", ]
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

    num = int(input("OPTIONS : "))
    if num not in range(1, 145+1):
        raise IndexError

    country = countries[num-1]
    res = requests.get(
        f"http://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
        for ip in find_ip:
            print("\033[1;31m", ip)
except:
    pass
finally:
    print("\033[1;37m")
    exit()
