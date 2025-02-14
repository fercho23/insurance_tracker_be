from app import app, logger
from app.models import DataProcessed
from flask import request, jsonify
from flask_cors import cross_origin

from flask import request


@app.route('/api/data_processed', methods=['GET'])
@cross_origin()
def api_data_processed():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)

        logger.info(f"Received request data.")

        data_processed = DataProcessed.query.paginate(page=page, per_page=per_page)

        if data_processed is None:
            return jsonify({'error': 'No data found'}), 404

        results = [
            {
                "created": data.created,
                "processed_data": data.processed_data,
                "company": {
                    "id": data.company.id,
                    "slug": data.company.slug,
                }
            } for data in data_processed.items
        ]

        return jsonify({
            'results': results,
            'pagination': {
                'page': data_processed.page,
                'per_page': data_processed.per_page,
                'total': data_processed.total,
                'pages': data_processed.pages
            }
        })

    except ValueError as e:
        return jsonify({'error': 'Invalid page or per_page parameter'}), 400

    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500