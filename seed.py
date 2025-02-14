from app import app, db
from app.models import Company


if __name__ == '__main__':
    """Pre-Populate Database"""

    with app.app_context():
        # Companies
        if Company.query.first() is None:
            slugs = ['dupixent']
            for slug in slugs:
                obj = Company(
                    slug=slug,
                    is_active=True,
                )
                db.session.add(obj)
            db.session.commit()