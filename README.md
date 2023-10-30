# Shopping-Support

Shopping Support is the AI persona to answer your shopping queries as well as resolve
any queries you may have related to your shopping experience. This is a demo of how
Generative AI can reason and act on complex queries and demand of shopping users of a
e-commerce site.

## Project Setup

The project uses Django framework for a basic python webapp. Here is what you do after
checkout -

Setup and activate the virtual environment inside the project -
```
cd shopping-support
python3 -m venv .venv
source .venv/bin/activate
```

Inside the virtual env, upgrade pip and install Django framework -
```
python -m pip install --upgrade pip
python -m pip install django bs4 lxml requests openai langchain
```

Set the OpenAI API Key in your environment
```
export OPENAI_API_KEY="..."
```

Create the local SQL database to store model instances
```
python manage.py makemigrations
python manage.py migrate
```

Compile the models in the app and migrate to local SQL database. You need to do the following steps every time you change the models.py in your app -
```
python manage.py makemigrations support_app
python manage.py migrate support_app
```

Collect all the static contents in the app to serve separately -
```
python manage.py collectstatic
```

Start the web server on your desktop (default port 8000) -
```
python manage.py runserver
```

Now open te browser and enter `http://127.0.0.1:8000` and start testing. Happy coding!
