from flask import Flask 
from .blueprints.site.routes import site 

#instantiating our Flask app
app = Flask(__name__) #passing in the __name__ variable which just takes the name of the folder we're in
app.register_blueprint(site)


