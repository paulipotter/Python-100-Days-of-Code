import requests
from bs4 import BeautifulSoup
import lxml
from notification_manager import NotificationManager

TARGET_PRICE = 15.0
WEBSITE = 'https://www.amazon.com/Anker-Management-Magnetic-Multipurpose-Lightning/dp/B08C722YMB/?_encoding=UTF8' \
          '&pd_rd_w=CXLDQ&pf_rd_p=6217d442-e765-42e6-8d47-a59919320bf4&pf_rd_r=SVP3SJX0VEYWVP4174M6&pd_rd_r=f59c520d' \
          '-e87d-47b8-b4a7-3e99bd1f9592&pd_rd_wg=DO7OD&ref_=pd_gw_bmx_gp_og4q1d8o '

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15',
    'Accept-Language': 'en-US,en;q=0.9'
}

notification_manager = NotificationManager()
response = requests.get(WEBSITE, headers=headers)

# print(response.text)

soup = BeautifulSoup(response.text, 'lxml')

price_tag = soup.find(class_="a-offscreen")
item_price = price_tag.getText().split('$')[1]
print(item_price)

if TARGET_PRICE >= item_price:
    notification_manager.send_emails(item_price, WEBSITE)

