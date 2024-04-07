from app import create_app
import datetime
from flask import session, redirect, url_for, flash
from flask_login import logout_user

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)