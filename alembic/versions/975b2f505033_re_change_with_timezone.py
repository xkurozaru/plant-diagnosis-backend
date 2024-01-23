"""re-change with timezone

Revision ID: 975b2f505033
Revises: 420086e21178
Create Date: 2024-01-23 17:40:18.118281

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "975b2f505033"
down_revision: Union[str, None] = "420086e21178"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        table_name="prediction_result_entities",
        column_name="predict_at",
        nullable=False,
        type_=sa.TIMESTAMP.timezone,
    )
    pass


def downgrade() -> None:
    op.alter_column(
        table_name="prediction_result_entities",
        column_name="predict_at",
        nullable=False,
        type_=sa.DateTime(timezone=True),
    )
    pass
