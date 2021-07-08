# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_cluster_create
from .example_steps import step_data_connection_event_hub_create
from .example_steps import step_attached_database_configuration_create
from .example_steps import step_attached_database_configuration_show
from .example_steps import step_data_connection_show
from .example_steps import step_database_list
from .example_steps import step_attached_database_configuration_list
from .example_steps import step_database_show
from .example_steps import step_cluster_list_sku
from .example_steps import step_cluster_show
from .example_steps import step_cluster_list2
from .example_steps import step_cluster_list
from .example_steps import step_cluster_list_sku2
from .example_steps import step_data_connection_event_hub_update
from .example_steps import step_data_connection_event
from .example_steps import step_database_remove_principal
from .example_steps import step_database_list_principal
from .example_steps import step_database_add_principal
from .example_steps import step_database_update
from .example_steps import step_cluster_detach_follower_database
from .example_steps import step_cluster_list_follower_database
from .example_steps import step_cluster_start
from .example_steps import step_cluster_stop
from .example_steps import step_cluster_update
from .example_steps import step_attached_database_configuration_delete
from .example_steps import step_data_connection_delete
from .example_steps import step_database_delete
from .example_steps import step_cluster_delete
from .example_steps import step_database_principal_assignment_show
from .example_steps import step_database_principal_assignment_create
from .example_steps import step_database_principal_assignment_delete
from .example_steps import step_cluster_principal_assignment_show
from .example_steps import step_cluster_principal_assignment_create
from .example_steps import step_cluster_principal_assignment_delete
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)
from azure_devtools.scenario_tests import AllowLargeResponse


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test, rg):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test, rg):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test, rg):
    setup_scenario(test, rg)
    step_cluster_create(test, rg, checks=[
        test.check("name", "{myCluster}", case_sensitive=False),
        test.check("identity.type", "SystemAssigned", case_sensitive=False),
        test.check("location", "westus", case_sensitive=False),
        test.check("enableDoubleEncryption", False),
        test.check("enablePurge", True),
        test.check("enableStreamingIngest", True),
        test.check("sku.name", "Standard_L8s", case_sensitive=False),
        test.check("sku.capacity", 2),
        test.check("sku.tier", "Standard", case_sensitive=False),
    ])
    # STEP NOT FOUND: KustoDatabasesCreateOrUpdate
    step_data_connection_event_hub_create(test, rg, checks=[])
    step_attached_database_configuration_create(test, rg, checks=[
        test.check("location", "westus", case_sensitive=False),
        test.check("clusterResourceId", "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Kusto"
                   "/Clusters/{myCluster3}", case_sensitive=False),
        test.check("defaultPrincipalsModificationKind", "Union", case_sensitive=False),
        test.check("tableLevelSharingProperties.externalTablesToExclude[0]", "ExternalTable2", case_sensitive=False),
        test.check("tableLevelSharingProperties.externalTablesToInclude[0]", "ExternalTable1", case_sensitive=False),
        test.check("tableLevelSharingProperties.materializedViewsToExclude[0]", "MaterializedViewTable2",
                   case_sensitive=False),
        test.check("tableLevelSharingProperties.materializedViewsToInclude[0]", "MaterializedViewTable1",
                   case_sensitive=False),
        test.check("tableLevelSharingProperties.tablesToExclude[0]", "Table2", case_sensitive=False),
        test.check("tableLevelSharingProperties.tablesToInclude[0]", "Table1", case_sensitive=False),
    ])
    step_attached_database_configuration_show(test, rg, checks=[
        test.check("location", "westus", case_sensitive=False),
        test.check("defaultPrincipalsModificationKind", "Union", case_sensitive=False),
        test.check("tableLevelSharingProperties.externalTablesToExclude[0]", "ExternalTable2", case_sensitive=False),
        test.check("tableLevelSharingProperties.externalTablesToInclude[0]", "ExternalTable1", case_sensitive=False),
        test.check("tableLevelSharingProperties.materializedViewsToExclude[0]", "MaterializedViewTable2",
                   case_sensitive=False),
        test.check("tableLevelSharingProperties.materializedViewsToInclude[0]", "MaterializedViewTable1",
                   case_sensitive=False),
        test.check("tableLevelSharingProperties.tablesToExclude[0]", "Table2", case_sensitive=False),
        test.check("tableLevelSharingProperties.tablesToInclude[0]", "Table1", case_sensitive=False),
    ])
    step_data_connection_show(test, rg, checks=[
        test.check("location", "westus", case_sensitive=False),
        test.check("consumerGroup", "testConsumerGroup1", case_sensitive=False),
        test.check("eventHubResourceId", "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Even"
                   "tHub/namespaces/eventhubTestns1/eventhubs/eventhubTest1", case_sensitive=False),
        test.check("managedIdentityResourceId", "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microso"
                   "ft.ManagedIdentity/userAssignedIdentities/managedidentityTest1", case_sensitive=False),
    ])
    step_database_list(test, rg, checks=[])
    step_attached_database_configuration_list(test, rg, checks=[
        test.check('length(@)', 1),
    ])
    step_database_show(test, rg, checks=[])
    step_database_list(test, rg, checks=[])
    step_cluster_list_sku(test, rg, checks=[])
    step_cluster_show(test, rg, checks=[
        test.check("name", "{myCluster}", case_sensitive=False),
        test.check("identity.type", "SystemAssigned", case_sensitive=False),
        test.check("location", "westus", case_sensitive=False),
        test.check("enableStreamingIngest", True),
        test.check("sku.name", "Standard_L8s", case_sensitive=False),
        test.check("sku.capacity", 2),
        test.check("sku.tier", "Standard", case_sensitive=False),
    ])
    step_cluster_list2(test, rg, checks=[
        test.check('length(@)', 1),
    ])
    step_cluster_list(test, rg, checks=[
        test.check('length(@)', 1),
    ])
    step_cluster_list_sku2(test, rg, checks=[])
    # STEP NOT FOUND: KustoOperationsList
    step_data_connection_event_hub_update(test, rg, checks=[])
    step_data_connection_event(test, rg, checks=[])
    # STEP NOT FOUND: KustoDataConnectionsCheckNameAvailability
    step_database_remove_principal(test, rg, checks=[])
    step_database_list_principal(test, rg, checks=[])
    step_database_add_principal(test, rg, checks=[])
    step_database_update(test, rg, checks=[])
    step_cluster_detach_follower_database(test, rg, checks=[])
    # STEP NOT FOUND: KustoDatabaseCheckNameAvailability
    step_cluster_list_follower_database(test, rg, checks=[])
    step_cluster_start(test, rg, checks=[])
    step_cluster_stop(test, rg, checks=[])
    step_cluster_update(test, rg, checks=[
        test.check("name", "{myCluster}", case_sensitive=False),
        test.check("identity.type", "SystemAssigned", case_sensitive=False),
        test.check("location", "westus", case_sensitive=False),
        test.check("enablePurge", True),
        test.check("enableStreamingIngest", True),
        test.check("engineType", "V2", case_sensitive=False),
        test.check("keyVaultProperties.keyName", "keyName", case_sensitive=False),
        test.check("keyVaultProperties.keyVaultUri", "https://dummy.keyvault.com", case_sensitive=False),
        test.check("keyVaultProperties.keyVersion", "keyVersion", case_sensitive=False),
    ])
    # STEP NOT FOUND: KustoClustersCheckNameAvailability
    step_attached_database_configuration_delete(test, rg, checks=[])
    step_data_connection_delete(test, rg, checks=[])
    step_database_delete(test, rg, checks=[])
    step_cluster_delete(test, rg, checks=[])
    step_database_principal_assignment_show(test, rg, checks=[])
    step_database_principal_assignment_create(test, rg, checks=[])
    step_database_principal_assignment_delete(test, rg, checks=[])
    step_cluster_principal_assignment_show(test, rg, checks=[])
    step_cluster_principal_assignment_create(test, rg, checks=[])
    step_cluster_principal_assignment_delete(test, rg, checks=[])
    cleanup_scenario(test, rg)


# Test class for Scenario
@try_manual
class KustoScenarioTest(ScenarioTest):

    def __init__(self, *args, **kwargs):
        super(KustoScenarioTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

    @AllowLargeResponse(size_kb=5000)
    @ResourceGroupPreparer(name_prefix='clitestkusto_kustorptest'[:7], key='rg', parameter_name='rg')
    def test_kusto_Scenario(self, rg):
        call_scenario(self, rg)
        calc_coverage(__file__)
        raise_if()
