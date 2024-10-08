## Инструкция к созданию телеграм бота с поддержкой docker
# 1. Создать виртуальное окружение
- создать папку, в которой будет проект
- перейти в редактор кода и открыть созданную папку
- создать виртуальное окружение через терминал
python3 -v venv venv

- активировать окружение
source venv/bin/activate

- проверить пип3
- <span style="color: blue">pip list</span>

- обновить пип3
pip3 install —upgrade pip

- устанавливаем библоиотеку aiogram
pip3 install aiogram

- фриз библиотек, которые сейчас используются и перенос их в файл requirements
pip3 freeze >> requirements.txt

# 2. Cоздать Докер образ
- создаем файл с именем dockerfile  и записываем в него следующую структур

- Используем базовый образ Python
FROM python:3.9-slim

- Устанавливаем рабочую директорию
WORKDIR /app

- Копируем содержимое проекта
COPY . .

- Устанавливаем зависимости
RUN pip install -r requirements.txt

- Запускаем приложение
CMD ["python", "main.py"]

## 3. Активируем докер и проверяем работу тг-бота
- создаем Образ
docker build .

- запускаем Докер-контейнер
docker run -d -p 5000:5000 IMAGE_ID
(вместо 5000:5000 может быть другой порт)

- после запуска выдается ID контейнера (длинная строка)
- проверка, какие контейнеры сейчас запущены
docker ps

- переходим в телеграм и проверяем возвращается ли транслитерация на латиницу
