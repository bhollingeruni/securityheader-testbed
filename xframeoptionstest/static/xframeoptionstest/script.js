$(function(){

   $(".check-on-load").on("load", function() {
      save_result(test_id, $(this).attr("id") + "_client_check", check_content($(this)));
   });

   $('.check-manually').on('click', function () {
      save_result(test_id, $(this).attr("id") + "_client_check", $(this).find(':checked').val());
   });
});

function check_content(element){
   var result = 'content_not_loaded';

   if (element.contents().find('body').text() !== '')
   {
      result = 'content_loaded';
   }
   return result;
}
