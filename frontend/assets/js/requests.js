const listarTemas = () => {
  $.ajax({
    type: 'GET',
    url: 'http://localhost:3000/temas',
    success: function (temas) {
      localStorage.setItem("temas", JSON.stringify(temas))
    }
  })
}

const pegarTema = async (id) => {
  $.ajax({
    type: 'GET',
    url: `http://localhost:3000/tema/${id}`,
    success: function (tema) {
      console.log(tema)
      localStorage.setItem("tema", JSON.stringify(tema));
      document.location.href = "./jogo.html"
    }
  })
}

listarTemas()