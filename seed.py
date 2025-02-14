from app import app
from app import db
from app.models import Company

if __name__ == "__main__":
    """Pre-Populate Database"""

    with app.app_context():
        # Companies
        if Company.query.first() is None:
            slugs = ["dupixent"]
            for slug in slugs:
                obj = Company(
                    slug=slug,
                    ai_resource="claude",
                    is_active=True,
                )
                db.session.add(obj)
            db.session.commit()
