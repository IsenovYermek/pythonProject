# название проекта (project name): cardioprognosis

Краткое описание проекта (The brief description of the project.):
Проект "Прогноз сердечной недостаточности" представляет собой систему, основанную на машинном обучении,
которая позволяет предсказывать наличие или отсутствие сердечной недостаточности у пациента на основе
нескольких входных параметров, таких как возраст, пол, боли в груди и уровень холестерина.
(The project "Heart Failure Prediction" is a machine learning-based system that predicts the presence or absence
of heart failure in a patient based on several input parameters, such as age, gender, chest pain, 
and cholesterol level.)

## Установка (Installation)

1. Склонируйте репозиторий (Clone the repository):

   
bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   


2. Создайте и активируйте виртуальное окружение (Create and activate a virtual environment.):

   
bash
   python3 -m venv myvenv
   source myvenv/bin/activate
   


3. Установите зависимости (Install dependencies.):

   
bash
   pip install -r requirements.txt
   


## Использование (Using)
1. Запустите Django сервер (Start Django server):
bash
   python manage.py runserver
2. Откройте веб-браузер и перейдите по адресу (Open your web browser and navigate to)[http://localhost:8000/tasks/](http://localhost:8000/tasks/)
3. Взаимодействуйте со страницей приложения для предсказания сердечной недостаточности (Using our web application, you can interact with the page to predict heart failure.)

## Структура проекта (Project structure)

- task_manager/ - приложение Django для управления задачами и предсказаний сердечной недостаточности.
  (A Django application for managing tasks and predicting heart failure.)
- cardioprognosis/ - папка с данными, содержащая файл heartdata.csv с тренировочными данными.
  (data folder containing heartdata.csv file with training data)
- task2_heart_deseases.model_consistent_V1.0 - файл с обученной моделью для предсказания сердечной недостаточности.
  (trained model file for predicting heart failure.)
- requirements.txt - список зависимостей проекта. (trained model file for predicting heart failure.)

