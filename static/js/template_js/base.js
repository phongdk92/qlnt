/**
 * Created by PyCharm.
 * User: vutran
 * Date: 8/4/11
 * Time: 6:05 AM
 * 
 */



$(document).ready(function(){
    // setting up css to render page in the right way

    $("footer").css('width',$(document).width());
//    if ($('#place_keeper').offset().top + $("footer").outerHeight() <= $(window).height()){
//        $("footer").css('position', 'fixed');
//        $("footer").css('bottom', '0');
//    }

    
    var maxHeight = 0;
    $(".thumb > ul").each(function(){
        if ($(this).height() > maxHeight){
            maxHeight = $(this).height();
        }
    });
    $(".thumb > ul").each(function(){
        $(this).css('height', maxHeight);
    });

    // end setting up
    // xss prevention


    $.fn.is_harmful = function(origin){
        if ($.encoder.encodeForHTML($.encoder.canonicalize(origin)) != origin ) return true;
        return $.encoder.encodeForJavascript($.encoder.canonicalize(origin)) != origin;

    };

    $("form").each(function(){
        $(this).submit(function(){
            var ok = true;
            console.log('submit');
            $('input:text').each(function(){
                var origin = $(this).val();
                if ($(this).is_harmful(origin)){
                    $("#notify").text("Thông tin bạn vừa nhập có chứa mã độc.");
                    $("#notify").fadeIn('fast');
                    $(this).focus();
                    $("#notify").delay(1000).fadeOut('fast');
                    ok = false;
                }
            });
            if (!ok) return false;

        });
    });


    $("input:text").each(function(){
        $(this).focusout(function(){
            var origin = $(this).val();
            if ($(this).is_harmful(origin)){
                $("#notify").text("Thông tin bạn vừa nhập có chứa mã độc.");
                $("#notify").fadeIn('fast');
                $(this).focus();
                $("#notify").delay(1000).fadeOut('fast');
            }
        });
    });
    // end xss prevention
    // jquery global function
    $.fn.disableNotification = function(){
        $(".notify-widget-pane").hide();
    };
    $.fn.enabelNotification = function(){
        $(".notify-widget-pane").show();
    };
    $.fn.showNotification = function(msg){
        $("#notify").enabelNotification();
        $("#notify").text(msg);
        $("#notify").fadeIn('fast');
        $("#notify").delay(1000).fadeOut('fast');
    };
    // end jquery global function

    // local functions.
    $.datepicker.setDefaults(
        $.extend(
            $.datepicker.regional['vi']
        )
    );

    $("input.datepicker").datepicker({
        changeMonth: true,
		changeYear: true,
        yearRange: 'c-60:c'
    });

    $("input:text").live('focus',function(){
        $(this).select();
        return false;
    });

    $("#notify").ajaxStart( function(){
        $(this).text("Đang lưu dữ liệu lên server...");
        $(this).fadeIn('fast');
    });

    $("#notify").ajaxSuccess( function(event, request, settings){
        $(this).text("Đã lưu.");
        $(this).delay(1000).fadeOut('fast');
    });

    $("#notify").ajaxError( function(event, request, settings){
        $(this).text("Gặp lỗi khi gửi dữ liệu tới server");
        $(this).delay(1000).fadeOut('fast');

    });


    $('*[class~="tiptipclick"]').tipTip({
        activation: "click",
        delay: 100
    });
    $('*[class~="tiptiphover"]').tipTip({
        activation: "hover",
        delay: 100
    });
    $('*[class~="tiptiphover_delay"]').tipTip({
        activation: "hover",
        delay: 1500
    });

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });

    $("#feedback").click(function(){
        $("#feedbackDiv").dialog('open');
    });

    var done = function(){
        $("#feedbackDiv").dialog('close');
        $("#feedback_content").val('');
    };


    $("#feedbackDiv").dialog({
        modal : true,
        buttons: {
            Gửi: function(){
                var data = $("#feedback_content").val();
                if ( data == ''){
                    $("#feedback_message").text("Bạn vui lòng điền nội dung để góp ý.");
                } else {
                    var feedback_url = window.location.href;
                    var arg = { type:"POST",
                        url:"/app/feedback/",
                        data:{content: data, feedback_url: feedback_url},
                        datatype:"json",
                        success: done
                    };
                    $.ajax(arg);

                }
            },
            Đóng: function(){ $(this).dialog('close');}
        },
        autoOpen: false,
        width: 440,
        height: 370,
        maxWidth: 500,
        maxHeight: 450,
        title: "Góp ý"
    });

});