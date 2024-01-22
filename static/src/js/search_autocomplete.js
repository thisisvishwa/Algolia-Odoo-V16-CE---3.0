odoo.define('algolia_ecommerce.search_autocomplete', function (require) {
"use strict";

var publicWidget = require('web.public.widget');
var ajax = require('web.ajax');

publicWidget.registry.searchAutoComplete = publicWidget.Widget.extend({
    selector: '#search_input',
    events: {
        'input': '_onInput',
        'focusout': '_onFocusOut',
    },
    start: function () {
        this._super.apply(this, arguments);
        this.algoliaClient = algoliasearch('ALGOLIA_APPLICATION_ID', 'ALGOLIA_SEARCH_ONLY_API_KEY');
        this.algoliaIndex = this.algoliaClient.initIndex('odoo_ecommerce');
    },
    _onInput: function (ev) {
        var self = this;
        var query = $(ev.currentTarget).val();
        if (query.length > 0) {
            this.algoliaIndex.search(query, {
                hitsPerPage: 5,
                attributesToRetrieve: ['name', 'description', 'price', 'image'],
                attributesToHighlight: []
            }).then(function (responses) {
                self._renderSuggestions(responses.hits);
            });
        } else {
            this._clearSuggestions();
        }
    },
    _onFocusOut: function () {
        setTimeout(this._clearSuggestions.bind(this), 250);
    },
    _renderSuggestions: function (suggestions) {
        var $suggestionsContainer = $('#search_suggestions');
        $suggestionsContainer.html('');
        suggestions.forEach(function (hit) {
            var $suggestionItem = $('<div/>', {
                'class': 'suggestion-item',
                'html': '<img src="' + hit.image + '" alt="' + hit.name + '"/><span>' + hit._highlightResult.name.value + '</span>'
            });
            $suggestionsContainer.append($suggestionItem);
        });
    },
    _clearSuggestions: function () {
        $('#search_suggestions').html('');
    },
});

return {
    searchAutoComplete: publicWidget.registry.searchAutoComplete,
};

});
