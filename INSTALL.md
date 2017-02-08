## Project Setup

### Create a new virtual environment.
```
virtualenv ve
. ve/bin/activate
```

### Install python requirements
```
`pip install -r requirements.txt`
```

### Install NPM dependencies
```
cd ngApp/
npm install
```

### Compile SCSS files
In the `./ngApp/` folder :
```
gulp sass
```

### Start npm / Launch the app
In the `./ngApp/` folder :
```
npm start
```

### Run Django Development Server
NB : Open a new terminal window
```
cd ../
python manage.py runserver
```

Though we use django server npm should be running behind to compile typescript to javascript instantly.