# diplom_project

# Для развертывания проекта сделайте следующее:
# Установите виртуальное окружение
py -m venv env

# Далее активируйте ее

.\env\Scripts\activate

# Затем пропишите ссылку с гитхаба
git clone "https://github.com/DaniilTishkin2001/diplom_project.git"

# Затем перейдите в папку site
# cd site

Перетащите файл requirements.txt в папку diplom_project
# Установите зависимости

pip install -r requirements.txt

# Произведите миграции

python manage.py migrate

# Запустите сервер

python manage.py runserver
