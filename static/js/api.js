const current_base = window.location.href
const url_base = 'http://127.0.0.1:3000/'

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
      item_obj = { "name": item_name }
      category['items'].push(item_obj)
    })

    tema.categories.push(category)
  })

  $.ajax({
    type: "POST",
    url: `${url_base}create_theme`,
    data: JSON.stringify(tema),
    contentType:"application/json; charset=utf-8",
    dataType:"json",
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

function editar_tema() {
  let name = $('#name').val()
  let description = $('#description').val()
  let categories = $('#groups #category-input')

}

function remover_tema(_id) {
  $.ajax({
    type: "DELETE",
    url: `${url_base}delete_theme/${_id}`,
    success: function () {
      console.log('Tema deletado com sucesso!')
      document.location.reload(true)
    }
  })
}
