# Global Schemas
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from app import ma
from app.models import User, Post, Comment

# User Schemas
class UserSchema(ma.SQLAlchemyAutoSchema):
    id = fields.String(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    password = fields.String(load_only=True) # Este campo se usa solo para cargar datos

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'created_at', 'update_at'] 
        load_instance = True

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Post Schemas
class PostSchema(ma.SQLAlchemyAutoSchema):
    id = fields.String(dump_only=True)
    comments = fields.Nested('CommentSchema', many=True, dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    user_id = fields.String(dump_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'user_id', 'comments', 'created_at', 'updated_at']
        load_instance = True

post_schema = PostSchema()
posts_schema = PostSchema(many=True)

# Comment Schemas
class CommentSchema(ma.SQLAlchemyAutoSchema):
    id = fields.String(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    user_id = fields.String(dump_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'user_id', 'post_id', 'created_at', 'updated_at']
        load_instance = True

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)

