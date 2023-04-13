# Django_movie
<blockquote>Интернет-издание о кинематографе написанный на Django</blockquote>
<blockquote>Pet-проект. Создается в целях более лучшего изучения Django</blockquote>
<img src="https://raw.githubusercontent.com/BgPyt/Django_movie/master/ScreenShot_20230412174107.png">

# 🔧Запуск проекта
<ol>Для локального запуска выполните следующие действия:
<br>
<br>
<li>Клонирование репозитория -
<p><code>git clone https://github.com/BgPyt/Django_movie.git</code></li>
<br>
<li>Устанавливаем зависимости проекта -
<p><code>pip install -r requirements.txt</code></li>
<br>
<li>Привязка к базе данных (Рекомендуется Postgresql). Ознакомиться можно <a href="https://docs.djangoproject.com/en/4.1/ref/databases/">тут</a>
<p><code>Директория movie/setting.py и находим константу DATABASES и вместо *** подставить свои параметры.<p>Перед этим создать БД при помощи sql - " CREATE DATABASE <dbname> CHARACTER SET utf8; " </code> <p>Если у вас <strong>Postgresql</strong> установить драйвер <code>pip install psycopg2</code></li>
<li>Выполняем миграции в бд -
<p><code>python manage.py makemigrations
<p>python manage.py migrate</code></li>
<br>
<li>Coздание клиента с полномочиями администратора -
<p><code>python manage.py createsuperuser</code></li>
<br>
<li>Запуск сервера -
<p><code>python manage.py runserver</code></li>
<br>
</ol>

