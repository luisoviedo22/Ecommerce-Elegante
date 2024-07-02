$(document).ready(function() {
    $('a[data-load-content]').click(function(event) {
      event.preventDefault();
      var url = $(this).attr('href');
      $.ajax({
        url: url,
        success: function(data) {
          $('#content-container').html(data);
        }
      });
    });
  });
  