# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

def load_command_table(self, _):
    from azure.cli.core.commands import CliCommandType
    from azure.cli.core.profiles import ResourceType
    from ._client_factory import synapse_data_plane_factory
    from ._client_factory import cf_synapse_spark_batch
    from ._client_factory import cf_synapse_spark_session

    synapse_data_sdk = CliCommandType(
        operation_tmpl='azure.synapse.synapse_client#SynapseClient.{}',
        client_factory=synapse_data_plane_factory,
        resource_type=ResourceType.DATA_SYNAPSE
    )
    synapse_spark_batch_sdk = CliCommandType(
        operation_tmpl='azure.synapse.operations#SparkBatchOperations.{}',
        client_factory=cf_synapse_spark_batch
    )

    synapse_spark_session_sdk= CliCommandType(
        operations_tmpl='azure.synapse.operations#SparkSessionOperations.{}',
        client_factory=cf_synapse_spark_session
    )

    # Data Plane Commands
    # Spark batch opertions
    with self.command_group('synapse spark-batch', synapse_spark_batch_sdk, client_factory=cf_synapse_spark_batch) as g:
        g.custom_command('create', 'create_spark_batch_job', supports_no_wait=True)
        g.custom_command('list', 'list_spark_batch_jobs')
        g.custom_command('show', 'get_spark_batch_job')
        g.custom_command('delete', 'delete_spark_batch_job', confirmation=True, supports_no_wait=True)

    # Spark session operations
    with self.command_group('synapse spark-session', synapse_spark_session_sdk, client_factory=cf_synapse_spark_session)\
            as g:
        g.custom_command('create', 'create_spark_session_job', supports_no_wait=True)
        g.custom_command('list', 'list_spark_session_jobs')
        g.custom_command('show', 'get_spark_session_job')
        g.custom_command('delete', 'delete_spark_session_job', confirmation=True, supports_no_wait=True)
        g.custom_command('reset-timeout', 'reset_timeout')

    # Spark session statements operations
    with self.command_group('synapse spark-statement', synapse_spark_session_sdk,\
                             client_factory=cf_synapse_spark_session) as g:
        g.custom_command('create', 'create_spark_session_statement', supports_no_wait=True)
        g.custom_command('list', 'list_spark_session_statements')
        g.custom_command('show', 'get_spark_session_statement')
        g.custom_command('delete', 'delete_spark_session_statement', confirmation=True, supports_no_wait=True)
