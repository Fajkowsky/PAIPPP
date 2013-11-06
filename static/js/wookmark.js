(function ($){
  var options = {
      // Prepare layout options.
      autoResize: true, // This will auto-update the layout when the browser window is resized.
      container: $('#main'), // Optional, used for some extra CSS styling
      offset: 15, // Optional, the distance between grid items
      outerOffset: 10, // Optional, the distance to the containers border
      itemWidth: 210 // Optional, the width of a grid item
  }

  function onScroll(event) {
    var winHeight = window.innerHeight ? window.innerHeight : $(window).height();
    var closeToBottom = ($(window).scrollTop() + winHeight > $(document).height() - 100);

    if (closeToBottom) {
      var items = $('#tiles li'),
          firstTen = items.slice(0, 10);
      $('#tiles').append(firstTen.clone());
      applyLayout();
    }
  };

  function applyLayout() {
    $('#tiles').imagesLoaded(function() {
      if (handler.wookmarkInstance) {
        handler.wookmarkInstance.clear();
      }

      handler = $('#tiles li');
      handler.wookmark(options);
    });
  }
  
  $(window).bind('scroll', onScroll);

  var handler = $('#tiles li');
  handler.wookmark();
})(jQuery);