"""add content column

Revision ID: 6f668c53f041
Revises: 42f497509cf6
Create Date: 2022-05-24 09:12:04.481634

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f668c53f041'
down_revision = '42f497509cf6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content',sa.String(), nullable = False))


def downgrade():
    op.drop_column('posts', 'content')
    pass
