from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd


# Cargar el modelo entrenado
model= joblib.load('modelo.pkl')

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Definir la ruta de inicio
@app.route('/')
def home():
    return render_template('index.html')

# Definir la ruta para procesar los datos ingresados por el usuario
@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los datos ingresados por el usuario
    feature1 = request.form.get('days_on_site')
    feature2 = request.form.get('bathrooms')
    feature3 = request.form.get('num_floors')
    feature4 = request.form.get('monthly_fee_mxn')
    feature5 = request.form.get('parking_lots')
    feature6 = request.form.get('beds')
    feature7 = request.form.get('m2')
    feature8 = request.form.get('final_price')

   # Crear una lista con los valores de entrada
    input_data = [feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8]  

   # Convertir los valores de entrada a un arreglo numpy
    input_array = np.array(input_data).reshape(1, -1)

    # Realizar la predicción utilizando el modelo
    prediction = model.predict(input_array)

    # Renderizar la plantilla de resultados y mostrar la predicción
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)