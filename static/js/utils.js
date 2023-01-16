const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))


const count_items = (categories) => {
  let number_of_items = 0
  
  categories.forEach((arr) => {
    arr.items.map((i) => {
      number_of_items++
    })
  })
  return number_of_items
}
