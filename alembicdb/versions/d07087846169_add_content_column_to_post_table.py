"""add content column to post table

Revision ID: d07087846169
Revises: e0698c5edbf6
Create Date: 2022-01-30 01:48:26.163840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd07087846169'
down_revision = 'e0698c5edbf6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(90), nullable=False))


def downgrade():
    op.drop_column("posts","content")
    pass

