var count = 1

$('.drag').draggable(
    {
        revert : function (event, ui) {
            let passou = true
            count > 5 ? passou = false : passou = true
            count++
            return passou
        }
    }
)

$('.drop').droppable(
    {
        drop: function(event, ui){

        }
    }
)