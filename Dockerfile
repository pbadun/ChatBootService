# Используем базовый образ Python
FROM python:3.9
# Устанавливаем зависимости
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
# Копируем исходный код в контейнер
COPY . /app
# Указываем рабочую директорию
WORKDIR /app
# Запускаем микросервис
CMD ["python", "main.py"]