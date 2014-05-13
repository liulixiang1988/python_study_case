$(document).ready ->
  $('#likes').click ->
    catid = $(this).attr('data-catid')
    $.get('/rango/like_category', {category_id: catid}, (data)->
      $('#like_count').html(data)
      $('#likes').hide()
    )