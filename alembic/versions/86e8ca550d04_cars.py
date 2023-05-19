"""cars

Revision ID: 86e8ca550d04
Revises: 284d6f0d6f25
Create Date: 2023-05-15 19:51:27.227785

"""
import sqlmodel  # NEW
from alembic import op

# revision identifiers, used by Alembic.
from sqlmodel import insert, delete, select

from database.models import Company


revision = "86e8ca550d04"
down_revision = "284d6f0d6f25"
branch_labels = None
depends_on = None

companies = [Company(name="BMW"), Company(name="Porsche")]


def upgrade():
    values = ", ".join(f"('{c.name}')" for c in companies)
    stmt = f"INSERT INTO company (name) VALUES {values}"
    op.execute(stmt)


def downgrade():
    # Query the Company instances from the database using their names
    for c in companies:
        op.execute(delete(Company).where(Company.name == c.name))
