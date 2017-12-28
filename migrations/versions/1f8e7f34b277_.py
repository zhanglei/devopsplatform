"""empty message

Revision ID: 1f8e7f34b277
Revises: 152f83ca8105
Create Date: 2017-12-28 16:49:05.550816

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1f8e7f34b277'
down_revision = '152f83ca8105'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Version_file')
    op.drop_table('cbt_resource_action')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cbt_resource_action',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('action_user', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('task_id', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('resversion', mysql.VARCHAR(length=32), nullable=True),
    sa.Column('action_time', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('Version_file',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('location_new', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('location_old', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('crate_timme', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    # ### end Alembic commands ###
