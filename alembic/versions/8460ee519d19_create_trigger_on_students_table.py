"""Create trigger on students table

Revision ID: 8460ee519d19
Revises: 1d3d1247038b
Create Date: 2024-11-13 19:03:14.754182

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8460ee519d19'
down_revision: Union[str, None] = '1d3d1247038b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
