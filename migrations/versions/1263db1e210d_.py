"""empty message

Revision ID: 1263db1e210d
Revises: 0762e480a73d
Create Date: 2021-11-18 21:53:47.479476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1263db1e210d'
down_revision = '0762e480a73d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('application', sa.Column('tagline', sa.String(length=50), nullable=True))
    op.drop_index('ix_application_timestamp', table_name='application')
    op.drop_column('application', 'timestamp')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('application', sa.Column('timestamp', sa.DATETIME(), nullable=True))
    op.create_index('ix_application_timestamp', 'application', ['timestamp'], unique=False)
    op.drop_column('application', 'tagline')
    # ### end Alembic commands ###
