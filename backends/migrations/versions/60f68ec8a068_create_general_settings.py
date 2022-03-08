# Copyright 2018 Google Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Create GeneralSettings

Revision ID: 60f68ec8a068
Revises: 05df3bf17d09
Create Date: 2017-06-22 14:13:59.989645

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '60f68ec8a068'
down_revision = '05df3bf17d09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('general_settings',
                    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
                    sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
                    sa.Column('value', sa.Text(), nullable=True),
                    sa.Column('created_at', mysql.DATETIME(), nullable=False),
                    sa.Column('updated_at', mysql.DATETIME(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    mysql_default_charset=u'utf8',
                    mysql_engine=u'InnoDB'
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('general_settings')
    # ### end Alembic commands ###