Task manager для работы со сделками 

Запуск сервера:

В терминале прописываем 

ssh mainadmin@84.***.1**.4*

Далее вводим пароль *** и попадаем на сервер 
Активируем zsh

sudo rm -rf /root/.oh-my-zsh

sudo sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

Активируем виртуальное окружение 

source env/bin/activate

Переходим в рабочую директорию 

cd code/django/App/taskmanager/

Чтобы запустить сайт прописываем 

python3 manage.py runserver 0.0.0.0:8000

Все! Сайт активен и доступен до адресу cpintern.site:8000