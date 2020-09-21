# GP Favorite Products

#### Prerequisites::
- Python 3.8 and PyPI
- Postgres Database

## Install with virtualenv
- Download the source code for this repository
```bash
git clone git@github.com:gilsonbp/gp-favorite-products.git
```

- Create a new VirtualEnv:
> Access the project folder and execute the command below:
```bash
python -m venv .venv
```

- Switch to the virtual environment before installing the project dependencies:
```bash
source .venv/bin/activate
```

- Install dependencies:
```bash
pip install -r requirements.txt
```
- Copy the local.env file to .env and set up the connection to the database and enter a secret_key:
```bash
cp local.env .env
```

- Execute the migrations:
```bash
python manage.py migrate 
```

- Execute tests
```bash
./tests.sh
```

- Start server:
```bash
python manage.py runserver 
```
Access the API documentation at http://127.0.0.1:8000/swagger/
