# Precios por metro cuadrado en el sector inmobiliario
Implementación de un modelo de aprendizaje automático para predecir el precio por m2 derivado de una serie de inmuebles con características geoespaciales y amenidades especificas.

Para lograr lo anterior se realizará los siguientes pasos:
1. Limpieza de la base de datos
2. Análisis exploratorio
3. Modelo lineal
4. Modelo Random Forrest
5. Otro modelo
6. Conclusiones
7. Herramientas utilizadas


## 1. Limpieza de la base de datos usando PowerQuery
- Se utilizó PowerQuery de Excel para revisar y transformar la base "reto_precios" inicial.
- PowerQuery tiene la capacidad de guardar los pasos de transformación para futuras actualizaciónes u otras bases.
- La base inicial contaba con 35 columnas, de las cuales varias repetían información por lo que fueron eliminadas.
- La columna"disposition" contaba únicamente con 20 observaciones, por lo que se eliminó.
- Se dividió la columna "location" para obtener tres columnas: calle, colonia y estado; aunque aun presentan erroes por contener carateres especiales.
- En total se eliminaron 17 columnas para quedar con 18 columnas.
- Todas las columnas se reemplazaron los valores "null" por ceros: amenidades, número de pisos, entre otras.
- Las variables que se cree pueden ser de utilidad para el modelo predictivo son las características del inmueble: "m2" (metros cuadrados del inmueble), "num_bedrooms" (número de dormitorios), "bathrooms" (número de baños), "amenities" (amenidades disponibles), "parking_lots (lugares de estacionamiento incluido), "disposition" (fente del departamento), "num_floors" ( ubicación del piso donde se encuentra el departamento), y **"price_square_meter"(precio por metro cuadrado) que será la variable dependiente**

![image](https://github.com/Alelopez383/Precios_por_m2/assets/43974872/c5ca029d-9c89-4b0c-97e0-779ab245d4fa)


## 2. Análisis exploratorio usando Python + Jupyter Notebook
- Para iniciar el análisis exploratorio de las variables, se utilizó Python a través de Jupyter Notebook
- La base transformada "reto_precios_v1" cuenta con 19 columnas y 981 observaciones.
- 

![image](https://github.com/Alelopez383/Precios_por_m2/assets/43974872/5dc29818-2a38-44a3-8560-7ce44dc1381b)

* Descriptivos:

![image](https://github.com/Alelopez383/Precios_por_m2/assets/43974872/094e4595-41f1-4dfd-b0f7-f15cb96d0815)


* Box Plot Número de baños, posibles outliers

![image](https://github.com/Alelopez383/Precios_por_m2/assets/43974872/c65bd2ea-36e8-4a43-b040-7dc4725797a4)

* Box plot para cuota mensual de mantenimiento, posibles outliers

![image](https://github.com/Alelopez383/Precios_por_m2/assets/43974872/84bbd8a7-865c-4b06-9ff1-31bbc7b2dde5)

* Box plot para precio final, posibles outliers

![image](https://github.com/Alelopez383/Precios_por_m2/assets/43974872/fbd76ca0-90aa-4c8b-8159-f57b803c497d)

## Derivado de lo anterior, se busca eliminar los outliers basado en la desviación estándar:

* Diagramas de dispersión

![image](https://github.com/Alelopez383/Precios_por_m2/assets/43974872/791036b4-4faf-4ba3-8f4d-e44615491536)

* Histogramas

![image](https://github.com/Alelopez383/Precios_por_m2/assets/43974872/cf8b565f-c0ae-4c83-9ba5-e367a07f8452)

*Buscando posibles relaciones

* Matriz de correlación

![image](https://github.com/Alelopez383/Precios_por_m2/assets/43974872/261f77e8-fe4b-4727-b525-78e9c3662185)


# Flujo de MLOps

1. Recolección y preparación de datos: Se recopilan y preparan los datos necesarios para entrenar y evaluar el modelo. Esto implica la limpieza de datos, la selección de características relevantes y la división del conjunto de datos en conjuntos de entrenamiento, validación y prueba.

2. Desarrollo y entrenamiento del modelo: Se desarrolla y entrena el modelo utilizando el conjunto de datos de entrenamiento. Se exploran diferentes algoritmos y técnicas de modelado para encontrar el enfoque más efectivo.

3. Validación y evaluación del modelo: Se evalúa el modelo utilizando el conjunto de datos de validación para medir su rendimiento. Se calculan métricas de evaluación para determinar la calidad del modelo.

4. Implementación del modelo: Una vez que el modelo ha sido validado, se implementa en un entorno de producción.

5. Monitoreo del modelo: Se establecen métricas y umbrales para monitorear el rendimiento del modelo.

6. Actualización y reentrenamiento del modelo

7. Despliegue continuo: Se automatiza el proceso de implementación y actualización del modelo.














