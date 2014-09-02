$(document).ready(function(){
	var month = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"];
	$( ".pointerDiv" ).hover(
	  function() {
	    $( this ).css( "opacity",1);
	  },function() {
	    $( this ).css( "opacity",0.1);
	  }
	);
	$(".previousTrigger").click(function(){
		var href = $(this).data('previousurl')
		console.log(href)
		window.location.href = href;
	})
	$(".nextTrigger").click(function(){
		var href = $(this).data('nexturl')
		console.log(href)
		window.location.href = href;
	})
	$( "#posts" ).on( "click", ".chatlist", function(e) {
		$(this).next().find('.comment').slideToggle( "fast" );
	});

	$("#sendPost").click(function() {
        // Send Post URL
		var postURL = $(this).val()
		console.log(postURL)
		//Post textarea is not empty 
		if ($('#postTextarea').val().trim()){
			var input_string = $("#postTextarea").val()
			var csrf = $("input[name='csrfmiddlewaretoken']").val()
			var videoid = $('#videoID').val()
			console.log("clicked")
			$.ajax({
				url : postURL,
				type : "POST",
				data : {
				text : input_string,
				videoID : videoid,
				csrfmiddlewaretoken: csrf
				},
				success : function(mess) {
					console.log(mess)
					postReload()
				}
				});
		}
	});

    // Prepend comments for posts 
    $( "#posts" ).on( "keydown", "textarea", function(event) {
        if ( event.which == 13 && $(this).val!="" ) {
           event.preventDefault();
	    // Send Post URL
		var postURL = $("#sendPost").val()
		//Post textarea is not empty 
		if ($(this).val()){
			var input_string = $(this).val()
			var csrf = $("input[name='csrfmiddlewaretoken']").val()
			var videoid = $('#videoID').val()
			$.ajax({
				url : postURL,
				type : "POST",
				data : {
				text : input_string,
				videoID : videoid,
				parentID : $(this).closest(".comment").parent().prev().data('postid'),
				csrfmiddlewaretoken: csrf
				},
				success : function(json) {
					postReload()
				}
				});
		}
           //clear the input
           $(this).val('')
        }
    });
    function clear () {
        $('#postTextarea').html('')
        $("#inputAttachments").html('')
    };
    function postReload(){
	// Current Page URL for reload posts
	var currentpage = document.URL
	$("#posts").load(currentpage+" #posts2",function(){
		console.log('posts upload success')
		// clear input textarea
		$('#postTextarea').val('')
	}); 
	}

	
});