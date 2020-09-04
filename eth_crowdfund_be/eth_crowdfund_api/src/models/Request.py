from marshmallow import fields, Schema 
import datetime 
from . import db


class Request(db.Model):
  """
  Request Model 
  """

  # table name 
  __tablename__ = 'requests'
  id = db.Column(db.Integer, primary_key=True)
  campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'), nullable=False)
  description = db.Column(db.String)
  image = db.Column(db.String)
  value = db.Column(db.Float, nullable=False)
  recipient = db.Column(db.String, nullable=False)
  approved = db.Column(db.Boolean, default=False)
  finalized = db.Column(db.Boolean, default=False)
  approvals = db.Column(db.Integer)
  created_at = db.Column(db.DateTime)
  updated_at = db.Column(db.DateTime)
  campaign = db.relationship('Campaign', backref='requests')




  # class constructor
  def __init__(self, data):
    self.description = data.get('description')
    self.image = data.get('image')
    self.value = data.get('value')
    self.recipient = data.get('recipient')
    self.approved = data.get('approved')
    self.finalized = data.get('finalized')
    self.approvals = data.get('approvals')
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
  def get_all_requests():
    return Request.query.all()

  @staticmethod 
  def get_one_request(id):
    return Request.query.get(id)

  def __repr__(self):
    return '<id {}>'.format(self.id)

class RequestSchema(Schema):
  id = fields.Int(dump_only=True)
  campaign_id = fields.Str(required=True)
  description = fields.Str(required=False)
  image = fields.Str(required=False)
  value = fields.Float(required=True)
  recipient = fields.Str(required=True)
  approved = fields.Bool(required=False)
  finalized = fields.Bool(required=False)
  approvals = fields.Int(required=False)
  created_at = fields.DateTime(dump_only=True)
  updated_at = fields.DateTime(dump_only=True)
