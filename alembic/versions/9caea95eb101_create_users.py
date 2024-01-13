"""create users

Revision ID: 9caea95eb101
Revises: 73e7f87610e1
Create Date: 2024-01-11 16:19:13.141783

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "9caea95eb101"
down_revision: Union[str, None] = "73e7f87610e1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user_entities",
        sa.Column("id", sa.String(21), primary_key=True),
        sa.Column("created_at", sa.DateTime, nullable=False, default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, nullable=False, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column("username", sa.String(255), index=True, unique=True, nullable=False),
        sa.Column("hash_password", sa.String(255), nullable=False),
        sa.Column("role", sa.String(255), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("user_entities")
