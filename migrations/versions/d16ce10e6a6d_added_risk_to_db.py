"""added risk to db

Revision ID: d16ce10e6a6d
Revises: 74febd982fa2
Create Date: 2018-08-09 19:06:59.614065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd16ce10e6a6d'
down_revision = '74febd982fa2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('risk', sa.String(length=120), nullable=True))
    op.create_index(op.f('ix_user_risk'), 'user', ['risk'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_risk'), table_name='user')
    op.drop_column('user', 'risk')
    # ### end Alembic commands ###
