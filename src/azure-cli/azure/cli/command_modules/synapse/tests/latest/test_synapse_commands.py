# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


import os

from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer

TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class SynapseScenarioTests(ScenarioTest):
    location = "northeurope"

    @ResourceGroupPreparer(name_prefix='synapse-cli', random_name_length=16)
    def test_workspaces(self, resource_group):
        # create a workspace
        self._create_workspace()

        # get workspace with workspace name
        self.cmd('az synapse workspace show --name {workspace} --resource-group {rg}', checks=[])

        # list all workspaces under a specific resource group
        self.cmd('az synapse workspace list --resource-group {rg}', checks=[])

        # list all synapse under a specific subscription
        self.cmd('az synapse workspace list', checks=[])

        # delete workspace with workspace name
        self.cmd('az synapse workspace delete --name {workspace} --resource-group {rg} --yes', checks=[])

    def test_spark_pool(self):
        self.kwargs.update({
            'location': 'eastus',
            'workspace': 'testsynapseworkspace1234',
            'rg': 'cli-test-rg',
            'spark-pool': self.create_random_name(prefix='testpool', length=15),
        })

        # create spark pool
        self.cmd('az synapse spark pool create --name {spark-pool} --workspace-name {workspace} --resource-group {rg}'
                 ' --location {location}', checks=[])

        # get spark pool with spark pool name
        self.cmd('az synapse spark pool show --name {spark-pool} --workspace-name {workspace} --resource-group {rg}',
                 checks=[])

        # list all spark pools under the workspace
        self.cmd('az synapse spark pool list --workspace-name {workspace} --resource-group {rg}', checks=[])

        # delete spark pool with spark pool name
        self.cmd(
            'az synapse spark pool delete --name {spark-pool} --workspace-name {workspace} --resource-group {rg} --yes',
            checks=[])

    @ResourceGroupPreparer(name_prefix='synapse-cli', random_name_length=16)
    def test_spark_batch(self, resource_group):
        self.kwargs.update({
            'spark-pool': 'testsparkpool',
            'workspace': 'testsynapseworkspace1234',
            'job': 'WordCount_Java',
            'file': 'abfss://testfilesystem@adlsgen2account.dfs.core.windows.net/samples/java/wordcount/wordcount.jar',
            'class-name': 'WordCount',
            'args': [
                'abfss://testfilesystem@adlsgen2account.dfs.core.windows.net/samples/java/wordcount/shakespeare.txt',
                'abfss://testfilesystem@adlsgen2account.dfs.core.windows.net/samples/java/wordcount/result/'],
            'driver-memory': '4g',
            'driver-cores': 4,
            'executor-memory': '4g',
            'executor-cores': 4,
            'num-executors': 2,
            'batch-id': 1
        })

        # create a spark batch job
        self.cmd('az synapse spark batch create --name {job} --workspace-name {workspace} '
                 '--spark-pool-name {spark-pool} --file {file} --class-name {class-name} --args {args} '
                 '--driver-memory {driver-memory} --driver-cores {driver-cores} '
                 '--executor-memory {executor-memory} --executor-cores {executor-cores} '
                 '--num-executors {num-executors}', checks=[])

        # get a spark batch job with batch id
        self.cmd('az synapse spark batch show --id {batch-id} --workspace-name {workspace} '
                 '--spark-pool-name {spark-pool}', checks=[])

        # list all spark batch jobs under a specific spark pool
        self.cmd('az synapse spark batch list --workspace-name {workspace} '
                 '--spark-pool-name {spark-pool}', checks=[])

        # cancel a spark batch job with batch id
        self.cmd('az synapse spark batch cancel --id {batch-id} --workspace-name {workspace} '
                 '--spark-pool-name {spark-pool} --yes', checks=[])

    @ResourceGroupPreparer(name_prefix='synapse-cli', random_name_length=16)
    def test_spark_session_and_statements(self, resource_group):
        self.kwargs.update({
            'spark-pool': 'testsparkpool',
            'workspace': 'testsynapseworkspace1234',
            'job': 'session_job',
            'driver-memory': '4g',
            'driver-cores': 4,
            'executor-memory': '4g',
            'executor-cores': 4,
            'num-executors': 2,
            'code': "\"import time\ntime.sleep(10)\nprint('hello from cli')\"",
            'kind': 'pyspark'
        })

        # create a spark session
        create_result = self.cmd('az synapse spark session create --name {job} --workspace-name {workspace} '
                                 '--spark-pool-name {spark-pool} --driver-memory {driver-memory} --driver-cores {driver-cores} '
                                 '--executor-memory {executor-memory} --executor-cores {executor-cores} '
                                 '--num-executors {num-executors}', checks=[]).get_output_in_json()

        self.kwargs['session-id'] = create_result['id']

        # wait for creating spark session
        import time
        time.sleep(360)

        # get a spark session
        self.cmd('az synapse spark session show --id {session-id} --workspace-name {workspace} '
                 '--spark-pool-name {spark-pool}', checks=[])

        # list all spark session jobs under a specific spark pook
        self.cmd('az synapse spark session list --workspace-name {workspace} '
                 '--spark-pool-name {spark-pool}', checks=[])

        # reset spark session's timeout time
        self.cmd('az synapse spark session reset-timeout --id {session-id} --workspace-name {workspace} '
                 '--spark-pool-name {spark-pool}', checks=[])

        # create a spark session statement job
        statement = self.cmd('az synapse spark session-statement create --session-id {session-id} '
                             '--workspace-name {workspace} --spark-pool-name {spark-pool} '
                             '--code {code} --kind {kind}', checks=[]).get_output_in_json()
        self.kwargs['statement-id']=statement['id']

        # get a spark session statement
        self.cmd('az synapse spark session-statement show --id {statement-id} --session-id {session-id} '
                 '--workspace-name {workspace} --spark-pool-name {spark-pool}', checks=[])

        # list all spark session statements under a specific spark session
        self.cmd('az synapse spark session-statement list --session-id {session-id} '
                 '--workspace-name {workspace} --spark-pool-name {spark-pool}', checks=[])

        # cancel a spark session statement
        self.cmd('az synapse spark session-statement cancel --id {statement-id} --session-id {session-id} '
                 '--workspace-name {workspace} --spark-pool-name {spark-pool}  --yes', checks=[])

        # delete/cancel a spark session
        self.cmd('az synapse spark session cancel --id {session-id} --workspace-name {workspace} '
                 '--spark-pool-name {spark-pool} --yes', checks=[])

    def _create_workspace(self):
        self.kwargs.update({
            'location': self.location,
            'workspace': self.create_random_name(prefix='clitest', length=16),
            'file-system': 'testfilesystem',
            'account-url': 'https://adlsgen2account.dfs.core.windows.net',
            'login-user': 'cliuser1',
            'login-password': 'Password123!'
        })

        # Wait some time to improve robustness
        if self.is_live or self.in_recording:
            import time
            time.sleep(60)

        # create synapse workspace
        self.cmd(
            'az synapse workspace create --name {workspace} --resource-group {rg} --account-url {account-url} '
            '--file-system {file-system} --sql-admin-login-user {login-user} '
            '--sql-admin-login-password {login-password}'
            ' --location {location}', checks=[])
