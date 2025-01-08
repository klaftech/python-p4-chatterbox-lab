"""initia

Revision ID: 13004b2dd76a
Revises: 
Create Date: 2025-01-07 22:22:12.825132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13004b2dd76a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###
