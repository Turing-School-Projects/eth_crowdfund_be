from marshmallow import fields, Schema
from . import db
# from .ApiKey import ApiKeySchema


class ApiKey(db.Model):
  # table name
  __tablename__ = 'api_keys'
  id = db.Column(db.Integer, primary_key=True)
  key = db.Column(db.String, unique=True, nullable=False)
  created_at = db.Column(db.DateTime)
  updated_at = db.Column(db.DateTime)

  # class constructor
  def __init__(self, data):
    self.key = data.get('key')
    self.created_at = datetime.datetime.utcnow()
    self.updated_at = datetime.datetime.utcnow()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, value in data.items():
      setattr(self, key, value)
    self.updated_at = datetime.datetime.utcnow()
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  @staticmethod
  def get_all_api_keys():
    return ApiKey.query.all()

  @staticmethod
  def get_api_key_by_id(id):
    return ApiKey.query.get(id)

  @staticmethod
  def get_api_key_by_key(key):
    return ApiKey.query.filter_by(key=key)

  def __repr(self):
    return '<id {}>'.format(self.id)


class ApiKeySchema(Schema):
  id = fields.Int(dump_only=True)
  key = fields.Str(required=True)
  created_at = fields.DateTime(dump_only=True)
  updated_at = fields.DateTime(dump_only=True)
