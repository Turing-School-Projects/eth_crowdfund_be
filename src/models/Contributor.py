from marshmallow import fields, Schema
import datetime
from . import db


class Contributor(db.Model):
  """
  Contributor Model
  """

  # table name
  __tablename__ = 'contributor'
  id = db.Column(db.Integer, primary_key=True)
  address = db.Column(db.String, unique=True, nullable=False)
  email = db.Column(db.String)
  created_at = db.Column(db.DateTime)
  updated_at = db.Column(db.DateTime)
  contributions = db.relationship('Campaign', secondary='campaign_contributor', backref=db.backref('contributors', lazy=True))




  # class constructor
  def __init__(self, data):
    self.address = data.get('address')
    self.email = data.get('email')
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
  def get_all_contributors():
    return Contributor.query.all()

  @staticmethod
  def get_one_contributor(id):
    return Contributor.query.get(id)

  @staticmethod
  def get_contributor_by_address(address):
      return Contributor.query.filter_by(address=address)

  def __repr(self):
    return '<id {}>'.format(self.id)

class ContributorSchema(Schema):
  id = fields.Int(dump_only=True)
  address = fields.Str(required=True)
  email = fields.Str(required=False)
  created_at = fields.DateTime(dump_only=True)
  updated_at = fields.DateTime(dump_only=True)
