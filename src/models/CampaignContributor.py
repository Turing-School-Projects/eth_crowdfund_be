from marshmallow import fields, Schema
import datetime
from . import db


class CampaignContributor(db.Model):
  """
  CampaignContributor Model
  """

  # table name
  __tablename__ = 'campaign_contributor'
  id = db.Column(db.Integer, primary_key=True)
  campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'), nullable=False)
  contributor_id = db.Column(db.Integer, db.ForeignKey('contributor.id'), nullable=False)
  created_at = db.Column(db.DateTime)
  updated_at = db.Column(db.DateTime)




  # class constructor
  def __init__(self, data):
    self.campaign_id = data.get('campaign_id')
    self.contributor_id = data.get('contributor_id')
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
  def get_all_campaign_contributors():
    return CampaignContributor.query.all()

  @staticmethod
  def get_one_campaign_contribution(id):
    return CampaignContributor.query.get(id)

  def __repr(self):
    return '<id {}>'.format(self.id)

class CampaignContributorSchema(Schema):
  id = fields.Int(dump_only=True)
  campaign_id = fields.Int(required=True)
  contributor_id = fields.Int(required=True)
  created_at = fields.DateTime(dump_only=True)
  updated_at = fields.DateTime(dump_only=True)
