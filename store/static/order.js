var element=''
console.log(orders)
for(let i=0;i<orders.length;i++)
{
    element+='<tr><td style="vertical-align:middle"><img src="../'+orders[i][6]+'" class="img-thumbnail" style="height:150px; width:100px"/></td>'
    //element+='<td>'+orders[i][3]+'</td>'
    element+='<td style="vertical-align:middle">'+orders[i][3]+'</td>'
    element+='<td style="vertical-align:middle">'+orders[i][4]+'</td>'
    element+='<td style="vertical-align:middle">'+orders[i][5]+'</td></tr>'
}



$(document).ready(function(){
    $('.order tbody').append(element)
})