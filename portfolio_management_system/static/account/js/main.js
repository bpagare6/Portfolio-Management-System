function bindPasswordReveal() {
    $('input[type="password"] + .input-group-append').each(function() {
        $(this).on('mousedown touchstart', function() {
            $(this)
                .prev()
                .attr('type', 'text');
        });
        $(this).on('mouseup touchend', function() {
            $(this)
                .prev()
                .attr('type', 'password');
        });
    });
}

function showErrorAlert() {
    $('.alert-form-error:not(.d-block)')
        .removeClass('d-none')
        .addClass('d-block');
}

function hideErrorAlert() {
    $('.alert-form-error')
        .removeClass('d-block')
        .addClass('d-none');
}

function bindInputFocusListener() {
    $('form .form-control')
        .bind('focus', function() {
            $(this)
                .closest('.form-group')
                .addClass('focused');
        })
        .bind('blur', function() {
            $(this)
                .closest('.form-group')
                .removeClass('focused');
        });
}

function bindInputErrorHandler() {
    $('form .form-control')
        .bind('invalid', function(e) {
            showErrorAlert();
            $(this)
                .closest('.form-group')
                .addClass('has-error');
        })
        .bind('change', function(e) {
            if ($(this).is(':valid')) {
                $(this)
                    .closest('.form-group')
                    .addClass('is-valid');
            }

            if ($(this).is(':invalid')) {
                showErrorAlert();
                $(this)
                    .closest('.form-group')
                    .addClass('has-error');
            }
        })
        .bind('keyup', function() {
            $(this)
                .closest('.form-group')
                .removeClass('has-error');
        });
}

window.addEventListener('load', function() {
    bindPasswordReveal();
    bindInputFocusListener();
    bindInputErrorHandler();
});
