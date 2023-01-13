var url = window.location.href
var tema_id = url.split('/').pop()
var erros = 0
var pontuacao = 0
var tempo = 30
var tempo_restante = 0
var tempo_preparar = 0
var thread_tempo
var categorias = JSON.parse(localStorage.getItem('categories'))
var items_count = 0


/* Começa contagem regressiva de 3 segundos para o início do jogo */
$('[id="start-game"]').click(function () {
  $('#start').removeClass('hide')
  $('.item').animate({top: '0px',left: '0px'})
  pontuacao = 0
  $('#points').text(pontuacao)
  erros = 0
  $('#errors').text(erros)
  $('#end').addClass('hide')
  $('#reset').addClass('hide')
  $('#board-game').addClass('hide')
  tempo_preparar = 3
  $('#start').html('<b><p>Prepare-se...</p><h1>' + tempo_preparar + '</h1></b>')
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


/* Verifica se a contagem regressiva terminou para começar o jogo */
const preparacao = () => {
  tempo_preparar--

  if (tempo_preparar == 0) {
      $('#start').html('<b><p style="font-size:30px">Valendo...</p></b>')
  } else {
      $('#start').html('<b><p>Prepare-se...</p><h1>' + tempo_preparar + '</h1></b>')
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
  items_count = conta_itens_tema()
}


/* Verifica se elemento foi arrastado para categoria correta */
function itemDrop(event, ui) {
  var slotCategoria = $(this)
  var cardItem = ui.draggable

  if(slotCategoria.attr('name') === cardItem.attr('categoria')){
    ui.draggable.draggable('option', 'revert', false)
    pontuacao++
    $('#points').text(pontuacao)

    pontuacao >= items_count ? fim_jogo() : null
  } else {
    erros++
    $('#errors').text(erros)
  }
}


/* Inicia contador do jogo */
const iniciar_contador = () => {
    tempo_restante = tempo
    $('#time').text(tempo_restante)
    thread_tempo = setInterval(function () {
        verificar_contador()
    }, 1000)
}


/* Verifica se contador não chegou ao fim */
const verificar_contador = () => {
    tempo_restante--
    $('#time').text(tempo_restante)

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


const conta_itens_tema = () => {
  let count = 0

  for (let categoria of categorias) {
    for(let item in categoria['items']) {
      count++
    }
  }
  return count
}


/* Acaba sessão do jogo limpando variáveis e removendo componentes */
const fim_jogo = () => {
  $('#end').removeClass('hide')
  $('#reset').addClass('hide')
  $('#board-game').addClass('hide')
  salvar_pontuacao(tema_id, pontuacao, erros, tempo_restante)
  terminar_contador()
}
