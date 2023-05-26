# Precios_por_m2
Implementación de un modelo de aprendizaje automático para predecir el precio por m2 derivado de una serie de inmuebles con características geoespaciales y amenidades especificas.

Para lograr lo anterior se realizará los siguientes pasos:
1. Limpieza de la base de datos
2. Análisis exploratorio
3. Modelo lineal
4. Modelo Random Forrest
5. Otro modelo
6. Conclusiones
7. Herramientas utilizadas

# Primera parte: Limpieza de base
## 1. PowerQuery
- Se utilizó PowerQuery de Excel para revisar y transformar la base "reto_precios" inicial.
- La base inicial contaba con 35 columnas, de las cuales varias repetían información por lo que fueron eliminadas.
- Se dividió la columna "location" para obtener tres columnas: calle, colonia y estado; aunque aun presentan erroes por contener carateres especiales.
- Se eliminaron 16 columnas para quedar con 19 columnas.
- Todas las columnas se reemplazaron los valores "null" por ceros; como amenidades, número de pisos, entre otras.
- Las variables que se cree pueden ser de utilidad para el modelo predictivo son las características del inmueble: "m2" (metros cuadrados del inmueble), "num_bedrooms" (número de dormitorios), "bathrooms" (número de baños), "amenities" (amenidades disponibles), "parking_lots (lugares de estacionamiento incluido), "disposition" (fente del departamento), "num_floors" ( ubicación del piso donde se encuentra el departamento), y **"price_square_meter"(precio por metro cuadrado) que será la variable dependiente**

![image](https://github.com/Alelopez383/Precios_por_m2/assets/43974872/c5ca029d-9c89-4b0c-97e0-779ab245d4fa)


## 2. Python + Jupyter Notebook
- Para iniciar el análisis exploratorio de las variables, se utilizó Python a través de Jupyter Notebook
- La base transformada "reto_precios_v1" cuenta con 19 columnas y 981 observaciones.

![image](https://github.com/Alelopez383/Precios_por_m2/assets/43974872/f087da65-6e47-465e-95ae-dd6989d56e7a)

# Segunda parte: 
