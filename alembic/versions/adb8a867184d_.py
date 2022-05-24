"""empty message

Revision ID: adb8a867184d
Revises: 2ecf12e5de35
Create Date: 2022-05-24 10:11:10.363008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adb8a867184d'
down_revision = '2ecf12e5de35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    # ### end Alembic commands ###