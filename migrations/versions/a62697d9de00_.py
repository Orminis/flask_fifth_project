"""empty message

Revision ID: a62697d9de00
Revises: 234fab4607b8
Create Date: 2022-07-30 17:41:09.151381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a62697d9de00'
down_revision = '234fab4607b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('complainers', 'location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('complainers', sa.Column('location', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
