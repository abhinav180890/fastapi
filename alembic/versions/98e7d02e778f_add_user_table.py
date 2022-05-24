"""add user table

Revision ID: 98e7d02e778f
Revises: 6f668c53f041
Create Date: 2022-05-24 09:17:31.321981

"""
from time import timezone
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98e7d02e778f'
down_revision = '6f668c53f041'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                     sa.Column('id', sa.Integer(), nullable=False),
                     sa.Column('email', sa.String(), nullable=False),
                     sa.Column('password', sa.String(), nullable=False),
                     sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                server_default=sa.text('now()'), nullable=False),
                     sa.PrimaryKeyConstraint('id'),
                     sa.UniqueConstraint('email')
                     )


def downgrade():
    op.drop_table('users')
