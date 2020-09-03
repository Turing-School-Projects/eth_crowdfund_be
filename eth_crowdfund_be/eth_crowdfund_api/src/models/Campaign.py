from marshmallow import fields, Schema 
import datetime 
from . import db
from .Request import RequestSchema

class Campaign(db.Model):
  """
  Campaign Model 
  """

  # table name 
  __tablename__ = 'campaigns'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  description = db.Column(db.Text)
  image = db.Column(db.String)
  manager = db.Column(db.String, nullable=False)
  contributors = db.Column(db.Integer)
  upvote = db.Column(db.Integer)
  min_contribution = db.Column(db.Float, nullable=False)
  address = db.Column(db.String, unique=True, nullable=False)
  expiration = db.Column(db.DateTime)
  created_at = db.Column(db.DateTime)
  updated_at = db.Column(db.DateTime)
  requests = db.relationship('Request', backref='campaigns')

  # class constructor
  def __init__(self, data):
    """
    Class constructor 
    """
    self.id = data.get('id')
    self.name = data.get('name')
    self.description = data.get('description')
    self.image = data.get('image')
    self.manager = data.get('manager')
    self.contributors = data.get('contributors')
    self.upvote = data.get('upvote')
    self.min_contribution = data.get('min_contribution')
    self.address = data.get('address')
    self.expiration = data.get('expiration')
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
  def get_all_campaigns():
    return Campaign.query.all()

  @staticmethod 
  def get_one_campaign(id):
    return Campaign.query.get(id)

  def __repr__(self):
    return '<id {}>'.format(self.id)

class CampaignSchema(Schema):
  """
  Campaign Schema 
  """
  id = fields.Str(dump_only=True)
  name = fields.Str(required=True)
  description = fields.Str(required=False)
  image = fields.Str(required=False)
  manager = fields.Str(required=True)
  contributors = fields.Int(required=False)
  upvote = fields.Int(required=False)
  min_contribution = fields.Float(required=True)
  address = fields.Str(required=True)
  expiration = fields.DateTime(required=False)
  created_at = fields.DateTime(dump_only=True)
  updated_at = fields.DateTime(dump_only=True)
  requests = fields.Nested(RequestSchema, many=True)
