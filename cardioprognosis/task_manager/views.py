import os
import pandas as pd
from django.shortcuts import render
from .models import Task
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib


def task_list(request):
    tasks = Task.objects.all()

    # Определение пути к файлу heartdata.csv
    csv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(file))), 'cardioprognosis', 'heartdata.csv')

    # Загрузка данных из файла heartdata.csv
    data = pd.read_csv(csv_path)

    # Предобработка данных
    X = data.drop('target', axis=1)
    y = data['target']

    # Разделение данных на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Масштабирование данных
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Загрузка модели из файла
    model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'task2_heart_deseases.model_consistent_V1.0')
    model = joblib.load(model_path)

    # Предсказание на тестовой выборке
    y_pred = model.predict(X_test_scaled)

    # Оценка точности модели
    accuracy = model.score(X_test_scaled, y_test)

    context = {
        'tasks': tasks,
        'accuracy': accuracy,
        # Другие контекстные переменные, которые вам могут понадобиться
    }
    return render(request, 'task_manager/task_list.html', context)