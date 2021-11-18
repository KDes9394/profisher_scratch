"""empty message

Revision ID: a4adb83df54c
Revises: da27f1ae349c
Create Date: 2021-11-17 14:14:43.954190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4adb83df54c'
down_revision = 'da27f1ae349c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job', sa.Column('title', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job', 'title')
    # ### end Alembic commands ###
