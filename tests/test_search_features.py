from odoo.tests.common import TransactionCase

class TestSearchFeatures(TransactionCase):

    def setUp(self):
        super(TestSearchFeatures, self).setUp()
        # Setup test data if necessary
        self.AlgoliaIntegration = self.env['algolia_integration.algolia_integration']

    def test_algolia_api_connection(self):
        """Test the connection to Algolia API."""
        algolia_integration = self.AlgoliaIntegration.create({
            'name': 'Test Connection',
            'algolia_api_key': 'fake_api_key',
            'algolia_app_id': 'fake_app_id'
        })
        self.assertTrue(algolia_integration.check_connection(), "Algolia API connection should be successful with correct credentials")

    def test_search_performance(self):
        """Test search performance and accuracy."""
        # Assuming there's a method to measure search performance
        search_performance = self.AlgoliaIntegration.search_performance('test query')
        self.assertLess(search_performance['time_taken'], 200, "Search should be performed under 200ms")

    def test_typo_tolerance(self):
        """Test typo-tolerance feature."""
        # Assuming there's a method to test typo tolerance
        search_results_with_typo = self.AlgoliaIntegration.search('iphnoe')
        search_results_without_typo = self.AlgoliaIntegration.search('iphone')
        self.assertEqual(search_results_with_typo, search_results_without_typo, "Search results should be the same with and without typos")

    def test_faceting_and_filtering(self):
        """Test faceting and filtering features."""
        # Assuming there's a method to apply filters and facets
        filtered_results = self.AlgoliaIntegration.search('phone', filters={'category': 'electronics'})
        for result in filtered_results:
            self.assertEqual(result['category'], 'electronics', "All search results should be in the 'electronics' category")