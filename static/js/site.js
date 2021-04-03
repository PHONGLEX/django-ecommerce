(function (site, $) {
    site.basket = function () {
        this.settings = {};

        this.init = (options) => {
            this.settings = $.extend(this.settings, options);
            this.loadData();
        }

        

        return this;
    }
}(window.site = window.site || {}, jQuery));