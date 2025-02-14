from app import db
from .fields import JsonField

class DataProcessed(db.Model):
    __tablename__ = "data_processed"

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    original_data = db.Column(JsonField, default={})
    processed_data = db.Column(JsonField, default={})
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))

    def __repr__(self):
        return f"<DataProcessed {self.id}>"