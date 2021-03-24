from selenium_driver import driver
amazon_url = 'https://www.amazon.es/Huawei-Matebook-D15-Multi-Screen-Collaboration/dp/B083V6LT1T/ref=pd_day0_2?pd_rd_w' \
             '=PD3a8&pf_rd_p=0ff21a3e-4297-4047-87ec-ba06b6bc995e&pf_rd_r=K80J9VPE80R3PTN64J0G&pd_rd_r=9d94802a-885f-4' \
             'b9e-8935-1672639d291a&pd_rd_wg=tkcrg&pd_rd_i=B083V6LT1T&psc=1'

driver.get(amazon_url)
deal_price = driver.find_element_by_id('priceblock_ourprice')
print(deal_price.text)

driver.close()
