from app import ma
from app.models import Company


class CompanySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Company

    id = ma.Int(dump_only=True)
    created = ma.DateTime(dump_only=True)
    slug = ma.Str()
    is_active = ma.Boolean()
