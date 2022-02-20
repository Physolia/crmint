# Copyright 2020 Google Inc. All rights reserved.
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

"""CRMint's worker executing Standard SQL scripts in BigQuery."""


from jobs.workers.bigquery.bq_worker import BQWorker


class BQScriptExecutor(BQWorker):  # pylint: disable=too-few-public-methods
  """Worker to run SQL scripts in BigQuery."""

  PARAMS = [
      ('query', 'sql', True, '', 'SQL script'),
  ]

  def _execute_sql_script(self, sql):
    client = self._get_client()
    job = client.query(sql, job_id_prefix=self._get_prefix())
    self._wait(job)

  def _execute(self):
    self._execute_sql_script(self._params['query'])