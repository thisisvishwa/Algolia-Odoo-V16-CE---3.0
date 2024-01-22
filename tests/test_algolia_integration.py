from odoo.tests.common import TransactionCase
from odoo.exceptions import AccessError

class TestAlgoliaIntegration(TransactionCase):

    def setUp(self):
        super(TestAlgoliaIntegration, self).setUp()
        # Setup test data and environment
        self.AlgoliaIntegration = self.env['algolia_integration.algolia_integration']

    def test_algolia_api_connection(self):
        # Test the connection to the Algolia API
        algolia_integration = self.AlgoliaIntegration.create({
            'name': 'Test Connection',
            'algolia_api_key': 'fake_api_key',
            'algolia_app_id': 'fake_app_id'
        })
        self.assertTrue(algolia_integration.check_connection(), "Algolia API connection should be successful with correct credentials")

    def test_search_performance(self):
        # Test the search performance and accuracy
        algolia_integration = self.AlgoliaIntegration.create({
            'name': 'Test Search Performance',
            'algolia_api_key': 'fake_api_key',
            'algolia_app_id': 'fake_app_id'
        })
        search_results = algolia_integration.perform_search('test query')
        self.assertIsInstance(search_results, list, "Search results should be a list")
        self.assertTrue(all(isinstance(result, dict) for result in search_results), "Each search result should be a dictionary")

    def test_typo_tolerance(self):
        # Test the typo-tolerance feature
        algolia_integration = self.AlgoliaIntegration.create({
            'name': 'Test Typo Tolerance',
            'algolia_api_key': 'fake_api_key',
            'algolia_app_id': 'fake_app_id'
        })
        search_results_with_typo = algolia_integration.perform_search('tset query')
        search_results_without_typo = algolia_integration.perform_search('test query')
        self.assertEqual(search_results_with_typo, search_results_without_typo, "Search results with typo should match those without typo due to typo-tolerance")

    def test_faceting_and_filtering(self):
        # Test faceting and filtering features
        algolia_integration = self.AlgoliaIntegration.create({
            'name': 'Test Faceting and Filtering',
            'algolia_api_key': 'fake_api_key',
            'algolia_app_id': 'fake_app_id'
        })
        filtered_results = algolia_integration.perform_search('test query', filters={'category': 'electronics'})
        self.assertTrue(all('electronics' in result.get('category', []) for result in filtered_results), "All filtered results should belong to the 'electronics' category")

    def test_access_rights(self):
        # Test the access rights for the Algolia integration model
        with self.assertRaises(AccessError):
            self.env['algolia_integration.algolia_integration'].with_user(self.env.ref('base.user_demo')).create({
                'name': 'Test Access Rights',
                'algolia_api_key': 'fake_api_key',
                'algolia_app_id': 'fake_app_id'
            })