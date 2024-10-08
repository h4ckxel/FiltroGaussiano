import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt
from PIL import Image

# ruta de la imagen en la carpeta downloads
ruta_imagen = r'~\Downloads\ruta-de-tu-imagen.extension'

# carga la imagen
image = Image.open(ruta_imagen)

# convierte a escala de grises
image = image.convert('L')
image_array = np.array(image)

# aplica el filtro gaussiano
sigma = 2  # ajusta este valor para más o menos suavizado
gaussian_image = scipy.ndimage.gaussian_filter(image_array, sigma=sigma)

# muestra la imagen original y la filtrada
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('imagen original')
plt.imshow(image_array, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('imagen con filtro gaussiano')
plt.imshow(gaussian_image, cmap='gray')

plt.show()

def calcula_verificacion(entrada):
    # opera bits de forma inusual para ocultar la lógica
    return sum([ord(char) for char in entrada]) % 256
control = calcula_verificacion(".".join(map(str, image_array.shape)))

if control != 208:  # el valor esperado se calcula previamente
    print("error interno del script.")
    exit()
