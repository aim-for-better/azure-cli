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

helps['synapse workspace'] = """
type: group
short-summary: Create, Show, List, ListByResourceGroup, Delete workspace.
"""

helps['synapse workspace create'] = """
type: command
short-summary: create a synapse workspace.
long-summary: create a synapse workspace.
examples:
  - name: Create a synapse workspace
    text: |-
        az synapse workspace create --resource-group zzy-test-rg --name fromcli4 \\
          --account-url https://newzzyadlsgen2.dfs.core.windows.net --file-system testfilesystem \\
          --sql-admin-login-user cliuser1 --sql-admin-login-password Password123! --location "East US"
"""

helps['synapse workspace list'] = """
type: command
short-summary: list all synapse workspaces under a subscription.
long-summary: list all synapse workspaces under a subscription
examples:
  - name: List all synapse workspaces under a subscription
    text: |-
        az synapse workspace list
"""

helps['synapse workspace list-by-resource-group'] = """
type: command
short-summary: list all synapse workspaces under a resource group.
long-summary: list all synapse workspaces under a resource group.
examples:
  - name: List all synapse workspaces under a resource group.
    text: |-
        az synapse workspace list-by-resource-group --resource-group zzy-test-rg 
"""

helps['synapse workspace show'] = """
type: command
short-summary: get a synapse workspaces with workspace name.
long-summary: get a synapse workspaces with workspace name.
examples:
  - name: Get a synapse workspaces with workspace name.
    text: |-
        az synapse workspace show --resource-group zzy-test-rg --name testsynapseworkspace 
"""

helps['synapse workspace delete'] = """
type: command
short-summary: delete a synapse workspaces with workspace name.
long-summary: delete a synapse workspaces with workspace name.
examples:
  - name: Delete a synapse workspaces with workspace name.
    text: |-
        az synapse workspace delete --resource-group zzy-test-rg --name testsynapseworkspace 
"""

helps['synapse big-data-pool'] = """
type: group
short-summary: Create, Get, List, Delete big data pool.
"""

helps['synapse big-data-pool create'] = """
type: command
short-summary: Create a big data pool(spark pool).
long-summary: Create a big data pool(spark pool) with default configuration.
examples:
  - name: Submit a java spark batch job to a specific spark pool.
    text: |-
        az synapse big-data-pool create --resource-group zzy-test-rg --name testsynapseworkspace \\
        --big-data-pool-name testpool --location "East US"
"""

helps['synapse big-data-pool list'] = """
type: command
short-summary: List all big data pools(spark pools).
long-summary: List all big data pools(spark pools) under a workspace.
examples:
  - name: List all big data pools(spark pools) under a workspace.
    text: |-
        az synapse big-data-pool list --resource-group zzy-test-rg --name testsynapseworkspace
"""

helps['synapse big-data-pool show'] = """
type: command
short-summary: Get a specific big data pools(spark pools) with big data pool name.
long-summary: Get a specific big data pools(spark pools) with big data pool name.
examples:
  - name: Get a specific big data pools(spark pools) with big data pool name.
    text: |-
        az synapse big-data-pool show --resource-group zzy-test-rg --name testsynapseworkspace \\
        --big-data-pool-name testpool
"""

helps['synapse big-data-pool delete'] = """
type: command
short-summary: Delete a specific big data pools(spark pools) with big data pool name.
long-summary: Delete a specific big data pools(spark pools) with big data pool name.
examples:
  - name: Delete a specific big data pools(spark pools) with big data pool name.
    text: |-
        az synapse big-data-pool delete --resource-group zzy-test-rg --name testsynapseworkspace \\
        --big-data-pool-name testpool
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
  - name: Get a spark batch job under the specific spark pool with batch id.
    text: |-
        az synapse spark-batch show --name testsynapseworkspace --spark-pool-name testsparkpool --batch-id 1
"""

helps['synapse spark-batch cancel'] = """
type: command
short-summary: cancel a specific spark batch job under the specific spark pool.
long-summary: cancle the spark batch job under the specific spark pool with batch id.
examples:
  - name: Cancel a spark batch job under the specific spark pool with batch id.
    text: |-
        az synapse spark-batch cancel --name testsynapseworkspace --spark-pool-name testsparkpool --batch-id 1
"""

helps['synapse spark-session'] = """
type: group
short-summary: Create, Get, List, Cancel spark session job. 
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
  - name: Get a spark session job under the specific spark pool with batch id.
    text: |-
        az synapse spark-session show --name testsynapseworkspace --spark-pool-name testsparkpool --session-id 1
"""

helps['synapse spark-session cancel'] = """
type: command
short-summary: cancel a specific spark session job under the specific spark pool.
long-summary: cancle the spark session job under the specific spark pool with batch id.
examples:
  - name: Cancel a spark session job under the specific spark pool with batch id.
    text: |-
        az synapse spark-session cancel --name testsynapseworkspace --spark-pool-name testsparkpool --session-id 1
"""

helps['synapse spark-statement'] = """
type: group
short-summary: Create, Get, List, Cancel spark statement. 
"""

helps['synapse spark-statement create'] = """
type: command
short-summary: Submit a spark statement to a spark session.
long-summary: Submit a spark statement to a spark session.
examples:
  - name: Submit a spark statement to a spark session
    text: |-
        az synapse spark-statement create --name testsynapseworkspace --spark-pool-name testsparkpool \\
        --session-id 8 --code "print(\"hello,azure cli\")" --kind pyspark
"""

helps['synapse spark-statement show'] = """
type: command
short-summary: get a spark statement with statement id.
long-summary: get a spark statement with statement id.
examples:
  - name: Get a spark statement with statement id
    text: |-
        az synapse spark-statement show --name testsynapseworkspace --spark-pool-name testsparkpool \\
        --session-id 11 --statement-id 1
"""

helps['synapse spark-statement list'] = """
type: command
short-summary: list all spark statements under the specify spark session.
long-summary: list all spark statements under the specify spark session.
examples:
  - name: List all spark statements under the specify spark session
    text: |-
        az synapse spark-statement list --name testsynapseworkspace --spark-pool-name testsparkpool --session-id 11
"""

helps['synapse spark-statement cancel'] = """
type: command
short-summary: cancel a spark statement with statement id.
long-summary: cancel a spark statement with statement id.
examples:
  - name: Cancel a spark statement with statement id
    text: |-
        az synapse spark-statement cancel --name testsynapseworkspace --spark-pool-name testsparkpool \\
        --session-id 11 --statement-id 1
"""
