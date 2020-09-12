"""empty message

Revision ID: 96a8d065e5ea
Revises: 
Create Date: 2020-09-11 15:36:01.940177

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96a8d065e5ea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('campaigns',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('manager', sa.String(), nullable=False),
    sa.Column('upvote', sa.Integer(), nullable=True),
    sa.Column('min_contribution', sa.Float(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('expiration', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address')
    )
    op.create_table('requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('campaign_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('recipient', sa.String(), nullable=False),
    sa.Column('approved', sa.Boolean(), nullable=True),
    sa.Column('finalized', sa.Boolean(), nullable=True),
    sa.Column('approvals', sa.Integer(), nullable=True),
    sa.Column('eth_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['campaign_id'], ['campaigns.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contributor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address')
    )
    op.create_table('campaign_contributor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('campaign_id', sa.Integer(), nullable=False),
    sa.Column('contributor_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['campaign_id'], ['campaigns.id'], ),
    sa.ForeignKeyConstraint(['contributor_id'], ['contributor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('campaigns', sa.Column('value', sa.Float(), nullable=True))
    op.drop_column('campaigns', 'contributors')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('campaigns', sa.Column('contributors', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('campaigns', 'value')
    op.drop_table('campaign_contributor')
    op.drop_table('contributor')
    # ### end Alembic commands ###
