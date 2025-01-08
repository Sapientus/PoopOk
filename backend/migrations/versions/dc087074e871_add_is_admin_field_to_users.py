"""add is_admin field to users

Revision ID: dc087074e871
Revises: 7b880190ad0d
Create Date: 2025-01-08 11:02:41.308116

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc087074e871'
down_revision: Union[str, None] = '7b880190ad0d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('is_admin', sa.Boolean(), nullable=False, server_default='false'))


def downgrade() -> None:
    op.drop_column('users', 'is_admin')

