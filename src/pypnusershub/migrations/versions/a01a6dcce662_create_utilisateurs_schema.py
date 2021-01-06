"""Create utilisateurs schema

Revision ID: a01a6dcce662
Revises: 
Create Date: 2020-12-31 16:48:07.084207

"""
from alembic import op, context
import sqlalchemy as sa
import pkg_resources
from distutils.util import strtobool


# revision identifiers, used by Alembic.
revision = 'a01a6dcce662'
down_revision = None
branch_labels = ('utilisateurs',)
depends_on = None


def upgrade():
    sql_files = ['usershub.sql']
    if strtobool(context.get_x_argument(as_dictionary=True).get('usershub-data', "true")):
        sql_files += ['usershub-data.sql']
    if strtobool(context.get_x_argument(as_dictionary=True).get('usershub-sample-data', "false")):
        sql_files += ['usershub-dataset.sql']
    for sql_file in sql_files:
        operations = pkg_resources.resource_string("pypnusershub.migrations", f"data/{sql_file}").decode('utf-8')
        op.execute(operations)


def downgrade():
    op.execute('DROP SCHEMA utilisateurs CASCADE')
