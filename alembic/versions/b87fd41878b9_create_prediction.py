"""create prediction

Revision ID: b87fd41878b9
Revises: 9caea95eb101
Create Date: 2024-01-12 15:33:03.109282

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "b87fd41878b9"
down_revision: Union[str, None] = "9caea95eb101"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "prediction_model_entities",
        sa.Column("id", sa.String(length=21), primary_key=True),
        sa.Column("created_at", sa.DateTime, nullable=False, default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, nullable=False, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column("name", sa.String(length=255), unique=True, nullable=False),
        sa.Column("model_type", sa.String(length=255), nullable=False),
        sa.Column("symptoms", sa.Text, nullable=False),
        sa.Column("path", sa.Text, nullable=False),
    )

    op.create_table(
        "prediction_result_entities",
        sa.Column("id", sa.String(length=21), primary_key=True),
        sa.Column("created_at", sa.DateTime, nullable=False, default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, nullable=False, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column("result", sa.String(length=255), nullable=False),
        sa.Column("prediction_model_id", sa.String(length=21), nullable=False),
        sa.Column("user_id", sa.String(length=21), index=True, unique=False),
    )


def downgrade() -> None:
    op.drop_table("prediction_result_entities")
    op.drop_table("prediction_model_entities")
