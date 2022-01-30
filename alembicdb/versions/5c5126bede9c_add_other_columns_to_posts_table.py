"""add other columns to posts table

Revision ID: 5c5126bede9c
Revises: 3ab15a989162
Create Date: 2022-01-30 02:53:39.000920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c5126bede9c'
down_revision = '3ab15a989162'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable = False, server_default = sa.text("now()")))


def downgrade():
    op.drop_column("posts", "created_at")
    pass
