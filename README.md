# Notes
## General
* Use yarn instead of npm
```
$ npm install --global yarn
```
* Make Flask directory a subdirectory of React 

## Flask instructions
1. If cloning, create own virtual environment and activate it
```
$ cd back-end
$ python3 -m venv venv
$ source venv/bin/activate
```
2. (If absent) Install python dotenv + create environmental variable and set starting file path
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

## React instructions
1. Install node.js (LTS) at https://nodejs.org/en/
2. Install node dependencies in root directory (where package.json is)
```
$ npm install
```
3. Run React app
```
$ yarn start
```