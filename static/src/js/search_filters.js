odoo.define('algolia_ecommerce.search_filters', function (require) {
  "use strict";

  var ajax = require('web.ajax');
  var core = require('web.core');
  var Widget = require('web.Widget');
  var _t = core._t;

  var SearchFilters = Widget.extend({
    events: {
      'click .facet-filter-item': '_onFacetFilterClick',
      'click .remove-facet-filter': '_onRemoveFacetFilterClick'
    },

    init: function (parent, options) {
      this._super(parent);
      this.algoliaSearch = options.algoliaSearch;
    },

    start: function () {
      this._renderFacets();
      return this._super();
    },

    _renderFacets: function () {
      var self = this;
      var facetsHtml = '';
      var facets = this.algoliaSearch.getFacets();
      _.each(facets, function (facet) {
        facetsHtml += '<div class="facet-filter-item" data-facet="' + facet.name + '">' +
                      '<span class="facet-name">' + _t(facet.label) + '</span>' +
                      '<span class="facet-count">' + facet.count + '</span>' +
                      '</div>';
      });
      this.$el.html(facetsHtml);
    },

    _onFacetFilterClick: function (e) {
      var $target = $(e.currentTarget);
      var facetName = $target.data('facet');
      this.algoliaSearch.addFacetFilter(facetName);
      this._renderSelectedFacets();
    },

    _onRemoveFacetFilterClick: function (e) {
      var $target = $(e.currentTarget);
      var facetName = $target.data('facet');
      this.algoliaSearch.removeFacetFilter(facetName);
      this._renderSelectedFacets();
    },

    _renderSelectedFacets: function () {
      var self = this;
      var selectedFacetsHtml = '';
      var selectedFacets = this.algoliaSearch.getSelectedFacets();
      _.each(selectedFacets, function (facet) {
        selectedFacetsHtml += '<div class="selected-facet-filter-item" data-facet="' + facet.name + '">' +
                              '<span class="selected-facet-name">' + _t(facet.label) + '</span>' +
                              '<span class="remove-facet-filter">x</span>' +
                              '</div>';
      });
      this.$('.selected-facet-filters').html(selectedFacetsHtml);
    }
  });

  return SearchFilters;
});