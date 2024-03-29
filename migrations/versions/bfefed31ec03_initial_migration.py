"""initial migration

Revision ID: bfefed31ec03
Revises: 
Create Date: 2024-01-12 15:48:12.169328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfefed31ec03'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('qr_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(length=255), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('qr_data')
    # ### end Alembic commands ###
