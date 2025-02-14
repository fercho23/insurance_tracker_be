# tests/unit/helpers/test_data_processor.py
import pytest
from app.helpers.DataProcessor import DataProcessor
from app.helpers.GenerativeAIManager import ResourceInterface


class TestDataProcessor:
    """Test the DataProcessor class."""

    @pytest.fixture
    def data(self):
        return {"key": "value"}

    def test_create_by_company(self, company, data):
        data_processor = DataProcessor.create_by_company(data, company)
        assert isinstance(data_processor, DataProcessor)
        assert data_processor._data == data
        assert isinstance(data_processor._ai_resource, ResourceInterface)

    def test_process(self, company, data):
        data_processor = DataProcessor(data)
        processed_data = data_processor.process()
        assert isinstance(processed_data, dict)
        assert processed_data == data_processor._processed_data
