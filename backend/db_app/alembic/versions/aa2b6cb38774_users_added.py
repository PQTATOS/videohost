"""users added

Revision ID: aa2b6cb38774
Revises: fd8c5523aa6e
Create Date: 2023-05-16 15:04:24.793315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa2b6cb38774'
down_revision = 'fd8c5523aa6e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_index('ix_user_id_1', table_name='user')
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.drop_column('user', 'id_1')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('id_1', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.create_index('ix_user_id_1', 'user', ['id_1'], unique=False)
    op.drop_column('user', 'id')
    # ### end Alembic commands ###
