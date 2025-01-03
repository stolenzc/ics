"""init mysql

Revision ID: 71053c490bd6
Revises: 
Create Date: 2024-12-12 10:04:12.786152

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '71053c490bd6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('birthday',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=False, comment='生日日期'),
    sa.Column('is_lunar', sa.Boolean(), server_default=sa.text('0'), nullable=False, comment='是否是农历'),
    sa.Column('is_remind', sa.Boolean(), server_default=sa.text('1'), nullable=False, comment='是否提醒'),
    sa.Column('create_time', sa.DateTime(), server_default=sa.text('NOW()'), nullable=False),
    sa.Column('update_time', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('is_delete', sa.Boolean(), server_default=sa.text('0'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_birthday_id'), 'birthday', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_birthday_id'), table_name='birthday')
    op.drop_table('birthday')
    # ### end Alembic commands ###
