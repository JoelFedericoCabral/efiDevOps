from flask import Blueprint, jsonify, request
from flask.views import MethodView
from flask_jwt_extended import jwt_required, current_user
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from app import db
from app.schemas import comment_schema
from app.models import Comment

bp = Blueprint('comments', __name__)

class CommentAPI(MethodView):

    def get(self, comment_id):
        # Devolver un solo comentario
        comment = Comment.query.get(comment_id)
        if not comment:
            return jsonify(error=f'Comment {comment_id} not found.'), 404
        return comment_schema.dump(comment), 200

    @jwt_required()
    def post(self):
        # Crear un nuevo comentario para una publicación específica.

        comment_data = request.json
        if not comment_data:
            return jsonify(error=f'Not input data provided.'), 404

        try:
            new_comment = comment_schema.load(comment_data)
            new_comment.user_id = current_user.id
            db.session.add(new_comment)
            db.session.commit()
            return comment_schema.dump(new_comment), 201 
        except ValidationError as err:
            return jsonify(err.messages), 400
        except IntegrityError:
            db.session.rollback()  # Rollback en caso de error
            return jsonify(error=f'Error creating comment'), 40

    @jwt_required()
    def delete(self, comment_id):
        # Eliminar un solo comentario
        comment = Comment.query.get(comment_id)
        if not comment:
            return jsonify(error=f'Comment {comment_id} not found.'), 404

        # Verifica si es dueño
        if comment.user_id != current_user.id:
            return jsonify(error='Forbidden'), 403

        db.session.delete(comment)
        db.session.commit()

        return jsonify(message='Comment delete sucesfully.'), 200

    @jwt_required()
    def put(self, comment_id):
        # Actualizar un solo comentario
        comment_data = request.json
        if not comment_data:
            return jsonify(error='No input data provided.'), 400

        comment = Comment.query.get(comment_id)
        if not comment:
            return jsonify(error=f'Comment {comment_id} not found.'), 404

        # Verifica si es dueño
        if comment.user_id != current_user.id:
            return jsonify(error='Forbidden'), 403

        try:
            updated_comment = comment_schema.load(comment_data, instance=comment, partial=True)
            db.session.commit()
            return comment_schema.dump(updated_comment), 200
        except ValidationError as err:
            return jsonify(err.messages), 400


comment_view = CommentAPI.as_view('comment_api')
bp.add_url_rule('/', view_func=comment_view, methods=['POST',])
bp.add_url_rule('/<int:comment_id>', view_func=comment_view, methods=['GET', 'PUT', 'DELETE'])