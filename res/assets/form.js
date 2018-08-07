require(['jquery', 'assetman'], function ($, assetman) {
    $('.auth-ui-form').on('submit:form:pytsite', function () {
        let q = assetman.parseLocation().query;
        window.location.href = q.hasOwnProperty('__redirect') ? q.__redirect : window.location.origin;
    });
});
