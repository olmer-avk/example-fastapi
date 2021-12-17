"""add user table

Revision ID: 1818be453baf
Revises: a459485dfe23
Create Date: 2021-12-16 16:21:00.985099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1818be453baf'
down_revision = 'a459485dfe23'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass