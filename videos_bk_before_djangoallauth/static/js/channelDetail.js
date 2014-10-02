$(function () {
   stack = []; // stores the target we are interested in
   $('.video_div').scrollable({
           direction: 'vertical',
           in: function ( e, ui ) {
            var name = $(this).closest(".row").prev().find('a').text()
            var videoDD = $(this).data('videodiv')
            if($.inArray(videoDD, stack)==-1){
               stack.push(videoDD)
               console.log(stack)
            }
            console.log(videoDD+"in")
            if(stack[0]){
               jwplayer(stack[0]).play(true)
               stopAll(stack[0]);
            }

           },

           out: function ( e, ui ) {
            var name = $(this).closest(".row").prev().find('a').text()
            var videoDD = $(this).data('videodiv')
            console.log(videoDD+"out")
            if($.inArray(videoDD, stack)!=-1){
               var position=stack.indexOf(videoDD);
               if ( ~position ) stack.splice(position, 1);
               console.log(stack)
            }
            if(stack[0]){
               stopAll(stack[0]);
               jwplayer(stack[0]).play(true)
            }
           }

        });

});

function stopAll(exceptOne){
   $(".video_div").each(function(){
      if($(this).data('videodiv')!=exceptOne){
         jwplayer($(this).data('videodiv')).play(false)
      }
   });
}