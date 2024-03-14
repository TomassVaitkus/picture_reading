import asyncio
from pyppeteer import launch
import random
import time

# url listas

# url_list = [
#     "https://rekvizitai.vz.lt/imone/atea/apyvarta/",
#     "https://rekvizitai.vz.lt/imone/{j}/",
#     "https://rekvizitai.vz.lt/imone/atea/atlyginimas/",
#     "https://rekvizitai.vz.lt/imone/atea/skolos-sodrai/"
# ]




# pasirasom funkcija, kuria naudosim nuotraukos darymui

async def screenshot(url: str, path: str):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    await page.screenshot({'path': path, 'fullPage': True})  
    await browser.close()


# pasiduodam imoniu lista (tik pavadinimus, nes kitaip nesuformuosim url)

partner_list = ['Atea']
partner_list_joined = []
for i in partner_list:
    partner_list_joined.append('_'.join(i.split()).lower())

for j in partner_list_joined:
    url_list = [
        f"https://rekvizitai.vz.lt/imone/{j}/apyvarta/",
        f"https://rekvizitai.vz.lt/imone/{j}/",
        f"https://rekvizitai.vz.lt/imone/{j}/atlyginimas/",
        f"https://rekvizitai.vz.lt/imone/{j}/skolos-sodrai/"
        ]
    for url in url_list:
        seconds = random.randint(1,3)
        time.sleep(seconds)
        # url = url
        if url == url_list[0]:
            path = f'D:/data_sandbox/pictures/apyvarta_{j}.png'
            asyncio.get_event_loop().run_until_complete(screenshot(url, path))
        if url == url_list[1]:
            path = f'D:/data_sandbox/pictures/{j}.png'
            asyncio.get_event_loop().run_until_complete(screenshot(url, path))
        if url == url_list[2]:
            path = f'D:/data_sandbox/pictures/atlyginimas_{j}.png'
            asyncio.get_event_loop().run_until_complete(screenshot(url, path))
        if url == url_list[3]:
            path = f'D:/data_sandbox/pictures/skolos_sodrai_{j}.png'
            asyncio.get_event_loop().run_until_complete(screenshot(url, path))
        else:
            pass

        
