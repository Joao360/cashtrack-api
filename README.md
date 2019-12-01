# CashTracker-API
CashTracker's web API so you can track where your money is going

__Python version:__ 3.7.4

## Setting up

### Python
intall pyenv for managing multiple versions of python

    brew install pyenv

install python 3.7.4

    pyenv install 3.7.4

python -m venv [dirname] --prompt [label]

    python -m venv venv --prompt cashtrack

activate virtual environment macOS

    source venv/bin/activate

activate virtual environment Windows

    venv\Scripts\activate

install project dependencies

    pip install -r requirements.txt

### Cashtrack database
This project uses a `Postgres` database, so it must be installed

create cashtrack database

    createdb cashtrack

`Postgres` must have this user
```
Username: joaograca
Password: 123
```

migrate database

    python manage.py migrate

### Run the project
    python manage.py runserver
