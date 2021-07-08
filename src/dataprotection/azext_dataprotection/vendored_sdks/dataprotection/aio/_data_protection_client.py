# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6375, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import DataProtectionClientConfiguration
from .operations import BackupVaultsOperations
from .operations import OperationResultOperations
from .operations import OperationStatusOperations
from .operations import BackupVaultOperationResultsOperations
from .operations import DataProtectionOperations
from .operations import DataProtectionOperationsOperations
from .operations import BackupPoliciesOperations
from .operations import BackupInstancesOperations
from .operations import RecoveryPointsOperations
from .operations import JobsOperations
from .operations import RestorableTimeRangesOperations
from .operations import ExportJobsOperations
from .operations import ExportJobsOperationResultOperations
from .. import models


class DataProtectionClient(object):
    """Open API 2.0 Specs for Azure Data Protection service.

    :ivar backup_vaults: BackupVaultsOperations operations
    :vartype backup_vaults: data_protection_client.aio.operations.BackupVaultsOperations
    :ivar operation_result: OperationResultOperations operations
    :vartype operation_result: data_protection_client.aio.operations.OperationResultOperations
    :ivar operation_status: OperationStatusOperations operations
    :vartype operation_status: data_protection_client.aio.operations.OperationStatusOperations
    :ivar backup_vault_operation_results: BackupVaultOperationResultsOperations operations
    :vartype backup_vault_operation_results: data_protection_client.aio.operations.BackupVaultOperationResultsOperations
    :ivar data_protection: DataProtectionOperations operations
    :vartype data_protection: data_protection_client.aio.operations.DataProtectionOperations
    :ivar data_protection_operations: DataProtectionOperationsOperations operations
    :vartype data_protection_operations: data_protection_client.aio.operations.DataProtectionOperationsOperations
    :ivar backup_policies: BackupPoliciesOperations operations
    :vartype backup_policies: data_protection_client.aio.operations.BackupPoliciesOperations
    :ivar backup_instances: BackupInstancesOperations operations
    :vartype backup_instances: data_protection_client.aio.operations.BackupInstancesOperations
    :ivar recovery_points: RecoveryPointsOperations operations
    :vartype recovery_points: data_protection_client.aio.operations.RecoveryPointsOperations
    :ivar jobs: JobsOperations operations
    :vartype jobs: data_protection_client.aio.operations.JobsOperations
    :ivar restorable_time_ranges: RestorableTimeRangesOperations operations
    :vartype restorable_time_ranges: data_protection_client.aio.operations.RestorableTimeRangesOperations
    :ivar export_jobs: ExportJobsOperations operations
    :vartype export_jobs: data_protection_client.aio.operations.ExportJobsOperations
    :ivar export_jobs_operation_result: ExportJobsOperationResultOperations operations
    :vartype export_jobs_operation_result: data_protection_client.aio.operations.ExportJobsOperationResultOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = DataProtectionClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.backup_vaults = BackupVaultsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation_result = OperationResultOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation_status = OperationStatusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.backup_vault_operation_results = BackupVaultOperationResultsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_protection = DataProtectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_protection_operations = DataProtectionOperationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.backup_policies = BackupPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.backup_instances = BackupInstancesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.recovery_points = RecoveryPointsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.jobs = JobsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.restorable_time_ranges = RestorableTimeRangesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.export_jobs = ExportJobsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.export_jobs_operation_result = ExportJobsOperationResultOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "DataProtectionClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
