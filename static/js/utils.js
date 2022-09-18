function addCategory() {
  var category_input = `
    <div id="category-input">
      <button type="button" id="remove-category" onclick="removeCategory(this)" class="btn btn-danger">
        Remover Categoria
      </button>
      <input id="category-name" class="form-control" placeholder="Categoria" required/>
      <button  type="button" id="add-item" onclick="addItem(this)" class="btn btn-success">
        Adicionar Item
      </button>
    <div>
  `

  $(category_input).insertBefore('#add-category')
}


function removeCategory(category) {
  $(category).parent().remove()
}


function addItem(item) {
  var item_input = `
    <div id="item-input">
      <input id="item-name" class="form-control" placeholder="Item da Categoria" required/>
      <button type="button" id="remove-item" onclick="removeItem(this)" class="btn btn-danger">
        Remover Item
      </button>
    <div>
  `

  $(item).parent().append(item_input)
}


function removeItem(item) {
  $(item).parent().remove()
}


(function () {
  'use strict'
  var forms = document.querySelectorAll('.needs-validation')

  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
})()