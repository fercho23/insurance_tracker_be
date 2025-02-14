from app import ma
from app.models import DataProcessed

class DataProcessedSchema(ma.SQLAlchemySchema):
    class Meta:
        model = DataProcessed

    id = ma.Int(dump_only=True)
    created = ma.DateTime(dump_only=True)
    processed_data = ma.Dict()
    company = ma.Nested('CompanySchema', only=['id', 'slug'])