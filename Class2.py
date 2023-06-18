import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import csv
import cv2
from skimage.metrics import structural_similarity as ssim
image1 = cv2.imread('5RC_6007.jpg')
image2 = cv2.imread('5RC_6009.jpg')
def calculate_difference(x, y, etiket, rotation):
    if etiket.startswith("RS"):
      width = 86
      height = 267
    elif etiket.startswith("D"):
      width = 139
      height = 80
    elif etiket.startswith("R"):
      width = 80
      height = 42
    elif etiket.startswith("P"):
      width = 523
      height = 355
    elif etiket.startswith("J"):
      width = 338
      height = 382
    elif etiket.startswith("C"):
      width = 27
      height = 59
    elif etiket.startswith("Y"):
      width = 78
      height = 102
    elif etiket.startswith("U"):
      width = 171
      height = 176
    elif etiket.startswith("Q"):
      width = 100
      height = 79
    elif etiket.startswith("LE"):
      width = 85
      height = 38
    elif etiket.startswith("L"):
      width = 312
      height = 298
    elif etiket.startswith("K"):
      width = 724
      height = 303
    else:
      width = 26
      height = 62


    roi1 = image1[5464-y:5464-y+height, x:x+width]

    roi2 = image2[5464-y+100:5464-y+height+100, x+100:x+width+100]
    gray_roi1 = cv2.cvtColor(roi1, cv2.COLOR_BGR2GRAY)


    gray_roi2 = cv2.cvtColor(roi2, cv2.COLOR_BGR2GRAY)
    #her resmin tek tek kıyaslandığını görebilmek için test kodları
    #cv2.imshow("ROI 1", roi1)
    #print(etiket)
    #cv2.imshow("ROI 2", roi2)
    #print(etiket)

   # cv2.waitKey(0)
    #cv2.destroyAllWindows()

    score, _ = ssim(gray_roi1, gray_roi2, full=True)
    return score
new_column_name = "Difference"
with open('libi.csv',encoding='windows-1252') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames + [new_column_name]

    rows = []
    for row in reader:
        # Difference sütununu 1 olarak ayarla
        row[new_column_name] = '1'

        # X ve Y koordinatlarını al
        x = float(row["Center-X(mm)"])
        x=x*25+2320
        x = int(x)
        y = float(row["Center-Y(mm)"])
        y=y*25+1100
        y = int(y)
        etiket = row['Designator']
        rotation = int(row['Rotation'])

        # Belirli bir işlemi gerçekleştir
        result = calculate_difference(x, y, etiket, rotation)

        # İşlem sonucunu Difference sütununa ata
        row[new_column_name] = str(result)

        rows.append(row)

# Güncellenmiş verileri dosyaya yaz
with open('libi.csv', 'w', newline='',encoding='windows-1252') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Dosya güncellendi.")
