"""add fk to post

Revision ID: 55725dc54fc3
Revises: 1818be453baf
Create Date: 2021-12-16 16:32:29.109457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55725dc54fc3'
down_revision = '1818be453baf'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
