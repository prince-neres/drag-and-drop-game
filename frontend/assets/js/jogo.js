const tema = JSON.parse(localStorage.getItem('tema'))
const { atividade } = tema
const { categorias } = tema
const { items } = tema
var erros = 0
var pontuacao = 0

$('.name').text(atividade.name)
$('.description').text(atividade.description)
$('#errors').text(erros)
$('#points').text(pontuacao)

const criaComponentes = () => {

  for (item of items) {
    let divItem = `
        <div class='item' id='${item.id}'>
          <h3>${item.name}</h3>
        </div>`
    $('.items').append(divItem)
  }

  for (categoria of categorias) {
    let divCategoria = `
        <div class='categoria' id='${categoria.id}'>
          <h3>${categoria.name}</h3>
          <p>${categoria.description}</p>
        </div>`
    $('.categorias').append(divCategoria)
  }


  $('.item').draggable()
  $('.categoria').droppable()
}

criaComponentes()