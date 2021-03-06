"""errors vote 2

Revision ID: f0c14593dc8a
Revises: ca3804dacf7a
Create Date: 2021-12-16 16:58:04.085253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0c14593dc8a'
down_revision = 'ca3804dacf7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('votes_user_id_fkey', 'votes', type_='foreignkey')
    op.drop_constraint('votes_post_id_fkey', 'votes', type_='foreignkey')
    op.create_foreign_key(None, 'votes', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'votes', 'posts', ['post_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'votes', type_='foreignkey')
    op.drop_constraint(None, 'votes', type_='foreignkey')
    op.create_foreign_key('votes_post_id_fkey', 'votes', 'users', ['post_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('votes_user_id_fkey', 'votes', 'posts', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
