import os
import pandas as pd
from django.shortcuts import render
from .models import Task
from sklearn.preprocessing import StandardScaler
import joblib


def task_list(request):
    tasks = Task.objects.all()

    # Загрузка данных из файла heartdata.csv
    data = pd.read_csv(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'cardioprognosis', 'heartdata.csv'))

    # Масштабирование данных
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    # Загрузка модели из файла
    model = joblib.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'cardioprognosis', 'task2_heart_deseasses.model_consistent_v1.0'))

    # Предсказание на данных
    y_pred = model.predict(data_scaled)

    context = {
        'tasks': tasks,
        'predictions': y_pred,
    }
    return render(request, 'task_manager/task_list.html', context)