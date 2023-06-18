import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
#Mapping yaptığımız sınıf
# CSV dosyasını oku
dfilk = pd.read_csv("libi.csv", encoding='windows-1252')
df= dfilk[dfilk["Layer"] == "TopLayer"]
# Resmi yükle
img = mpimg.imread("5RC_6007.jpg")

# Boş bir grafik oluştur
fig, ax = plt.subplots()

# Resmi göster
ax.imshow(img, extent=[0, img.shape[1], 0, img.shape[0]])

# Her bir satır için noktaları ekle
for index, row in df.iterrows():

    x = int(row["Center-X(mm)"])*25+2500
    y = int(row["Center-Y(mm)"])*25+1100


    ax.plot(x, y, marker="o", markersize=4,  color='red')

# Eksen etiketlerini ayarla
ax.set_xlabel("X Koordinatı (mm)")
ax.set_ylabel("Y Koordinatı (mm)")


# Etiketleri göster


# Grafik penceresini göster
plt.show()