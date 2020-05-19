"""new table category 2

Revision ID: 3e7c677c1097
Revises: b36faa5f2632
Create Date: 2020-05-19 23:50:33.719049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e7c677c1097'
down_revision = 'b36faa5f2632'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'category', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'category', type_='unique')
    # ### end Alembic commands ###
