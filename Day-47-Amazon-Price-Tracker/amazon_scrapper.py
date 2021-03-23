import requests
from bs4 import BeautifulSoup as bs

user_product_url = 'https://www.amazon.es/nuevo-echo-dot-4a-generacion-altavoz-inteligente-con-alexa-blanco/dp/B084J4MZ' \
                   'K6/ref=gbps_img_s-5_5212_82f4600f?smid=A1AT7YVPFBWXBL&pf_rd_p=88bac0c7-285e-402f-8b50-478fef455212&' \
                   'pf_rd_s=slot-5&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=A1AT7YVPFBWXBL&pf_rd_r=5N9HAZH12ZD5NDQHM9WA'
headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/89.0.4389.90 Safari/537.36'
        }


class AmazonScrapper:
    def get_product_price(self):
        product_url = requests.get(url=user_product_url, headers=headers)
        soup = bs(product_url.content, "html.parser")

        try:
            previous_price = soup.find(id="priceblock_dealprice").getText().replace(u'\xa0', u' ').split()[0]
            deal_price = soup.find(class_="priceBlockStrikePriceString").getText().replace(u'\xa0', u' ').split()[0]
        except AttributeError:
            pass
        else:
            data_to_send = [float(previous_price.replace(',', '.')), float(deal_price.replace(',', '.'))]
            return data_to_send
