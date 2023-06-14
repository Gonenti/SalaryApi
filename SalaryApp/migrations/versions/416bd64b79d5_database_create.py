"""Database create

Revision ID: 416bd64b79d5
Revises: 
Create Date: 2023-06-14 02:37:05.158994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '416bd64b79d5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userName', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('salary',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=False),
    sa.Column('increase_date', sa.TIMESTAMP(), nullable=False),
    sa.Column('payment_date', sa.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id', 'increase_date', 'payment_date')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('salary')
    op.drop_table('user')
    # ### end Alembic commands ###
