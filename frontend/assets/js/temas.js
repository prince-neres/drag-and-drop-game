const gerarDivs = () => {
  const temas = JSON.parse(localStorage.getItem('temas'))
  console.log(temas)
  for (tema of temas) {
    let divTema = `
        <div class='tema'>
          <h3>${tema.name}</h3>
          <p>${tema.description}</p>
          <button onclick='pegarTema(${tema.id})'>Jogar</button>
        </div>`
    $('.temas').append(divTema)
  }
}

gerarDivs()