from odoo import models, fields, api
from odoo.exceptions import UserError
import logging
import requests

_logger = logging.getLogger(__name__)

class AlgoliaIntegration(models.Model):
    _name = 'algolia.integration'
    _description = 'Algolia Integration for Odoo eCommerce'

    algolia_app_id = fields.Char(string='Algolia Application ID', required=True)
    algolia_api_key = fields.Char(string='Algolia API Key', required=True)
    algolia_index_name = fields.Char(string='Algolia Index Name', required=True)

    @api.model
    def create(self, vals):
        record = super(AlgoliaIntegration, self).create(vals)
        self._check_algolia_credentials(record.algolia_app_id, record.algolia_api_key)
        return record

    def write(self, vals):
        super(AlgoliaIntegration, self).write(vals)
        if 'algolia_app_id' in vals or 'algolia_api_key' in vals:
            self._check_algolia_credentials(self.algolia_app_id, self.algolia_api_key)
        return True

    def _check_algolia_credentials(self, app_id, api_key):
        """Check if the provided Algolia credentials are valid."""
        if not app_id or not api_key:
            raise UserError("Algolia Application ID and API Key must be set.")
        try:
            url = f'https://{app_id}-dsn.algolia.net/1/indexes/*/settings'
            headers = {
                'X-Algolia-API-Key': api_key,
                'X-Algolia-Application-Id': app_id
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                _logger.info("Successfully connected to Algolia with the provided credentials.")
            else:
                raise UserError("Failed to connect to Algolia with the provided credentials.")
        except Exception as e:
            _logger.error("Error checking Algolia credentials: %s", e)
            raise UserError("Error checking Algolia credentials. Please verify your Application ID and API Key.")

    @api.model
    def synchronize_with_algolia(self):
        """Synchronize Odoo products with Algolia index."""
        products = self.env['product.template'].search([])
        for product in products:
            self._update_algolia_index(product)

    def _update_algolia_index(self, product):
        """Update or create a single product in the Algolia index."""
        data = {
            'objectID': product.id,
            'name': product.name,
            'description': product.description_sale,
            'price': product.list_price,
            'categories': [c.name for c in product.categ_id],
            'image': product.image_1920,
        }
        url = f'https://{self.algolia_app_id}.algolia.net/1/indexes/{self.algolia_index_name}'
        headers = {
            'X-Algolia-API-Key': self.algolia_api_key,
            'X-Algolia-Application-Id': self.algolia_app_id,
            'Content-Type': 'application/json'
        }
        try:
            response = requests.put(f"{url}/{product.id}", json=data, headers=headers)
            if response.status_code == 200 or response.status_code == 201:
                _logger.info("Product %s successfully synchronized with Algolia.", product.name)
            else:
                _logger.error("Failed to synchronize product %s with Algolia. Status code: %s", product.name, response.status_code)
        except Exception as e:
            _logger.error("Error updating Algolia index for product %s: %s", product.name, e)
            raise UserError("Error updating Algolia index. Please check the logs for more details.")