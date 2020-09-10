from marshmallow import fields, Schema
import datetime
from . import db
from .Request import RequestSchema
from .CampaignContributor import CampaignContributorSchema
from .Contributor import ContributorSchema

class Campaign(db.Model):

  # table name
  __tablename__ = 'campaigns'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  description = db.Column(db.Text)
  image = db.Column(db.String)
  manager = db.Column(db.String, nullable=False)
  upvote = db.Column(db.Integer)
  min_contribution = db.Column(db.Float, nullable=False)
  value = db.Column(db.Float)
  address = db.Column(db.String, unique=True, nullable=False)
  expiration = db.Column(db.DateTime)
  created_at = db.Column(db.DateTime)
  updated_at = db.Column(db.DateTime)
  requests = db.relationship('Request', cascade="all, delete-orphan")

  # class constructor
  def __init__(self, data):

    self.name = data.get('name')
    self.description = data.get('description')
    self.image = data.get('image')
    self.manager = data.get('manager')
    self.upvote = data.get('upvote')
    self.min_contribution = data.get('min_contribution')
    self.value = data.get('value')
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

  @staticmethod
  def get_campaign_by_address(address):
      return Campaign.query.filter_by(address=address)

  @staticmethod
  def get_campaign_by_name(name):
    return Campaign.query.filter_by(name=name).first()

  @staticmethod
  def get_campaigns_by_manager(manager):
      return Campaign.query.filter_by(manager=manager)

  def __repr(self):
    return '<id {}>'.format(self.id)

class CampaignSchema(Schema):
  """
  Campaign Schema
  """
  id = fields.Int(dump_only=True)
  name = fields.Str(required=True)
  description = fields.Str(required=False)
  image = fields.Str(required=False)
  manager = fields.Str(required=True)
  upvote = fields.Int(required=False)
  min_contribution = fields.Float(required=True)
  value = fields.Float(required=False)
  address = fields.Str(required=True)
  expiration = fields.DateTime(required=False)
  created_at = fields.DateTime(dump_only=True)
  updated_at = fields.DateTime(dump_only=True)
  requests = fields.Nested(RequestSchema, many=True)
