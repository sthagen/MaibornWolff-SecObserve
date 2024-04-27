from unittests.access_control.api.test_authorization import (
    APITest,
    TestAuthorizationBase,
)
from unittests.access_control.services.test_authorization import (
    prepare_authorization_groups,
)


class TestAuthorizationObservationLogs(TestAuthorizationBase):
    def test_authorization_observation_logs_product_member(self):
        self._test_authorization_observation_logs()

    def test_authorization_observation_logs_product_authorization_group_member(self):
        prepare_authorization_groups()
        self._test_authorization_observation_logs()

    def _test_authorization_observation_logs(self):
        expected_data = "{'count': 4, 'next': None, 'previous': None, 'results': [{'id': 2, 'observation_title': 'db_observation_internal', 'user_full_name': 'db_internal_write', 'approval_user_full_name': None, 'severity': '', 'status': 'Duplicate', 'comment': 'Set by product rule', 'created': '2022-12-15T17:10:35.524000+01:00', 'vex_justification': '', 'assessment_status': 'Auto approved', 'approval_remark': '', 'approval_date': None, 'observation': 1, 'user': 2, 'approval_user': None, 'general_rule': None, 'product_rule': None}, {'id': 1, 'observation_title': 'db_observation_internal', 'user_full_name': 'db_internal_write', 'approval_user_full_name': None, 'severity': 'Medium', 'status': 'Open', 'comment': 'Set by parser', 'created': '2022-12-15T17:10:35.518000+01:00', 'vex_justification': '', 'assessment_status': 'Auto approved', 'approval_remark': '', 'approval_date': None, 'observation': 1, 'user': 2, 'approval_user': None, 'general_rule': None, 'product_rule': None}, {'id': 4, 'observation_title': 'db_observation_internal', 'user_full_name': 'db_external', 'approval_user_full_name': None, 'severity': '', 'status': 'False positive', 'comment': 'Set by product rule', 'created': '2022-12-15T17:12:23.196000+01:00', 'vex_justification': '', 'assessment_status': 'Auto approved', 'approval_remark': '', 'approval_date': None, 'observation': 2, 'user': 4, 'approval_user': None, 'general_rule': None, 'product_rule': None}, {'id': 3, 'observation_title': 'db_observation_internal', 'user_full_name': 'db_external', 'approval_user_full_name': None, 'severity': 'Medium', 'status': 'Open', 'comment': 'Set by parser', 'created': '2022-12-15T17:11:28.326000+01:00', 'vex_justification': '', 'assessment_status': 'Auto approved', 'approval_remark': '', 'approval_date': None, 'observation': 2, 'user': 4, 'approval_user': None, 'general_rule': None, 'product_rule': None}]}"
        self._test_api(
            APITest(
                "db_admin", "get", "/api/observation_logs/", None, 200, expected_data
            )
        )

        expected_data = "{'count': 2, 'next': None, 'previous': None, 'results': [{'id': 2, 'observation_title': 'db_observation_internal', 'user_full_name': 'db_internal_write', 'approval_user_full_name': None, 'severity': '', 'status': 'Duplicate', 'comment': 'Set by product rule', 'created': '2022-12-15T17:10:35.524000+01:00', 'vex_justification': '', 'assessment_status': 'Auto approved', 'approval_remark': '', 'approval_date': None, 'observation': 1, 'user': 2, 'approval_user': None, 'general_rule': None, 'product_rule': None}, {'id': 1, 'observation_title': 'db_observation_internal', 'user_full_name': 'db_internal_write', 'approval_user_full_name': None, 'severity': 'Medium', 'status': 'Open', 'comment': 'Set by parser', 'created': '2022-12-15T17:10:35.518000+01:00', 'vex_justification': '', 'assessment_status': 'Auto approved', 'approval_remark': '', 'approval_date': None, 'observation': 1, 'user': 2, 'approval_user': None, 'general_rule': None, 'product_rule': None}]}"
        self._test_api(
            APITest(
                "db_internal_write",
                "get",
                "/api/observation_logs/",
                None,
                200,
                expected_data,
            )
        )

        expected_data = "{'id': 1, 'observation_data': {'id': 1, 'product_data': {'id': 1, 'permissions': {<Permissions.VEX_View: 5001>, <Permissions.VEX_Edit: 5002>, <Permissions.VEX_Delete: 5003>, <Permissions.VEX_Create: 5004>, <Permissions.Product_Rule_View: 1301>, <Permissions.Product_Rule_Edit: 1302>, <Permissions.Product_Rule_Delete: 1303>, <Permissions.Product_Rule_Create: 1304>, <Permissions.Product_Rule_Apply: 1305>, <Permissions.Product_Api_Token_Revoke: 4003>, <Permissions.Product_Api_Token_Create: 4004>, <Permissions.Product_Member_View: 1201>, <Permissions.Product_Member_Edit: 1202>, <Permissions.Product_Member_Delete: 1203>, <Permissions.Product_Member_Create: 1204>, <Permissions.Observation_Log_Approval: 2101>, <Permissions.Api_Configuration_View: 3001>, <Permissions.Api_Configuration_Edit: 3002>, <Permissions.Api_Configuration_Delete: 3003>, <Permissions.Api_Configuration_Create: 3004>, <Permissions.Product_Authorization_Group_Member_View: 1601>, <Permissions.Product_Authorization_Group_Member_Edit: 1602>, <Permissions.Product_Authorization_Group_Member_Delete: 1603>, <Permissions.Product_Authorization_Group_Member_Create: 1604>, <Permissions.Product_View: 1101>, <Permissions.Product_Edit: 1102>, <Permissions.Product_Delete: 1103>, <Permissions.Product_Import_Observations: 1105>, <Permissions.Observation_View: 2001>, <Permissions.Observation_Edit: 2002>, <Permissions.Observation_Create: 2004>, <Permissions.Observation_Delete: 2003>, <Permissions.Observation_Assessment: 2005>, <Permissions.Service_View: 1501>, <Permissions.Service_Delete: 1503>, <Permissions.Product_Group_View: 1001>, <Permissions.Product_Group_Edit: 1002>, <Permissions.Product_Group_Delete: 1003>, <Permissions.Branch_View: 1401>, <Permissions.Branch_Edit: 1402>, <Permissions.Branch_Delete: 1403>, <Permissions.Branch_Create: 1404>}, 'product_group_assessments_need_approval': False, 'name': 'db_product_internal', 'description': '', 'purl': '', 'cpe23': '', 'repository_prefix': '', 'repository_branch_housekeeping_active': None, 'repository_branch_housekeeping_keep_inactive_days': None, 'repository_branch_housekeeping_exempt_branches': '', 'security_gate_passed': True, 'security_gate_active': None, 'security_gate_threshold_critical': None, 'security_gate_threshold_high': None, 'security_gate_threshold_medium': None, 'security_gate_threshold_low': None, 'security_gate_threshold_none': None, 'security_gate_threshold_unkown': None, 'apply_general_rules': True, 'notification_ms_teams_webhook': '', 'notification_slack_webhook': '', 'notification_email_to': '', 'issue_tracker_active': False, 'issue_tracker_type': '', 'issue_tracker_base_url': '', 'issue_tracker_username': '', 'issue_tracker_api_key': '', 'issue_tracker_project_id': '', 'issue_tracker_labels': '', 'issue_tracker_issue_type': '', 'issue_tracker_status_closed': '', 'issue_tracker_minimum_severity': '', 'last_observation_change': '2022-12-16T17:13:18.283000+01:00', 'assessments_need_approval': False, 'product_group': 3, 'repository_default_branch': 1}, 'branch_name': 'db_branch_internal_dev', 'parser_data': {'id': 1, 'name': 'db_parser_file', 'type': 'DAST', 'source': 'File'}, 'references': [], 'evidences': [{'id': 1, 'name': 'db_evidence_internal'}], 'origin_source_file_url': None, 'origin_component_purl_type': '', 'origin_component_purl_namespace': '', 'issue_tracker_issue_url': None, 'assessment_needs_approval': None, 'title': 'db_observation_internal', 'description': '', 'recommendation': '', 'current_severity': 'Medium', 'parser_severity': 'Medium', 'rule_severity': '', 'assessment_severity': '', 'current_status': 'Duplicate', 'parser_status': 'Open', 'rule_status': 'Duplicate', 'assessment_status': '', 'scanner_observation_id': '', 'vulnerability_id': '', 'origin_component_name': '', 'origin_component_version': '', 'origin_component_name_version': '', 'origin_component_purl': '', 'origin_component_cpe': '', 'origin_component_dependencies': '', 'origin_docker_image_name': '', 'origin_docker_image_tag': '', 'origin_docker_image_name_tag': '', 'origin_docker_image_name_tag_short': '', 'origin_docker_image_digest': '', 'origin_endpoint_url': '', 'origin_endpoint_scheme': '', 'origin_endpoint_hostname': '', 'origin_endpoint_port': None, 'origin_endpoint_path': '', 'origin_endpoint_params': '', 'origin_endpoint_query': '', 'origin_endpoint_fragment': '', 'origin_service_name': 'db_service_internal_backend', 'origin_source_file': '', 'origin_source_line_start': None, 'origin_source_line_end': None, 'origin_cloud_provider': '', 'origin_cloud_account_subscription_project': '', 'origin_cloud_resource': '', 'origin_cloud_resource_type': '', 'origin_cloud_qualified_resource': '', 'cvss3_score': None, 'cvss3_vector': '', 'cwe': None, 'epss_score': None, 'epss_percentile': None, 'found': None, 'scanner': 'db_parser', 'upload_filename': 'parser.json', 'api_configuration_name': '', 'import_last_seen': '2022-12-15T17:14:20.870000+01:00', 'created': '2022-12-15T17:10:35.513000+01:00', 'modified': '2022-12-16T17:13:18.282000+01:00', 'last_observation_log': '2022-12-16T17:13:18.281000+01:00', 'identity_hash': '6eef8088480aa2523aeeb64ad35f876a942cc3172cfb36752f3a052a4f88642c', 'issue_tracker_issue_id': '', 'issue_tracker_issue_closed': False, 'has_potential_duplicates': False, 'current_vex_justification': '', 'parser_vex_justification': '', 'rule_vex_justification': '', 'assessment_vex_justification': '', 'product': 1, 'branch': 1, 'parser': 1, 'origin_service': 1, 'general_rule': None, 'product_rule': 1}, 'user_full_name': 'db_internal_write', 'approval_user_full_name': None, 'severity': 'Medium', 'status': 'Open', 'comment': 'Set by parser', 'created': '2022-12-15T17:10:35.518000+01:00', 'vex_justification': '', 'assessment_status': 'Auto approved', 'approval_remark': '', 'approval_date': None, 'observation': 1, 'user': 2, 'approval_user': None, 'general_rule': None, 'product_rule': None}"
        self._test_api(
            APITest(
                "db_internal_write",
                "get",
                "/api/observation_logs/1/",
                None,
                200,
                expected_data,
            )
        )

        self._test_api(
            APITest(
                "db_internal_write", "get", "/api/observation_logs/3/", None, 404, None
            )
        )
