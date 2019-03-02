"""empty message

Revision ID: cd59fc52af9d
Revises: 31048e0f0756
Create Date: 2019-02-27 02:26:20.170759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd59fc52af9d'
down_revision = '31048e0f0756'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agrimodulefbtable',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=True),
    sa.Column('msg', sa.Text(), nullable=True),
    sa.Column('_time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contactustable',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('email', sa.String(length=30), nullable=True),
    sa.Column('phone', sa.String(length=30), nullable=True),
    sa.Column('msg', sa.Text(), nullable=True),
    sa.Column('_time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('newslettertable',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=True),
    sa.Column('_time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('platformfbtable',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=True),
    sa.Column('msg', sa.Text(), nullable=True),
    sa.Column('_time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workwithustable',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=True),
    sa.Column('msg', sa.Text(), nullable=True),
    sa.Column('_time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('workwithustable')
    op.drop_table('platformfbtable')
    op.drop_table('newslettertable')
    op.drop_table('contactustable')
    op.drop_table('agrimodulefbtable')
    # ### end Alembic commands ###