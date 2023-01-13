from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.booking.com/searchresults.es.html?ss=Nueva+York%2C+New+York+State%2C+Estados+Unidos&efdco=1&label=es-JCB2UqznXtCO_RDP_nj5CAS410545262609%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005530%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Ye8F2ouj63ytkBtrYs5TAfs&aid=376371&lang=es&sb=1&src_elem=sb&src=index&dest_id=20088325&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=es&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=0f1e5f85fa8200e4&ac_meta=GhAwZjFlNWY4NWZhODIwMGU0IAAoATICZXM6BE5ldyBAAEoAUAA%3D&checkin=2023-01-20&checkout=2023-01-22&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

response = requests.get(url, headers=headers)
print(response.status_code)
soup = BeautifulSoup(response.text, 'lxml')

o = {}
l = list()
fac = []
fac_arr = []


if response.status_code == 200:  
    new_list = response.json()['data']
    with open('new.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['nombre', 'url', 'localizacion','numero coments','desayuno','cancelacion','precio'])
        for item in soup.select('.a826ba81c4.fe821aea6c.fa2f36ad22.afd256fc79.d08f526e0d.ed11e24d01.ef9845d4b3.da89aeb942'):
            try:
                print('---------------------')
                print(item.select('.fcab3ed991.a23c043802')[0].get_text().strip())  # name
                
                print(item.select('.e13098a59f')[0]['href'])                        # url
                print(item.select('.f4bd0794db.b4273d69aa')[0].get_text().strip())  # location
                print(item.select('.d8eab2cf7f.c90c0a70d3.db63693c62')[0].get_text().strip()) #hw many commets
                try:
                    print(item.select('.e05969d63d')[0].get_text().strip())             # breakfast?
                except Exception as e2:
                    print('No hay desayuno incluido')
                
                #print(item.select('.e4755bbd60')[0])             # number of stars
                try:
                    print(item.select('.d506630cf3')[0].get_text().strip())             # cancelation
                except Exception as e1:
                    print('No hay cancelacion')

                print('---------------------')
            except Exception as e:
                print('')
                
            # clase a predecir
            print(item.select('.b5cd09854e.d10a6220b4')[0].get_text().strip())  # price
else:
    print('Status Failed On', response.status_code)
  
