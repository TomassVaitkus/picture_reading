import cv2
import numpy as np
from sklearn.cluster import KMeans
import pytesseract
import pandas as pd
import os 


pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
# susikeliam i lista visus direktorijoj esanciu nuotrauku pavadinimus

png_list = os.listdir('D:/data_sandbox/pictures/')



# nuskaitom visas nuotraukas ir sukraunam kas nuskaityta i tekstinius failus
for i in png_list:
    img = cv2.imread(f'D:/data_sandbox/pictures/{i}')

    # pasidarom reshape
    pixels = img.reshape(-1, 3)

    # panaudojam Kmeans, kad suskirstyti i klasterius, siuo atveju naudojam standartiskai tris klasterius
    # ir sufitinam i Kmeans modeli
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(pixels)

    # surandam centroidus ir pakeiciam visu pikseliu spalvas i tam klasteriui priklausancio centroido spalva
    segmented_img = kmeans.cluster_centers_[kmeans.labels_]

    # grazinam i nuotrauka, bet tik su likusiom trim spalvopm.
    segmented_img = segmented_img.reshape(img.shape)

    # konvertuojam i 8 bitus. Nes opencv dirba su 8 bitu vaizdais, o tai reiskia, kad  kiekvienas pikselis gali tureti reiksme nuo 0-255
    # jei to nepadarysim - gali atsirasti klaidos ar netikslios spalvos
    segmented_img = np.uint8(segmented_img)

    # panaudojam teserakta, kad nusiskaityti teksta is turimo paveikslo
    text = pytesseract.image_to_string(segmented_img,lang='lit')

    with open(f'D:/data_sandbox/output/{i[:-4]}.txt','w', encoding='utf-8') as t:
        t.write(text)
        t.close()

# cia nezinau ar sitas variantas tinka, bet kolkas ji uzkomentuoju ir palieku
    # bet greiciausiai jo neliks :)

# rows = text.split('\n')  # Skaidykite tekstą į eilutes
# data = [row.split(',') for row in rows if row]
# df = pd.DataFrame(data)
# df.to_excel('D:/data_sandbox/output/baltneta.xlsx', index=False)