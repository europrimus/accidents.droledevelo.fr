# stats from official data

## data source
 - [Bases de données annuelles des accidents corporels de la circulation routière - Années de 2005 à 2021](https://www.data.gouv.fr/fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2021/)
 - [Description des bases de données annuelles des accidents corporels de a circulation routière Années de 2005 à 2021](file:///home/didier/T%C3%A9l%C3%A9chargements/description-des-bases-de-donnees-annuelles-2021.pdf)

## setup
### Python virtual environement
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### database
create file ```~/.pgpass``` with content :
```
localhost:5432:NAME:USER:PASSWORD
```
and ```~/.pg_service.conf```  with content :
```
[pgsql_django_stats_accidents_service]
host=localhost
user=USER
dbname=NAME
port=5432
```
remember to change your user name, password and database.

then
```
python manage.py migrate
```

### dev
```
python manage.py runserver
```

## Usage
### Update data
Data could be parsed from data.gouv.fr with this command (run in virtual environement)
```
./manage.py updateData data.gouv.fr
```
