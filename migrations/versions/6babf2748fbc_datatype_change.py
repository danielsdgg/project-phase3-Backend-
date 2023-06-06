"""datatype change

Revision ID: 6babf2748fbc
Revises: 899601259427
Create Date: 2023-06-06 22:00:23.843362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6babf2748fbc'
down_revision = '899601259427'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('phones', 'manufacturer_id', existing_type=sa.VARCHAR, type_=sa.Integer())
    op.alter_column('phones', 'customer_id', existing_type=sa.VARCHAR, type_=sa.Integer())
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('phones', 'manufacturer_id', existing_type=sa.Integer(), type_=sa.VARCHAR)
    op.alter_column('phones', 'customer_id', existing_type=sa.Integer(), type_=sa.VARCHAR)
    # ### end Alembic commands ###
