"""add fields

Revision ID: 5ddddc663809
Revises: 13004b2dd76a
Create Date: 2025-01-07 22:24:37.267751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ddddc663809'
down_revision = '13004b2dd76a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('body', sa.String(), nullable=True))
    op.add_column('messages', sa.Column('username', sa.String(), nullable=True))
    op.add_column('messages', sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'created_at')
    op.drop_column('messages', 'username')
    op.drop_column('messages', 'body')
    # ### end Alembic commands ###
