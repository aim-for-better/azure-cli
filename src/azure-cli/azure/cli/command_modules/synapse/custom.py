# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from knack.prompting import prompt_pass, NoTTYException
from knack.util import CLIError
from azure.cli.core.util import sdk_no_wait

from azure.synapse.models import ExtendedLivyBatchRequest, ExtendedLivyListBatchResponse, ExtendedLivyBatchResponse, \
    ExtendedLivySessionRequest, ExtendedLivyListSessionResponse, ExtendedLivySessionResponse, LivyStatementRequestBody,\
    LivyStatementResponseBody

logger = get_logger(__name__)


# pylint: disable=too-many-locals, too-many-branches, too-many-statements, unused-argument
def list_spark_batch_jobs(cmd, client, workspace_name, spark_pool_name, from_index=None, size=None, detailed=None):
    print("hello,world, list spark batch job")
    return client.list(workspace_name, spark_pool_name, from_index, size, detailed)


def create_spark_batch_job(cmd, client, workspace_name, spark_pool_name, job_name, file, class_name,
                           args, driver_memory, driver_cores, executor_memory, executor_cores,
                           num_executors, jars=None, files=None, archives=None, conf=None, artifact_id=None,
                           tags=None, detailed=None):
    print("create spark batch job")
    print("The parameter is as bellow:\n")
    print(
        "workspace: " + workspace_name + " sparkpool: " + spark_pool_name + " jobname: " + job_name + " class name: " + class_name
        + "file: " + file + " args: " + str(args) + " driver-memory " + driver_memory)

    livy_batch_request = ExtendedLivyBatchRequest(
        tags=tags, artifact_id=artifact_id,
        name=job_name, file=file, class_name=class_name, args=args, jars=jars, files=files, archives=archives,
        conf=conf, driver_memory=driver_memory, driver_cores=driver_cores, executor_memory=executor_memory,
        executor_cores=executor_cores, num_executors=num_executors)

    return client.create(workspace_name, spark_pool_name, livy_batch_request, detailed)


def get_spark_batch_job(cmd, client, workspace_name, spark_pool_name, batch_id, detailed=None):
    print("get spark batch job")
    return client.get(workspace_name, spark_pool_name, batch_id, detailed)


def delete_spark_batch_job(cmd, client, workspace_name, spark_pool_name, batch_id):
    return client.delete(workspace_name, spark_pool_name, batch_id)

# Spark Session
def list_spark_session_jobs(cmd, client, workspace_name, spark_pool_name, from_index=None, size=None, detailed=None):
    print("hello,world, list spark session job")
    return client.list(workspace_name, spark_pool_name, from_index, size, detailed)


def create_spark_session_job(cmd, client, workspace_name, spark_pool_name,driver_memory, driver_cores,
                             executor_memory, executor_cores, num_executors, job_name=None, file=None, class_name=None,
                             args=None,  jars=None, files=None, archives=None, conf=None, artifact_id=None,
                             tags=None, detailed=None):

    print("The parameter is as bellow:\n")
    print(
        "workspace: " + workspace_name + " sparkpool: " + spark_pool_name + " driver-memory " + driver_memory)

    livy_session_request = ExtendedLivySessionRequest(
        tags=tags, artifact_id=artifact_id,
        name=job_name, file=file, class_name=class_name, args=args, jars=jars, files=files, archives=archives,
        conf=conf, driver_memory=driver_memory, driver_cores=driver_cores, executor_memory=executor_memory,
        executor_cores=executor_cores, num_executors=num_executors)

    return client.create(workspace_name, spark_pool_name, livy_session_request, detailed)


def get_spark_session_job(cmd, client, workspace_name, spark_pool_name, session_id, detailed=None):
    print("get spark session job")
    return client.get(workspace_name, spark_pool_name, session_id, detailed)


def delete_spark_session_job(cmd, client, workspace_name, spark_pool_name, session_id):
    return client.delete(workspace_name, spark_pool_name, session_id)


def reset_timeout(cmd, client, workspace_name, spark_pool_name, session_id):
    return client.reset_timeout(workspace_name, spark_pool_name, session_id)


def list_spark_session_statements(cmd, client, workspace_name, spark_pool_name, session_id):
    print("list spark session statements")
    return client.list_statements(workspace_name, spark_pool_name, session_id)


def create_spark_session_statement(cmd, client, workspace_name, spark_pool_name, session_id, code, kind):
    print("create spark session statements")
    livy_statement_request=LivyStatementRequestBody(code=code, kind=kind)
    return client.create_statement(workspace_name, spark_pool_name, session_id, livy_statement_request)


def get_spark_session_statement(cmd, client, workspace_name, spark_pool_name, session_id, statement_id):
    print("get spark session statement.")
    return client.get_statement(workspace_name, spark_pool_name, session_id, statement_id)


def delete_spark_session_statement(cmd, client, workspace_name, spark_pool_name, session_id, statement_id):
    print("delete spark session statement.")
    return client.delete_statement(workspace_name, spark_pool_name, session_id, statement_id)


def get_workspace(cmd, client, resource_group_name, workspace_name):
    print("get synapse workspace")
    return client.get(resource_group_name, workspace_name)


def get_bigdatapool(cmd, client, resource_group_name, workspace_name, bigdatapool_name):
    print("get synapse bigdatapool")
    return client.get(resource_group_name, workspace_name, bigdatapool_name)
