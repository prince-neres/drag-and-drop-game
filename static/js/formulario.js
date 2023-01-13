function add_categoria() {
  var category_input = `
    <div id="category-input">
      <button type="button" id="remove-category" onclick="remove_categoria(this)" class="btn btn-danger">
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


function remove_categoria(category) {
  $(category).parent().remove()
}


function addItem(item) {
  var item_input = `
    <div id="item-input">
      <input id="item-name" class="form-control" placeholder="Item da Categoria" required/>
      <button type="button" id="remove-item" onclick="remove_item(this)" class="btn btn-danger">
        <i class="bi bi-trash-fill"></i>
      </button>
    <div>
  `
  $(item).parent().append(item_input)
}


function remove_item(item) {
  $(item).parent().remove()
}
