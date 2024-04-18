from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, verify_jwt_in_request, get_jwt_identity
from marshmallow import Schema, fields
from sqlalchemy import text
from ..conn import Session
from ..logger import logger

select_module_id_bp = Blueprint('select_module_id', __name__)

class SelectModuleIDSchema(Schema):
    module_id = fields.Int(required=True)

@select_module_id_bp.route('/select_module/<int:id>', methods=['GET'])
@jwt_required()
def select_module_id(id):
    
    doctor_id = get_jwt_identity()

    data = jsonify({'module_id': id})
    schema = SelectModuleIDSchema()
    errors = schema.validate(data)

    

    if errors:
        logger.error(f"Invalid request made by Doctor ID: {doctor_id}", extra={"method": "GET", "statuscode": 400})
        return jsonify({'errors': errors}), 400
    
    session = Session()
    module_id = data['module_id']
    try:
        result = session.execute(
            text('SELECT * FROM modules WHERE module_id = :module_id'),
            {'module_id': module_id},
        ).fetchone()
        if result:
            result = result._asdict()
            logger.info(f"Doctor ID: {doctor_id} selected Module ID: {module_id}", extra={"method": "GET", "statuscode": 200})
        return jsonify({'success': True, 'module': result}), 200
    except Exception as e:
        session.rollback()
        logger.warning(str(e), extra={"methos": "GET", "statuscode": 500})
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()