"""empty message

Revision ID: 58227a332d7d
Revises: b43c107f855b
Create Date: 2021-11-18 14:24:04.187082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58227a332d7d'
down_revision = 'b43c107f855b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job', sa.Column('requirements1', sa.String(length=500), nullable=True))
    op.add_column('job', sa.Column('requirements2', sa.String(length=500), nullable=True))
    op.add_column('job', sa.Column('requirements3', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job', 'requirements3')
    op.drop_column('job', 'requirements2')
    op.drop_column('job', 'requirements1')
    # ### end Alembic commands ###
