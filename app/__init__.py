from flask_restplus import Api
from flask import Blueprint

from .main.controller.company_controller import api as comapny_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='DNL company API',
          version='1.0',
          description='Company APIs'
          )

api.add_namespace(comapny_ns, path='/company')