# CRM-website


> Website for registrate companies/organizations/etc deployed on free hosting [here](https://my-grand-site-countinue.herokuapp.com/).

## Getting Started

First of all, clone the repo:

```bash
git clone https://github.com/Pavlo-Olshansky/CRM-website.git
```

## Dependencies
* `django 1.11.1` and `python3`.

## Installing & running
### Dev mode
```
virtualenv venv --no-site-packages
venv/Scripts/activate
pip install -r requirements.txt
```
Then configure your database:
```
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```
*Now you can check server at [localhost:8000](http://localhost:8000)*

**Attention : You must run all of these commands in administrator mode**.

## Important note
All env variables are configured as system variable by command `setx var_name var_value`.
#### Example
`setx ENV_ROLE development`

