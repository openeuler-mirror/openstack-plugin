# Copyright 2023 OpenStack Foundation
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

from alembic import op
import sqlalchemy as sa

"""add router gateway port forwarding

Revision ID: cab12b72ed90
Revises: c613d0b82681
Create Date: 2023-07-04 10:27:54.485453

"""

# revision identifiers, used by Alembic.
revision = 'cab12b72ed90'
down_revision = 'c613d0b82681'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'rgportforwardings',
        sa.Column('id', sa.String(length=36), nullable=False),
        sa.Column('router_id', sa.String(length=36), nullable=False),
        sa.Column('external_port', sa.Integer(), nullable=False),
        sa.Column('internal_neutron_port_id', sa.String(length=36),
                  nullable=False),
        sa.Column('protocol', sa.String(length=40), nullable=False),
        sa.Column('socket', sa.String(length=36), nullable=False),
        sa.ForeignKeyConstraint(['internal_neutron_port_id'], ['ports.id'],
                                ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['router_id'], ['routers.id'],
                                ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint(
            'internal_neutron_port_id', 'socket', 'protocol',
            name='uniq_port_forwardings0internal_neutron_port_id0socket0protocol'),
        sa.UniqueConstraint(
            'router_id', 'external_port', 'protocol',
            name='uniq_rg_port_forwardings0router_id0external_port0protocol')
    )
    # ### end Alembic commands ###
