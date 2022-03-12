"""empty message
Revision ID: 889db968153c
Revises: 
Create Date: 2021-03-22 23:16:25.158473
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '889db968153c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=150), nullable=True),
    sa.Column('description', sa.String(length=350), nullable=True),
    sa.Column('num_of_bedrooms', sa.Integer(), nullable=True),
    sa.Column('num_of_bathrooms', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('ptype', sa.String(length=10), nullable=True),
    sa.Column('location', sa.String(length=50), nullable=True),
    sa.Column('photo', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    # ### end Alembic commands ###