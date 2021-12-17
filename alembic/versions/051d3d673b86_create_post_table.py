"""create post table

Revision ID: 051d3d673b86
Revises: 
Create Date: 2021-12-16 16:01:45.459007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '051d3d673b86'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
