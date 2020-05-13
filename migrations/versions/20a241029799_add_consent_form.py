"""add consent form

Revision ID: 20a241029799
Revises: 4b78f9d20b28
Create Date: 2020-05-13 20:13:23.959528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20a241029799'
down_revision = '4b78f9d20b28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('consent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('childFirstName', sa.String(length=80), nullable=False),
    sa.Column('childLastName', sa.String(length=80), nullable=False),
    sa.Column('parentFirstName', sa.String(length=80), nullable=False),
    sa.Column('parentLastName', sa.String(length=80), nullable=False),
    sa.Column('signature', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('consent')
    # ### end Alembic commands ###
