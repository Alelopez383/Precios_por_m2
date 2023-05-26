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

* Diagramas de dispersión

![image](https://github.com/Alelopez383/Precios_por_m2/assets/43974872/791036b4-4faf-4ba3-8f4d-e44615491536)

* Histogramas

![image](https://github.com/Alelopez383/Precios_por_m2/assets/43974872/cf8b565f-c0ae-4c83-9ba5-e367a07f8452)

*Buscando posibles relaciones
















