"""empty message

Revision ID: 444e53f167fd
Revises: cc398a11c2ac
Create Date: 2024-07-01 18:48:07.829082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '444e53f167fd'
down_revision = 'cc398a11c2ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
