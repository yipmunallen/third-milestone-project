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


window.addEventListener("pageshow", () => {
  // update hidden input field
});