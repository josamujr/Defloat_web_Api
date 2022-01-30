"""create post table

Revision ID: e0698c5edbf6
Revises: 
Create Date: 2022-01-30 01:32:36.369846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0698c5edbf6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column("id", sa.Integer(), nullable=False, primary_key=True), sa.Column("title", sa.String(50), nullable=False))
    pass


def downgrade():
    op.drop_table("posts")
