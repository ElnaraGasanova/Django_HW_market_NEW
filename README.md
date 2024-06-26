## Домашняя работа по теме 20.1 "Работа с ORM в Django". НОВАЯ ВЕРСИЯ!
#### Предыдущая версия была "утеряна" в момент создания users и отката миграций. Посмотреть можно по ссылке:
```commandline
https://github.com/ElnaraGasanova/Django_HW_20.1.git
```
Приложение Продуктовый магазин по работе с Категориями, Товаром, Версиями
и Пользователями. А так же Публикациями.
В приложении можно создать/изменить/удалить Категории, Товары и Публикации,
вся информация сохраняется в БД PostgreSQL.

### Используемые технологии:
* Python
* Django
* PostgerSQL 

#### Параметры по работе в БД с Категориями товаров:
* Наименование
* Описание
#### Параметры по работе в БД с Товаром:
* Наименование
* Описание
* Изображение
* Категория
* Цена за покупку
* Дата создания (записи в БД)
* Дата последнего изменения (записи в БД)
* Пользователь, создавший продукт в БД
#### Параметры по работе в БД с Публикациями:
* Заголовок
* Содержимое публикации
* Дата создания
* Дата публикации
* Счетчик просмотров
#### Параметры по работе в БД с Версиями:
* Наименование товара
* Номер версии
* Наименование версии
* Признак версии (действующая/не действующая)

### ИНСТРУКЦИЯ ПО РАЗВЕРТЫВАНИЮ
* Сделайте Fork этого репозитория. Репозиторий появится
в личных репозиториях на GitHub:
```
https://github.com/ElnaraGasanova/Django_HW_market_NEW.git
```
* Сделайте git clone форкнутого репозитория, чтобы получить
репозиторий локально:
```
git clone https://github.com
```
* Создайте виртуальное окружение и активируйте его:
```
python -m venv venv
venv\Scripts\activate
```
p.s. Для выхода из виртуального окружения и возврата к глобальному
окружению Python введите следующую команду:
```
deactivate
```
* Для установки всех библиотек выполните команду:
```
pip install -r requirements.txt
```
* Для соединения с pgAdmin внесите информацию о пароле в config/settings.py в 
разделе DATABASES = ...

* Приложение работает следующим образом, для соединения с сервером,
необходимо в терминале PyCharm ввести команду:
```
python manage.py runserver
```
и перейти по ссылке для дальнейшей работы
```
http://127.0.0.1:8000/admin/
```
### Автор проекта :)
```
https://github.com/ElnaraGasanova
```