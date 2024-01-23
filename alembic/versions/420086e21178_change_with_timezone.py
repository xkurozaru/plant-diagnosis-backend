"""change with timezone

Revision ID: 420086e21178
Revises: b87fd41878b9
Create Date: 2024-01-23 17:26:02.690249

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "420086e21178"
down_revision: Union[str, None] = "b87fd41878b9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        table_name="prediction_result_entities",
        column_name="predict_at",
        nullable=False,
        type_=sa.DateTime(timezone=True),
    )

    pass


def downgrade() -> None:
    op.alter_column(
        table_name="prediction_result_entities",
        column_name="predict_at",
        nullable=False,
        type_=sa.DateTime(timezone=False),
    )
    pass
