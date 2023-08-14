import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

# Ввод данных
age = float(input("Введите значение age: "))
sex = float(input("Введите значение sex: "))
cp = float(input("Введите значение cp: "))
trestbps = float(input("Введите значение trestbps: "))
chol = float(input("Введите значение chol: "))
fbs = float(input("Введите значение fbs: "))
restecg = float(input("Введите значение restecg: "))
thalach = float(input("Введите значение thalach: "))
exang = float(input("Введите значение exang: "))
oldpeak = float(input("Введите значение oldpeak: "))
slope = float(input("Введите значение slope: "))
ca = float(input("Введите значение ca: "))
thal = float(input("Введите значение thal: "))
target = 0  # Значение целевой переменной, для которой вы хотите получить предсказание

# Создание DataFrame с введенными данными
data = pd.DataFrame({
    'age': [age],
    'sex': [sex],
    'cp': [cp],
    'trestbps': [trestbps],
    'chol': [chol],
    'fbs': [fbs],
    'restecg': [restecg],
    'thalach': [thalach],
    'exang': [exang],
    'oldpeak': [oldpeak],
    'slope': [slope],
    'ca': [ca],
    'thal': [thal],
    'target': [target]
})

# Масштабирование данных
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Загрузка модели из файла
model_path = os.path.join(os.path.dirname(__file__), 'task2_heart_deseases.model_consistent_v1.0')
model = joblib.load(model_path)

# Проверка, является ли загруженный объект модели моделью
if hasattr(model, 'predict'):
    print("Модель успешно загружена")

    # Предсказание на данных
    y_pred = model.predict(data_scaled)

    # Проверка типа данных предсказаний
    if isinstance(y_pred, int):
        # Преобразование в тип float
        y_pred = float(y_pred)

    # Вывод предсказаний
    for i, pred in enumerate(y_pred):
        print(f"Sample {i + 1}: {pred}")

# Сохранение предсказаний в файл
output_file = "predictions.csv"
predictions = pd.DataFrame({"target": y_pred})
predictions.to_csv(output_file, index=False)
print(f"Предсказания сохранены в файл: {output_file}")