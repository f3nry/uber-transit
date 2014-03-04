"""create agencies

Revision ID: 3e49366fccab
Revises: None
Create Date: 2014-03-04 00:16:34.752304

"""

# revision identifiers, used by Alembic.
revision = '3e49366fccab'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
      'agencies',
      sa.Column('id', sa.Integer, primary_key=True),
      sa.Column('name', sa.String, nullable=False),
      sa.Column('has_direction', sa.Boolean, nullable=False),
      sa.Column('mode', sa.String)
    )


def downgrade():
    op.drop_table('agencies')
