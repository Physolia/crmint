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

"""Application configuration."""
import os


class Config(object):
  """Base configuration."""
  SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
  """Production configuration."""
  ENV = 'prod'
  DEBUG = False


class DevConfig(Config):
  """Development configuration."""
  ENV = 'dev'
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = os.getenv(
      'DATABASE_URI',
      'mysql+mysqlconnector://crmint:crmint@db:3306/crmint_development'
  )
