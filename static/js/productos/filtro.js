$(document).ready(function() {
    // Evento de clic en el botón de filtros
    $('#toggleFilterButton').click(function() {
      $('#filterBox').toggle();
      var buttonText = $(this).find('span').text().trim();
      var buttonImage = $(this).find('img');
      var productContainer = $('.product-container');
  
      if (buttonText === 'Ocultar filtros') {
        $(this).find('span').text('Mostrar filtros');
        buttonImage.addClass('rotate-180');
        productContainer.addClass('col-md-12').removeClass('col-md-9');
      } else {
        $(this).find('span').text('Ocultar filtros');
        buttonImage.removeClass('rotate-180');
        productContainer.removeClass('col-md-12').addClass('col-md-9');
      }
    });
});