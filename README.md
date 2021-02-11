# CashTracker-API
CashTracker's web API so you can track where your money is going

__Python version:__ 3.8.6

## Setting up

### Python
intall pyenv for managing multiple versions of python
```
brew install pyenv
```

install python 3.8.6
```
pyenv install 3.8.6
```

python -m venv [dirname] --prompt [label]
```
python -m venv venv --prompt cashtrack
```

activate virtual environment macOS
```
source venv/bin/activate
```

activate virtual environment Windows
```
venv\Scripts\activate
```

install project dependencies
```
pip install -r requirements.txt
```

### Cashtrack database
This project uses a **Postgres** database, so it must be installed

create cashtrack database
```
createdb cashtrack
```

migrate database
```
python manage.py migrate
```
### Populate database
Before running the server, the database must have some values in it. To do so run the command 
```
python manage.py loaddata categories.json
```

### Run the project
```
python manage.py runserver
```

### Environment variables
This project needs a **.env** file located in **cashstrack/apps/**
You can look on **.env.example** what variables you'll need to run the project
