Project "Bookstore" preview:

https://drive.google.com/file/d/1VAqzWRWEZHfyaYX9ugoldgvn80lv0pf3/view?usp=sharing

Installing "Bookstore" project on Linux:

git clone git@github.com:ppenkovskiy/bookstore_app.git

cd bookstore_app

sudo apt install python3.10-venv

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
