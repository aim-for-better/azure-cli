# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import
# pylint: disable=line-too-long, too-many-lines


helps['synapse'] = """
type: group
short-summary: Manage and operate Synapse Workspace, BigDataPool, SqlPool.
"""

helps['synapse spark-batch'] = """
type: group
short-summary: Create, Get, List, Delete spark batch job.
"""

helps['synapse spark-batch create'] = """
type: command
short-summary: Submit spark batch job.
long-summary: Submit a spark batch job to a specific spark pool.
examples:
  - name: Submit a java spark batch job to a specific spark pool.
    text: |-
        az synapse spark-batch create --name testsynapseworkspace --spark-pool-name testsparkpool \\
          --job-name WordCount_Java \\
          --file abfss://testfilesystem@newzzyadlsgen2.dfs.core.windows.net/samples/java/wordcount/wordcount.jar \\
          --class-name WordCount \\
          --args abfss://testfilesystem@newzzyadlsgen2.dfs.core.windows.net/samples/java/wordcount/shakespeare.txt \\
          abfss://testfilesystem@newzzyadlsgen2.dfs.core.windows.net/samples/java/wordcount/result/ \\
          --driver-memory 4g --driver-cores 4 --executor-memory 4g --executor-cores 4 --num-executors 2
"""

helps['synapse spark-batch list'] = """
type: command
short-summary: list all spark batch jobs under the specific spark pool.
long-summary: list all spark batch jobs under the specific spark pool.
examples:
  - name: List all spark batch job under the specific spark pool.
    text: |-
        az synapse spark-batch list --name testsynapseworkspace --spark-pool-name testsparkpool
"""

helps['synapse spark-batch show'] = """
type: command
short-summary: get a specific spark batch job under the specific spark pool.
long-summary: get the spark batch job under the specific spark pool with batch id.
examples:
  - name: get a spark batch job under the specific spark pool with batch id.
    text: |-
        az synapse spark-batch show --name testsynapseworkspace --spark-pool-name testsparkpool --batch-id 1
"""

helps['synapse spark-batch delete'] = """
type: command
short-summary: cancel a specific spark batch job under the specific spark pool.
long-summary: cancle the spark batch job under the specific spark pool with batch id.
examples:
  - name: cancel a spark batch job under the specific spark pool with batch id.
    text: |-
        az synapse spark-batch delete --name testsynapseworkspace --spark-pool-name testsparkpool --batch-id 1
"""

helps['synapse spark-session'] = """
type: group
short-summary: Create, Get, List, Delete spark session job. 
"""

helps['synapse spark-session create'] = """
type: command
short-summary: Submit a spark session job
long-summary: Submit a spark session job to a specific spark pool.
examples:
  - name: Submit a spark session job under the specific spark pool.
    text: |-
        az synapse spark-session create --name testsynapseworkspace --spark-pool-name testsparkpool \\
        --job-name testsession --driver-memory 4g --driver-cores 4 \\
        --executor-memory 4g --executor-cores 4 --num-executors 2
"""

helps['synapse spark-session list'] = """
type: command
short-summary: list all spark session jobs under the specific spark pool.
long-summary: list all spark session jobs under the specific spark pool.
examples:
  - name: List all spark session jobs under the specific spark pool.
    text: |-
        az synapse spark-session list --name testsynapseworkspace --spark-pool-name testsparkpool
"""

helps['synapse spark-session show'] = """
type: command
short-summary: get a specific spark session job under the specific spark pool.
long-summary: get the spark session job under the specific spark pool with batch id.
examples:
  - name: get a spark session job under the specific spark pool with batch id.
    text: |-
        az synapse spark-session show --name testsynapseworkspace --spark-pool-name testsparkpool --session-id 1
"""

helps['synapse spark-session delete'] = """
type: command
short-summary: cancel a specific spark session job under the specific spark pool.
long-summary: cancle the spark session job under the specific spark pool with batch id.
examples:
  - name: cancel a spark session job under the specific spark pool with batch id.
    text: |-
        az synapse spark-session delete --name testsynapseworkspace --spark-pool-name testsparkpool --session-id 1
"""
