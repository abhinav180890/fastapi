"""add last few columns to post table

Revision ID: 2ecf12e5de35
Revises: 33825979c7dc
Create Date: 2022-05-24 09:56:25.454823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ecf12e5de35'
down_revision = '33825979c7dc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                           server_default=sa.text('now()'), nullable=False))

def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')