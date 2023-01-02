import uuid
import datetime

from app.main import db
from app.main.model.company import Company
from typing import Dict, Tuple


def save_company(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    company = Company.query.filter_by(company_name=data['company_name']).first()
    if not company:
        new_company = Company(
            company_id = str(uuid.uuid4()),
            class_name = data['class_name'],
            company_name = data['company_name'],
            language = data['language'],
            balance = data['balance'],
            created_at = datetime.datetime.utcnow(),
            updated_at = datetime.datetime.utcnow(),
        )
        save_changes(new_company)
        response_object = {
            'status': 'success',
            'message': 'Successfully Created Company.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Company already exists.',
        }
        return response_object, 409

def get_all_company():
    return Company.query.all()


def save_changes(data):
    db.session.add(data)
    db.session.commit()