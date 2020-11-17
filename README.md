# LesJardinsDeSabine
Site dynamique django basé sur le modele bootstrap agency

```
python -m venv ./venv

venv\Scripts\activate
# OU
source venv/bin/activate

pip install -r requirements.txt

sudo apt-get update && sudo apt-get install python3-pip
pip install uwsgi


# python -m pip install Django
python
	>>> import django
	>>> print(django.get_version())
	3.1
	>>> exit()
# ou
python -m django --version
3.1.3
django-admin startproject LJDS


# test du server
python manage.py runserver

#download boostrap project
git clone git@github.com:StartBootstrap/startbootstrap-agency.git static
# modifier le fichier d'index et modifier les variables avec le commandes de template 
mkdir LDJS/template

Ajouter :
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]TEMPLATES = [
    {
    ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
    ...
    }

```
git clone  <this repo>
	
````
echo aa >  /var/log/uwsgi/LJDS.log
sudo chmod 777  /var/log/uwsgi/
echo aa >  /var/log/uwsgi/LJDS.log
uwsgi --ini uwsgi.ini
sudo mkdir /var/www/dir
sudo chmod 777  /var/www/dir

 uwsgi --ini uwsgi.ini --socket /var/www/dir/uwsgi.sock
````
* branchement webhook discord 
