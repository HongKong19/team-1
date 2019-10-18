
document.onload(function(event){
    event.preventDefault();
    $.ajax({
        url: 'http://localhost:3001/schedule',
        method: 'get',
        crossDomain: true
      })
      .then(function(success){
        var result = JSON.parse(success);
        var update="";
        for(var i=0; i<result.length();i++){
            update+='<li><h3>'+result[i]+'<h3><a href="#" class="button fit">Accept</a></li>';
        }
        $("#dashboard").innerhtml(update);
        });
});

