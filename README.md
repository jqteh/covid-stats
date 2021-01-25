# Notes
1. Use yarn instead of npm
```
$ npm install --global yarn
```
2. Make Flask directory a subdirectory of React 

## Flask instructions
1. If cloning, create own virtual environment and activate it
```
$ python3 -m venv venv
$ source venv/bin/activate
```
2. Install python dotenv + create environmental variable and set starting file path
```
$ pip install flask python-dotenv

inside .flaskenv
FLASK_APP=api.py
FLASK_ENV=development
```
3. Install flask and sklearn if not present
```
$ pip install flask sklearn
```
4. Run flask either with native command or via package.json
```
$ flask run
$ yarn start-api
```
