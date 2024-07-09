"""empty message

Revision ID: 870f8077fe51
Revises: 087f06839540
Create Date: 2024-07-09 17:46:43.376046

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '870f8077fe51'
down_revision: Union[str, None] = '087f06839540'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'answer', 'user', ['user_id'], ['id'])
    op.add_column('question', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'question', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'question', type_='foreignkey')
    op.drop_column('question', 'user_id')
    op.drop_constraint(None, 'answer', type_='foreignkey')
    # ### end Alembic commands ###
