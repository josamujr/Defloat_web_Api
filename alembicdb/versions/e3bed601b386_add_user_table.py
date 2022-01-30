"""add user table

Revision ID: e3bed601b386
Revises: d07087846169
Create Date: 2022-01-30 01:58:06.726113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3bed601b386'
down_revision = 'd07087846169'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(50), nullable=False),
                    sa.Column("password", sa.String(250), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")
                    )
    pass


def downgrade():
    op.drop_table("users")
    pass
