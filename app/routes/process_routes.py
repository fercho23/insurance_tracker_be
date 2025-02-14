import json
from app import app, db, logger
from app.models import Company, DataProcessed
from app.helpers import DataProcessor, GenerativeAIConstructor
from flask import request, jsonify
from flask_cors import cross_origin
import datetime

@app.route('/api/process/<company_slug>', methods=['POST'])
@cross_origin()
def api_process(company_slug: str):
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        company = Company.query.filter_by(slug=company_slug).first()
        if not company:
            return jsonify({'error': 'Company not found'}), 404

        logger.info(f"Received request data.")

        file_contents = file.read()
        data = json.loads(file_contents)

        ai_resource = GenerativeAIConstructor.get_resource("claude")
        data_processor = DataProcessor(data, ai_resource)
        processed_data = data_processor.process()

        data_processed = DataProcessed(
            original_data=data,
            processed_data=processed_data,
            company=company
        )
        db.session.add(data_processed)
        db.session.commit()

        return jsonify({
            "status": "success",
            "message": "Data processed successfully",
        }), 200
    except json.JSONDecodeError as e:
        return jsonify({'error': 'Invalid JSON File'}), 400
    except Exception as e:
        # import traceback
        # logger.error(traceback.format_exc())
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500