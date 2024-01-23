from odoo import http
from odoo.http import request

class AlgoliaSearchController(http.Controller):

    @http.route('/shop/search', type='http', auth="public", website=True)
    def search(self, **post):
        search_query = post.get('search', '').strip()
        if search_query:
            # Initialize Algolia search
            algolia_search = request.env['algolia_integration'].sudo().initAlgoliaSearch()
            # Perform the search
            results = algolia_search.search(search_query)
            # Render the search results page with the found items
            return request.render('your_module_name.search_results_page', {
                'search_results': results['hits'],
                'search_query': search_query,
                'facets': results.get('facets', {}),
                'pagination': results.get('pagination', {}),
            })
        else:
            # If there is no search query, redirect to the shop page
            return request.redirect('/shop')

    @http.route('/shop/search/autocomplete', type='json', auth="public", website=True)
    def autocomplete(self, **post):
        search_query = post.get('search', '').strip()
        if search_query:
            # Initialize Algolia search
            algolia_search = request.env['algolia_integration'].sudo().initAlgoliaSearch()
            # Get autocomplete suggestions
            suggestions = algolia_search.suggest(search_query)
            return suggestions
        return []

    @http.route('/shop/search/filters', type='http', auth="public", website=True)
    def filters(self, **post):
        # Retrieve selected filters from the request
        selected_filters = post.get('filters', {})
        # Initialize Algolia search
        algolia_search = request.env['algolia_integration'].sudo().initAlgoliaSearch()
        # Apply filters to the search
        results = algolia_search.search_with_filters(selected_filters)
        # Render the search results page with the filtered items
        return request.render('your_module_name.search_results_page', {
            'search_results': results['hits'],
            'search_query': post.get('search', ''),
            'facets': results.get('facets', {}),
            'selected_filters': selected_filters,
            'pagination': results.get('pagination', {}),
        })