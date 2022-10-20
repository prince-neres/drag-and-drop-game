const url_base = 'http://localhost:3000/'


function garda_tema(tema) {
  console.log(tema)
}


async function pegar_tema(theme_id) {  
  const response = await fetch(`http://localhost:3000/api/theme/${theme_id}`)
  let theme = await response.json()
  return theme
}

function criar_tema() {
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
}

function editar_tema() {
  let name = $('#name').val()
  let description = $('#description').val()
  let categories = $('#groups #category-input')

}

function remover_tema(id) {
  console.log(id)
}
