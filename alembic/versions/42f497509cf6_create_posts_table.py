"""create posts table"

Revision ID: 42f497509cf6
Revises: 
Create Date: 2022-05-24 09:00:39.960532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42f497509cf6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                            sa.Column('title', sa.String(), nullable=False))


def downgrade():
    op.drop_table('posts')
