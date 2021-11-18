"""empty message

Revision ID: 39ed464f731b
Revises: a4adb83df54c
Create Date: 2021-11-18 00:28:58.291043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39ed464f731b'
down_revision = 'a4adb83df54c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_us', sa.String(length=140), nullable=True))
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.VARCHAR(length=140), nullable=True))
    op.drop_column('user', 'about_us')
    # ### end Alembic commands ###