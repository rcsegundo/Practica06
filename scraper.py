import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://scrapeme.live/shop/"
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, "html.parser")
productos = soup.find_all("li", class_="product")

datos = []
for producto in productos:
    nombre = producto.find("h2", class_="woocommerce-loop-product__title").text.strip()
    precio_texto = producto.find("span", class_="woocommerce-Price-amount").text
    precio = float(precio_texto.replace("£", "").replace("Â", "").strip())
    link = producto.find("a", class_="woocommerce-LoopProduct-link")["href"]

    datos.append({
        "nombre": nombre,
        "precio_gbp": precio,
        "link": link
    })

df = pd.DataFrame(datos)
df.to_csv("catalogo_pokemon.csv", index=False)
print("Scraping exitoso y archivo catalogo_pokemon.csv creado.")
