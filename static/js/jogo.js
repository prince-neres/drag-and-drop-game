import { count_items } from './utils.js'
var erros = 0
var pontuacao = 0
var tempo = 30
var tempo_preparar = 0
var tempo_restante = 0
var thread_tempo
var categorias = JSON.parse(localStorage.getItem('categories'))
var number_of_items = count_items(categorias)


/* Começa contagem regressiva de 3 segundos para o início do jogo */
$('button[id^="start-game"]').on('click', function () {
  reset_game_vars()
  $('#board-game').addClass('hide')
  $('#end').addClass('hide')
  $('#reset').addClass('hide')
  $('#start').removeClass('hide')
  $(".item").animate({top: "0px",left: "0px"})

  tempo_preparar = 3
  $("#start").html('<p>Prepare-se...</p><h1>' + tempo_preparar + '</h1>')

  thread_tempo = setInterval(function () {
      preparacao()
  }, 1000)

  $('.item').draggable(
    {
      containment: '#board',
      stack: '.items div',
      cursor: 'move',
      revert: true
    }
  )

  $('.categoria').droppable(
    {
      accept: '.item',
      hoverClass: 'hovered',
      drop: itemDrop
    }
  )
})


/* Reseta variaveis do jogo */
const reset_game_vars = () =>{
  pontuacao = 0
  erros = 0
  tempo = 30
  $('#points').text(pontuacao) &&  $('#errors').text(erros)
}


/* Verifica se a contagem regressiva terminou para começar o jogo */
const preparacao = () => {
  tempo_preparar--

  if (tempo_preparar == 0) {
      $("#start").html('<p style="font-size:30px">Valendo...</p>')
  } else {
      $("#start").html('<p>Prepare-se...</p><h1>' + tempo_preparar + '</h1>')
  }

  if (tempo_preparar < 0) {
      clearInterval(thread_tempo)
      tempo_preparar = 3
      comecar_jogo()
      return
  }
}


/* Começa o jogo adicionando componentes do mesmo e removendo não necessários */
const comecar_jogo = () => {
  $('.box').addClass('hide')
  $('#board-game').removeClass('hide')
  $('#reset').removeClass('hide')
  iniciar_contador()
}


/* Verifica se elemento foi arrastado para categoria correta */
function itemDrop(event, ui) {
  let slot_categoria = $(this)
  let card_item = ui.draggable
  let categoria = slot_categoria.attr('categoria')
  let item = card_item.attr('item')
  let categoria_obj = categorias.filter(c => c.name === categoria)
  let contains_item = categoria_obj[0].items.filter(i => i.name === item)

  if(contains_item.length === 1){
    ui.draggable.draggable('option', 'revert', false)
    pontuacao++
    pontuacao >= number_of_items ? fim_jogo() : $('#points').text(pontuacao)
  } else {
    erros++
    $('#errors').text(erros)
  }
}


/* Inicia contador do jogo */
const iniciar_contador = () => {
    tempo_restante = tempo
    $("#time").text(tempo_restante)
    thread_tempo = setInterval(function () {
        verificar_contador()
    }, 1000)
}


/* Verifica se contador não chegou ao fim */
const verificar_contador = () => {
    tempo_restante--
    $("#time").text(tempo_restante)

    if (tempo_restante <= 0) {
        terminar_contador()
        fim_jogo()
    }
}


/* Termina contador */
const terminar_contador = () => {
    clearInterval(thread_tempo)
    tempo_restante = tempo
}


/* Acaba sessão do jogo limpando variáveis e removendo componentes */
const fim_jogo = () => {
  $('#end').removeClass('hide')
  $('#reset').addClass('hide')
  $('#board-game').addClass('hide')
  terminar_contador()
  pontuacao = 0
  erros = 0
}
