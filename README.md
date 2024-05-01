Installing "Bookstore" project on Linux.

git clone git@github.com:ppenkovskiy/bookstore.git

cd bookstore

sudo apt install python3.10-venv

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
