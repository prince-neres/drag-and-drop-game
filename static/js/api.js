const url_base = 'http://localhost:3000'

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

  console.log(tema)

  $.ajax({
    type: "POST",
    url: `${url_base}/create_theme`,
    data: JSON.stringify(tema),
    contentType:"application/json; charset=utf-8",
    dataType:"json",
    success: function () {
      console.log('Tema criado com sucesso!')
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
    url: `${url_base}/delete_theme/${_id}`,
    success: function () {
      console.log('Tema deletado com sucesso!')
    }
  })
}
