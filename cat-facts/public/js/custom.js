$('input[type="checkbox"]').click(function() {
    if ($(this).prop("checked") == true) {
        $('#encoder-btn').removeClass("disabled");
        $('#encoder-btn').attr('onclick', 'location.href="/encode"');
    } else if ($(this).prop("checked") == false) {
        $('#encoder-btn').addClass("disabled");
        $('#encoder-btn').attr('onclick', '');
    }
});

$('#get-passwd').click(function() {
    if ($('input[type="checkbox"]').prop("checked") == true) {
        $('#passwd-disp').removeClass("d-none");
    } else if ($('input[type="checkbox"]').prop("checked") == false) {
        $('#passwd-disp').addClass("d-none");
    }
});

$('#encode-submit').click(() => {
    if ($('#passwd-error:contains("Password was incorrect")'.length > 0)) {
        console.log("hi");
        $('#passwd-error').removeClass('d-none');
    }   
});