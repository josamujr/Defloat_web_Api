"""add foreign key to posts table

Revision ID: 3ab15a989162
Revises: e3bed601b386
Create Date: 2022-01-30 02:34:41.209951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ab15a989162'
down_revision = 'e3bed601b386'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_to_users_fk', source_table="posts", referent_table ="users", local_cols =['owner_id'],remote_cols =['id'], ondelete="CASCADE")



def downgrade():
    op.drop_constraint("posts_to_users_fk", table_name = "posts")
    op.drop_column("posts", "owner_id")
    pass
