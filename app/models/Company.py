from app import db


class Company(db.Model):
    __tablename__ = "company"

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    slug = db.Column(db.String(255))
    ai_resource = db.Column(db.String(255), nullable=False, server_default="claude")
    is_active = db.Column(db.Boolean, default=False)
    data_processed = db.relationship("DataProcessed", backref="company")

    def __repr__(self):
        return f"<Company {self.id}>"
