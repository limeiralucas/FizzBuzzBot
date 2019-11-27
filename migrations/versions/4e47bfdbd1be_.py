"""empty message

Revision ID: 4e47bfdbd1be
Revises: 
Create Date: 2019-11-27 20:44:52.778606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e47bfdbd1be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authentication',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('request_token', sa.String(length=64), nullable=True),
    sa.Column('oauth_token', sa.String(length=64), nullable=True),
    sa.Column('oauth_token_secret', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('interaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender', sa.String(length=100), nullable=True),
    sa.Column('message', sa.String(length=280), nullable=True),
    sa.Column('response', sa.String(length=280), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('interaction')
    op.drop_table('authentication')
    # ### end Alembic commands ###