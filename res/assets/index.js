import $ from 'jquery';
import assetman from '@pytsite/assetman';

$('.auth-ui-form.driver-password').on('submit:form:pytsite', function () {
    let q = assetman.parseLocation().query;
    window.location.href = q.hasOwnProperty('__redirect') ? q.__redirect : window.location.origin;
});
