$(document).ready(function(){
    // https://stackoverflow.com/questions/7643308/how-to-automatically-close-alerts-using-twitter-bootstrap
    $(".comment-alerts").alert();
    window.setTimeout(function() { $(".comment-alerts").alert('close'); }, 3000);
    $('.dropdown-toggle').dropdown();

    $('.edit-comment').each(function(){
    
        var comment_body = 'comment-body-' + $(this).attr('id');
        var comment_form = 'edit-comment-form-' + $(this).attr('id');
        var delete_comment_button = 'delete-comment-' + $(this).attr('id');
    
        $(this).click(function(){
            $('#'+comment_body).css('display','none');
            $('#'+comment_form).css('display','block');
            // Hide all other edit buttons ( you can only edit one at a time )
            $('.edit-comment').css('display','none');
            $('#'+delete_comment_button).css('display','none');
        });
    
    });

    $('.cancel-edit-comment').on('click',function(){

        $('.comment-body').css('display','block');
        $('.edit-comment-form').css('display','none');
        $('.edit-comment').css('display','block');
        $('.delete-comment').css('display','block');

    });
});

$(document).on('click',function(){
    $('.navbar-collapse').collapse('hide');
});

