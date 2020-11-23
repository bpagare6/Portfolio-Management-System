/**
 * For demo purposes only.
 * Remove this file from production builds.
 */

function bindPasswordResetForm() {
    $('form.reset-password-form').on('submit', function(e) {
        e.preventDefault();
        $('.reset-form')
            .removeClass('d-block')
            .addClass('d-none');
        $('.reset-confirmation').addClass('d-block');
    });
}

window.addEventListener('load', function() {
    bindPasswordResetForm();
});
