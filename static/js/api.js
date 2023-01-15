const current_base = window.location.href
const url_base = 'http://localhost:5000/'


function criar_tema(event) {
  event.preventDefault()
  let name = $('#name').val()
  let description = $('#description').val()
  let categories = $('#groups #category-input')
  let tema = {}

  tema.name = name
  tema.description = description
  tema.categories = []

  $.each(categories, function(i, l) {
    category = {}
    items = $(l).children('#item-input')
    category_name = $(l).children('#category-name').val()
    category.name = category_name
    category.items = []

    $.each(items, function(i, l) {
      item_name = $(l).children('#item-name').val()
      item_obj = {'name': item_name}
      category['items'].push(item_obj)
    })

    tema.categories.push(category)
  })

  $.ajax({
    type: 'POST',
    url: `${url_base}create_theme`,
    data: JSON.stringify(tema),
    contentType:'application/json; charset=utf-8',
    dataType:'json',
    success: function (response) {
      var alert = ''
      
      if (response.success) {
        alert = `
          <div class="alert alert-success alert-dismissible fade show" role="alert">
            <strong>${response.success}</strong>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
          </div>
        `
      } else {
        alert = `
          <div class="alert alert-danger alert-dismissible fade show" role="alert">
            <strong>${response.error}</strong>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
          </div>
        `
      }
      $(alert).insertBefore('#formulario')
    }
  })
}


function editar_tema(_id) {
  event.preventDefault()
  let name = $('#name').val()
  let description = $('#description').val()
  let categories = $('#groups #category-input')
  let tema = {}

  tema.name = name
  tema.description = description
  tema.categories = []

  $.each(categories, function(i, l) {
    category = {}
    items = $(l).children('#item-input')
    category_name = $(l).children('#category-name').val()
    category.name = category_name
    category.items = []

    $.each(items, function(i, l) {
      item_name = $(l).children('#item-name').val()
      item_obj = { 'name': item_name }
      category['items'].push(item_obj)
    })

    tema.categories.push(category)
  })
  
  $.ajax({
    type: 'PUT',
    url: `${url_base}update_theme/${_id}`,
    data: JSON.stringify(tema),
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    success: function (response) {
      var alert = ''
      
      if (response.success) {
        alert = `
          <div class="alert alert-success alert-dismissible fade show" role="alert">
            <strong>${response.success}</strong>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
          </div>
        `
      } else {
        alert = `
          <div class="alert alert-danger alert-dismissible fade show" role="alert">
            <strong>${response.error}</strong>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
          </div>
        `
      }
      $(alert).insertBefore('#edicao')
    }
  })
}


function remover_tema(_id) {
  $.ajax({
    type: 'DELETE',
    url: `${url_base}delete_theme/${_id}`,
    success: function () {
      document.location.reload(true)
    }
  })
}


function salvar_pontuacao (_id, pontuacao, erros, tempo) {
  let req_obj = {}
  req_obj.theme_id = _id
  req_obj.score = pontuacao
  req_obj.mistakes = erros
  req_obj.time = tempo

  $.ajax({
    type: 'POST',
    url: `${url_base}save_score`,
    data: JSON.stringify(req_obj),
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    success: function () {
      console.log('Pontuação salva com sucesso!')
    }
  })
}
