"""add content column to posts

Revision ID: a459485dfe23
Revises: 051d3d673b86
Create Date: 2021-12-16 16:14:33.774952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a459485dfe23'
down_revision = '051d3d673b86'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
