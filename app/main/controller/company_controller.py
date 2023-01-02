from flask import request
from flask_restplus import Resource, Api

from ..util.dto import CompanyDto
from ..service.company_service import save_company, get_all_company

api = CompanyDto.api
_company = CompanyDto.company


@api.route('/')
class CompanyList(Resource):
    @api.doc('list of companies')
    @api.marshal_list_with(_company, envelope='data')
    def get(self):
        """List all companies"""
        return get_all_company()

    @api.response(201, 'Comapny successfully created.')
    @api.doc('create a new company')
    @api.expect(_company, validate=True)
    def post(self):
        """Creates a new company """
        data = request.get_json()
        print("data")
        print(data)
        return save_company(data=data)

