"""Relaciones marca y tipo

Revision ID: ffc8fcb873f6
Revises: cbd0fa54c409
Create Date: 2024-06-25 20:26:11.809065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffc8fcb873f6'
down_revision = 'cbd0fa54c409'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehiculo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tipo_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('marca_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'tipo', ['tipo_id'], ['id'])
        batch_op.create_foreign_key(None, 'marca', ['marca_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehiculo', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('marca_id')
        batch_op.drop_column('tipo_id')

    # ### end Alembic commands ###
