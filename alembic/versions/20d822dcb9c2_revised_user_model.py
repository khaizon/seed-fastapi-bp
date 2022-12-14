"""revised user model

Revision ID: 20d822dcb9c2
Revises: c1a33cc33509
Create Date: 2022-11-21 16:32:27.456038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20d822dcb9c2"
down_revision = "c1a33cc33509"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("name", sa.String(), nullable=False, server_default="NA"))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "name")
    # ### end Alembic commands ###
