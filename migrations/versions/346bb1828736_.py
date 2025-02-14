"""empty message

Revision ID: 346bb1828736
Revises: 
Create Date: 2025-02-14 11:31:11.097637

"""
from alembic import op
import sqlalchemy as sa
from app.models.fields import JsonField



# revision identifiers, used by Alembic.
revision = '346bb1828736'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
        sa.Column('slug', sa.String(length=255), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('data_processed',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
        sa.Column('original_data', JsonField(), nullable=True),
        sa.Column('processed_data', JsonField(), nullable=True),
        sa.Column('company_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data_processed')
    op.drop_table('company')
    # ### end Alembic commands ###
