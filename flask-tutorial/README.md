# Flask tutorial

The [Flask][100] documentation contains a [tutorial][110] for a
simple blog example.

[100]: https://flask.palletsprojects.com/en/3.0.x/

[110]: https://flask.palletsprojects.com/en/3.0.x/tutorial/

## Run the flaskr application

1. Initialize the database for the Flaskr application

```
make flaskr-init-db
```

2. Run the application

```
make flaskr-run
```

3. Open a web browser at http://localhost:5000/

4. Register a new user by clicking on "Register"

5. Log in with the registerd using the "Log in" option

6. Try create/edit/delete of a blog post.

## Build the flaskr application

1. Build the flaskr app using poetry
poetry build

2. A `flaskr*.whl` file is created in the dist directory

## Use the whl file

On WSL it can take 10 times as long to create a virtual environment (venv) on a shared folder as compared to a WSL folder.

1. Create a venv on a WSL folder

```
mkdir ~/ws/venv
```

2. Create a link from a `.venv` project folder to the WSL folder

```
ln -s ~/ws/venv .venv
```

3. Change to the venv directory

```
cd .venv
```

4. Create a virtual environment

```
python -m venv .
```

5. Exit the venv directory

```
cd ..
```

6. Activate the venv

```
source .venv/bin/activate
```

7. Install the whl file

```
pip install dist/flaskr*.whl
```

8. Run the flaskr app

```
flask --app flaskr run
```

9. Exit the venv (declare -F | grep deactivate)

```
deactivate
```
