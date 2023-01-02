from flask_restplus import Namespace, fields

class CompanyDto:
    api = Namespace('company', description='Company api')
    company = api.model('company', {
        'company_name': fields.String(attributes= "company_name",required=True, description='company name'),
        'class_name': fields.String(required=True, description='company class name'),
        'language': fields.String(required=True, description='language'),
        'balance': fields.String(required=True, description='balance'),
    })