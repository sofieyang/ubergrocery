#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import *
import os

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    return render_template('pages/pickedforyou.html')
    #return render_template('pages/placeholder.home.html')

@app.route('/pickedforyou')
def pickedforyou():
    return render_template('pages/pickedforyou.html')
    #return render_template('pages/placeholder.home.html')

@app.route('/recipe-carousel')
def recipe_carousel():
    #should still have the individual recipes below it
    return render_template('pages/recipe-carousel.html')
    #return render_template('pages/placeholder.home.html')

@app.route('/recipe-expanded') #this is where you see all the ingredients
def recipe_expanded():
    #has 
    return render_template('pages/recipe-expanded.html')
    #return render_template('pages/placeholder.home.html')

@app.route('/recipe-instructions') #how do we get a pop-up that can be dismissed
def recipe_instructions():
    return render_template('pages/recipe-instructions.html')
    #return render_template('pages/placeholder.home.html')

@app.route('/cart')
def cart():
    return render_template('pages/cart.html')
    #return render_template('pages/placeholder.home.html')

@app.route('/cart-salmon')
def cart_salmon():
    return render_template('pages/cart-salmon.html')
    #return render_template('pages/placeholder.home.html')

@app.route('/cart-salmon-burger')
def cart_salmon_burger():
    return render_template('pages/cart-salmon-burger.html')
    #return render_template('pages/placeholder.home.html')

@app.route('/order-placed')
def order_placed():
    return render_template('pages/order-placed.html')
    #return render_template('pages/placeholder.home.html')

@app.route('/merchant-home')
def merchant_home():
    return render_template('pages/merchant-home.html')

@app.route('/merchant-home-salmon')
def merchant_home_salmon():
    return render_template('pages/merchant-home-salmon.html')


# @app.route('/about')
# def about():
#     return render_template('pages/placeholder.about.html')


@app.route('/login')
def login():
    form = LoginForm(request.form)
    return render_template('forms/login.html', form=form)


@app.route('/register')
def register():
    form = RegisterForm(request.form)
    return render_template('forms/register.html', form=form)


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)

# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
