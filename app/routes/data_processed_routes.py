from app import app, logger
from app.models import DataProcessed
from app.schemas import DataProcessedSchema
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

        schema = DataProcessedSchema(many=True)
        results = schema.dump(data_processed)

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

@app.route('/api/data_processed/<int:id>', methods=['GET'])
@cross_origin()
def api_data_processed_by_id(id):
    try:
        data_processed = DataProcessed.query.get(id)

        if data_processed is None:
            return jsonify({'error': 'No data found'}), 404

        schema = DataProcessedSchema()
        result = schema.dump(data_processed)

        return jsonify(result), 200

    except ValueError as e:
        return jsonify({'error': 'Invalid id parameter'}), 400

    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500