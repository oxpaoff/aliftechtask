## Инструкция

#### 1) Установить зависимости
	pip install -r requirements.txt

#### 2) Запустить файл main.ipynb из папки ml для создания модели
	jupyter nbconvert --to notebook --inplace --execute ml/main.ipynb

#### 3) В файле docker-compose.yml заполнить данные для подключения к Postgresql

#### 4) Поднять докер контейнер

	docker-compose up --build
                                                    
#### 5) Перейти по адресу http://0.0.0.0:8000/, убедиться что всё работает


