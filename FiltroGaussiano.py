import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt
from PIL import Image

# Ruta completa a la imagen en la carpeta Downloads
ruta_imagen = r'C:\Users\Lenovo\Downloads\fsociety.webp'

# Cargar la imagen webp
image = Image.open(ruta_imagen)

# Convertir a escala de grises si es necesario
image = image.convert('L')
image_array = np.array(image)

# Aplicar el filtro Gaussiano
sigma = 2  # Ajusta el valor de sigma para mayor o menor suavizado
gaussian_image = scipy.ndimage.gaussian_filter(image_array, sigma=sigma)

# Mostrar la imagen original y la imagen filtrada
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Imagen Original')
plt.imshow(image_array, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Imagen con Filtro Gaussiano')
plt.imshow(gaussian_image, cmap='gray')

plt.show()
