"""empty message

Revision ID: 41ca1375d77c
Revises: 
Create Date: 2018-03-15 11:27:48.842061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41ca1375d77c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('course')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('course_code', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('department', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('long_title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'course_pkey')
    )
    # ### end Alembic commands ###
