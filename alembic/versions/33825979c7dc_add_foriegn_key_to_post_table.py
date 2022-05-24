"""add foriegn key to post table

Revision ID: 33825979c7dc
Revises: 98e7d02e778f
Create Date: 2022-05-24 09:48:32.116007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33825979c7dc'
down_revision = '98e7d02e778f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id',sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", 
                           local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")


def downgrade():
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
