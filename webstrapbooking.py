from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv

url = 'https://www.booking.com/searchresults.es.html?ss=Nueva+York%2C+New+York+State%2C+Estados+Unidos&efdco=1&label=es-JCB2UqznXtCO_RDP_nj5CAS410545262609%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005530%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Ye8F2ouj63ytkBtrYs5TAfs&aid=376371&lang=es&sb=1&src_elem=sb&src=index&dest_id=20088325&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=es&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=0f1e5f85fa8200e4&ac_meta=GhAwZjFlNWY4NWZhODIwMGU0IAAoATICZXM6BE5ldyBAAEoAUAA%3D&checkin=2023-01-20&checkout=2023-01-22&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

response = requests.get(url, headers=headers)
print(response.status_code)
soup = BeautifulSoup(response.text, 'lxml')


if response.status_code == 200: 
    # obtener la lista de noticias de la respuesta
    # new_list = response.json()['data']
    # abrir un fichero csv para guardar los datos
    with open('new.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # crear un objeto DictWriter para escribir los datos en el fichero csv
        writer = csv.DictWriter(csvfile, fieldnames=['nombre', 'url', 'localizacion','numero coments','desayuno','cancelacion','precio'])
        # escribir los encabezados
        writer.writeheader()
        for item in soup.select('.a826ba81c4.fe821aea6c.fa2f36ad22.afd256fc79.d08f526e0d.ed11e24d01.ef9845d4b3.da89aeb942'):
            try:
                print('---------------------')
                
                name = item.select('.fcab3ed991.a23c043802')[0].get_text().strip()
                print(name)  # name

                url = item.select('.e13098a59f')[0]['href']
                print(url)   # url

                location = item.select('.f4bd0794db.b4273d69aa')[0].get_text().strip()
                print(location)  # location

                num_coments = item.select('.d8eab2cf7f.c90c0a70d3.db63693c62')[0].get_text().strip()
                print(num_coments) #hw many commets
                try:
                    breakfast = item.select('.e05969d63d')[0].get_text().strip()
                    print(breakfast) # breakfast?
                except Exception as e2:
                    breakfast='No hay desayuno incluido'
                    print(breakfast)
                
                #print(item.select('.e4755bbd60')[0])             # number of stars


                try:
                    cancelation = item.select('.d506630cf3')[0].get_text().strip()
                    print(cancelation)    # cancelation
                except Exception as e1:
                    cancelation = 'No hay cancelacion'
                    print(cancelation)

                # clase a predecir
                price = item.select('.fcab3ed991.fbd1d3018c.e729ed5ab6')[0].get_text().strip()
                print(price)  # price

            
                    
                writer.writerow({
                   'nombre':name, 
                    'url':url, 
                    'localizacion':location,
                    'numero coments':num_coments,
                    'desayuno':breakfast,
                    'cancelacion':cancelation,
                    'precio': price
                })
              
            except Exception as e:
                print(e)

else:
    print('Status Failed On', response.status_code)
