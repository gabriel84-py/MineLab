"""remove hash column from license

Revision ID: 8501039d3baa
Revises: 15a8831d76ce
Create Date: 2025-07-29 14:26:09.047701

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8501039d3baa'
down_revision: Union[str, Sequence[str], None] = '15a8831d76ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    # Suppression de la colonne 'hash' dans la table 'license'
    with op.batch_alter_table("license", schema=None) as batch_op:
        batch_op.drop_index('ix_license_hash')  # supprimer l'index avant la suppression de la colonne
        batch_op.drop_column('hash')  # ensuite supprimer la colonne
    with op.batch_alter_table("license", schema=None) as batch_op:
        batch_op.drop_column("hash")


def downgrade():
    # En downgrade, on réajoute la colonne (nullable=True pour éviter problème)
    with op.batch_alter_table("license", schema=None) as batch_op:
        batch_op.add_column(sa.Column('hash', sa.String(), nullable=True))
