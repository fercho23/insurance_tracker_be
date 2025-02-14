import pytest
from app.models import Company


@pytest.fixture
def company():
    obj = Company(
        slug="test-company",
        ai_resource="claude",
        is_active=True,
    )
    yield obj
