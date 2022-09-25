function addCategory() {
  var category_input = `
    <div id="category-input">
      <button type="button" id="remove-category" onclick="removeCategory(this)" class="btn btn-danger">
        <i class="bi bi-trash-fill"></i>
      </button>
      <input id="category-name" class="form-control" placeholder="Categoria" required/>
      <button  type="button" id="add-item" onclick="addItem(this)" class="btn btn-primary">
        <i class="bi bi-plus-square"></i>
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
        <i class="bi bi-trash-fill"></i>
      </button>
    <div>
  `

  $(item).parent().append(item_input)
}


function removeItem(item) {
  $(item).parent().remove()
}
