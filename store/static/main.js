
var categories_tag=''
for(let i=0;i<categories.length;i++)
{
  categories_tag+='<div class="category">'+categories[i][0]+'</div>'
}


$(document).ready(function(){
  $('.categories').append(categories_tag)
})



var item=''
for(let i=0;i<items.length;i++)
{

    item += '<div style="border-bottom: 1px solid #dedfee; height: 35%; margin-bottom: 1%;" class="bookname"> <div style="height: 100%;" class="col-lg-2"><img src="../'+items[i][5]+'" class="img-thumbnail" /></div>'
    item += '<div class="col-lg-8"> <h4>'+items[i][1].toUpperCase()+'</h4><p class="genere">'+items[i][2]+'</p><p>'+items[i][4].slice(0, 500)+'...</p></div>'
    item += '<div style="height: 100%; text-align: center;" class="col-lg-2"> <h3 class="'+items[i][1].split(" ").join("")+'">₹'+items[i][3]+'</h3><div class="authenticate"><button class="btn btn-primary" type="button" name="'+items[i][1]+'">Add</button></div></div></div>'

}


$(document).ready(function(){
    $('.book_list').append(item)
    $('.authenticate').hide();
    $('.genere').hide();
})


var total_amount = 0;
var object = []

$(document).ready(function(){
  $('.authenticate button').click(function(){
    var classname = $(this).attr('name').split(" ").join("")
    var bookname = $(this).attr('name')
    var item = $('.'+classname)    
    quantity = 1;
    amount = parseInt($("."+classname).get(0).innerHTML.slice(1))
    if(isNaN(quantity) || quantity<1){
      alert('Enter valid quantity');
    }
    else{
      total_amount += amount;
      var tags = '';
      tags+='<tr><td style="text-align:left;">'+bookname+'</td><td style="text-align:right;">'+amount+'</td></tr>'
      $('#orders').append(tags);
      $('#submit').html('Amount : ₹ '+total_amount) 
      let arr = {bookname, quantity, amount}    
      object.push(arr);
      console.log(object);
    }
    
  })
})

$(document).ready(function(){
  $('#remove').click(function(){
    var remove_amount = object[object.length-1].amount;
    total_amount-=remove_amount;
    object.pop()
    var rows = $('#orders').children()
    rows[rows.length-1].remove()
    $('#submit').html('Amount : ₹ '+total_amount) 
  })
})


$(document).ready( function() {
    $('#submit').click(function() {
      const jsonString = JSON.stringify(Object.assign({}, object))
      $.ajax({
        type: 'POST',
        contentType: 'application/json',
        data: jsonString,
        dataType: 'json',
        url: 'http://127.0.0.1:5000/home',
        success: function (e) {
            alert("Order placed successfully")
            location.reload();
            
        },
        error: function(error) {
          alert("Order placed successfully")
          location.reload();
        }
    });
    });
  });

$(document).ready(function(){
  $('.search-option input').on("keyup", function(){
    var value = $('.search-option input').val().toLowerCase()
    $('.bookname').filter(function(){
      $(this).toggle($(this).text().toLowerCase().indexOf(value)>-1)
    })
  })
})


$(document).ready(function(){
  $('.category').on("click", function(){
    var value = $(this).text().toLowerCase()
    $('.bookname').filter(function(){
      $(this).toggle($(this).text().toLowerCase().indexOf(value)>-1)
    })
  })
})

