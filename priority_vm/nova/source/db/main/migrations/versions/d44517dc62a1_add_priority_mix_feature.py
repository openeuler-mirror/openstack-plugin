# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""add priority mix feature

Revision ID: d44517dc62a1
Revises: 16f1fbcab42b
Create Date: 2022-05-31 07:27:31.234643
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd44517dc62a1'
down_revision = '16f1fbcab42b'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('compute_nodes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('priority', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('high_vcpus_used', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('low_vcpus_used', sa.Integer(), nullable=True))

    with op.batch_alter_table('instances', schema=None) as batch_op:
        batch_op.add_column(sa.Column('priority', sa.String(length=255), nullable=True))
