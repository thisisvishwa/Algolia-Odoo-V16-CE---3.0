# Odoo eCommerce Algolia Search Integration Developer Guide

## Introduction

This guide provides technical details for developers to install, configure, and customize the Algolia search integration for Odoo Version 16 Community Edition eCommerce websites.

## Installation

To install the Algolia search integration module, follow these steps:

1. Navigate to your Odoo addons directory.
2. Clone or download the module into the addons directory.
3. Update the Odoo app list by navigating to Apps -> Update Apps List.
4. Install the module by searching for 'Algolia eCommerce Search' and clicking the 'Install' button.

## Configuration

### Setting up Algolia

Before configuring the module in Odoo, you need to set up your Algolia account:

1. Sign up for an Algolia account at https://www.algolia.com/.
2. Create a new index for your Odoo products.
3. Obtain your Application ID and Admin API Key from the Algolia dashboard.

### Configuring Algolia in Odoo

To configure Algolia settings in Odoo:

1. Go to the Odoo Backend module.
2. Navigate to the Algolia Settings view (`algolia_settings_view`).
3. Enter your Algolia Application ID and Admin API Key in the respective fields (`algolia_api_key_field`).

## Synchronization

To synchronize your product data with Algolia:

1. Run the synchronization script located at `data/algolia_data.xml`.
2. Ensure that the product data schema matches the Algolia index configuration.

## Customization

### Modifying Search Templates

To customize the search interface:

1. Edit the `views/search_template.xml` file to modify the search bar layout.
2. Adjust the `views/search_results_page.xml` file to change the appearance of the search results page.
3. Use the `static/src/css/search_styles.css` file to apply custom styles.

### Adding Responsive Design

To enhance mobile responsiveness:

1. Modify the `views/responsive_design.xml` file to adjust the search components for different screen sizes.
2. Utilize the `.responsive-element` class in the `static/src/css/search_styles.css` file to style responsive elements.

## JavaScript Functions

The following JavaScript functions are used for search functionality:

- `initAlgoliaSearch()`: Initializes the Algolia search client.
- `updateSearchResults()`: Updates the DOM with new search results.
- `handleSearchInput()`: Manages the search input and suggestions logic.
- `applyFacetFilter()`: Applies a selected facet filter to the search.
- `removeFacetFilter()`: Removes a selected facet filter from the search.

These functions are defined in `static/src/js/search_autocomplete.js` and `static/src/js/search_filters.js`.

## Testing

To run tests:

1. Execute the `tests/test_algolia_integration.py` script to test Algolia API integration.
2. Run the `tests/test_search_features.py` script to test search features like typo-tolerance and faceting.

## Translation

To add translations for search-related terms:

1. Edit the `i18n/en_US.po` file to include translations for terms like `search_placeholder`, `search_no_results`, and `search_error_message`.

## Module Initialization

To initialize the module:

1. Import the necessary modules in the `__init__.py` file:
   ```python
   from . import controllers
   from . import models
   ```
2. Define the module metadata in the `__manifest__.py` file:
   ```python
   {
       'name': 'Algolia eCommerce Search',
       'depends': ['base', 'website_sale'],
       'data': [
           'views/algolia_settings.xml',
           'views/search_template.xml',
           'views/search_results_page.xml',
           'views/responsive_design.xml',
           'data/algolia_data.xml',
           'security/ir.model.access.csv',
       ],
       'qweb': [
           'static/src/xml/*.xml',
       ],
   }
   ```

## Conclusion

This guide provides the necessary steps and information for developers to integrate and customize the Algolia search functionality within an Odoo Version 16 Community Edition eCommerce website. For further assistance, refer to the Algolia API documentation and Odoo developer resources.