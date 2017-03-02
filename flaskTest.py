
# imports list
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# configuration
DATABASE = '/tmp/flaskTest.db'
# imports list
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# configuration
DATABASE = '/tmp/flaskTest.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
# imports list
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# configuration
DATABASE = '/tmp/flaskTest.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our application
app = Flask(__name__)
app.config.from_object(__name__)
print(__name__)

# imports list
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# configuration
DATABASE = '/tmp/flaskTest.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our application
app = Flask(__name__)
app.config.from_object(__name__)
print(__name__)

# db connection
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

# run server
if __name__ == '__main__' :
    app.run()
# imports list
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# configuration
DATABASE = '/tmp/flaskTest.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our application
app = Flask(__name__)
app.config.from_object(__name__)

# db connection
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

# run server
if __name__ == '__main__' :
    app.run()