from .. import db

class Company(db.Model):
    __tablename__ = "company"

    company_id = db.Column(db.String(255), primary_key=True)
    class_name = db.Column(db.String(255))
    company_name = db.Column(db.String(255), unique=True, nullable=False)
    language = db.Column(db.String(255))
    balance = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Company '{}'>".format(self.company_name)