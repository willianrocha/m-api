# Marvel API
Simple Django APP for requesting some information from Marvel API

## How to run it

```shell
  git clone https://github.com/willianrocha/m-api.git
  cd m-api
  virtualenv -p python3 ENV
  source ENV/bin/activate
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py runserver
```

## The comics APP

### Index
The app comics presents a simple form to receive the character's name to search.  After a search is issued, a list of characters is shown, where the user might select the characters of interest.

<!-- The Marvel API only allow to search for the full name of a string the begins the name. -->

### Character

The character pages show its image, a short bio and a list of comics related to the character.

### Comics

The comics page shows the issues' cover, a short description and the characters involved.
