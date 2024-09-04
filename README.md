# 💻 **Filtro Gaussiano en Imágenes** 🖥️

<div align="center">
<img src="https://developer.ridgerun.com/wiki/images/6/62/GstVPI_Gaussian_filter.gif"/>
</div>

## **Descripción del Proyecto**

Bienvenido al proyecto de ***Suavizado de Imágenes con Filtro Gaussiano (SIFG)***. Este script Python aplica un filtro gaussiano a una imagen en escala de grises para darle un efecto de desenfoque controlado. Perfecto para darle un toque de misterio a tus imágenes o para mejorar tus habilidades en procesamiento de imágenes.

## **Cómo Funciona**

1. **🕵️‍♂️ Cargar Imagen**: Se carga una imagen desde una ruta especificada en tu sistema.

2. **🔬 Aplicar Filtro Gaussiano**: Se aplica un filtro gaussiano para suavizar la imagen. Ajusta el valor de `sigma` para experimentar con el desenfoque.

3. **📊 Mostrar Resultados**: Se muestran la imagen original y la imagen suavizada en una ventana gráfica.

## **Código**

```python
import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt
from PIL import Image

# Ruta completa a la imagen en la carpeta Downloads
ruta_imagen = r'~\Downloads\ruta-de-tu-imagen.extension'

# Cargar la imagen
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
```
## Cómo Ejecutar el Código
1. **Instalar Dependencias**: Asegúrate de tener las siguientes bibliotecas instaladas:
  - `numpy`
  - `scipy`
  - `matplotlib`
  - `Pillow`

Instálalas con:
```bash
pip install numpy scipy matplotlib Pillow
```

2. 💾 **Guardar el Código**: Guarda el código en un archivo Python, por ejemplo, `filtro_gaussiano.py`.

3. ▶️ **Ejecutar el Script**: Corre el archivo Python para aplicar el filtro y ver el resultado:

## 📸 Ejemplo

<div align="center">
<img src="FiltroGaussiano.png"/>
</div>

### 💡 Nota
Este proyecto demuestra el procesamiento básico de imágenes. Puedes ajustar el parámetro sigma en el filtro gaussiano para experimentar con diferentes niveles de desenfoque y obtener el efecto deseado.

## 🤖 Autor
 - [h4ckxel](https://github.com/h4ckxel)

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CA1A5?style=for-the-badge&logo=scipy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-007ACC?style=for-the-badge&logo=matplotlib&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-EB0028?style=for-the-badge&logo=pillow&logoColor=white)

</div>

### 📜 Licencia
Este proyecto está licenciado bajo la [Licencia MIT](https://opensource.org/licenses/MIT).

