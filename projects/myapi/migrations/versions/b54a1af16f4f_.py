"""empty message

Revision ID: b54a1af16f4f
Revises: d2785ba1abeb
Create Date: 2024-07-09 17:10:02.296765

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b54a1af16f4f'
down_revision: Union[str, None] = 'd2785ba1abeb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'answer', 'user', ['user_id'], ['id'])
    op.add_column('question', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'question', 'user', ['user_id'], ['id'])
    op.add_column('user', sa.Column('real_username', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'real_username')
    op.drop_constraint(None, 'question', type_='foreignkey')
    op.drop_column('question', 'user_id')
    op.drop_constraint(None, 'answer', type_='foreignkey')
    op.drop_column('answer', 'user_id')
    # ### end Alembic commands ###
