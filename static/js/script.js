$(document).on('click',function(){
    $('.navbar-collapse').collapse('hide');
});

$('#edit-comment').on('click',function(){

    $('#comment-body').css('display','none');
    $('#edit-comment-form').css('display','block');
    $('#edit-comment').css('display','none');
    $('#delete-comment').css('display','none');

});

$('#cancel-edit-comment').on('click',function(){

    $('#comment-body').css('display','block');
    $('#edit-comment-form').css('display','none');
    $('#edit-comment').css('display','block');
    $('#delete-comment').css('display','block');

});

$(document).ready(function(){
    // https://stackoverflow.com/questions/7643308/how-to-automatically-close-alerts-using-twitter-bootstrap
    $(".comment-alerts").alert();
    window.setTimeout(function() { $(".comment-alerts").alert('close'); }, 3000);
    $('.dropdown-toggle').dropdown()
});
