import pandas as pd
from bs4 import BeautifulSoup
import requests
import lxml
import streamlit as st


st.set_page_config(
    page_title='Graphics-card-buyer',
    page_icon="https://images.unsplash.com/photo-1555618254-84e2cf498b01?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8Z3JhcGhpY3MlMjBjYXJkfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
    layout="wide"
    )
st.title("Web scraping amazon realtime Graphics card price ! ")
name = st.radio("**Enter your graphics card branding ?** ",
                key="visibility",
                options=["Amd","Geforce"]).lower()
price = st.slider("**Enter your budget ?** : ",2000,250000,5000)
for i in range(1,20):
    soup = BeautifulSoup(requests.get(f"https://www.amazon.in/s?k=graphics+card&crid=3AEMUTDZ4V4BA&qid=1683695510&sprefix=gra%2Caps%2C353&ref=sr_pg_{i}").text, 'lxml')
    graphics_cards = soup.find_all('div', class_="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16")
    graphics_card_data = []
    for graphics_card in graphics_cards:
        graphics_card_name = graphics_card.find('span', class_="a-size-medium a-color-base a-text-normal").text.lower()
        if name in graphics_card_name:
            graphics_card_price = graphics_card.find('span',class_="a-price-whole").text.replace(',','')
            _graphics_card_price = int(graphics_card_price)
            if price >= _graphics_card_price:
                delivery_by = graphics_card.find('span',class_ = "a-color-base a-text-bold").text
                links = graphics_card.div.h2.a["href"]
                graphics_card_data.append([graphics_card_name,graphics_card_price])
                st.subheader(graphics_card_name)
                st.write(f'***Price*** : **{graphics_card_price}**')
                st.write(f"Delivery time : **{delivery_by}**")
                st.write(f"[Click here to view the product](https://amazon.in{links})")
                
            
print(graphics_card_data)





















































    























































































    










