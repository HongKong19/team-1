
document.onload(function(event){
    event.preventDefault();
    $.ajax({
        url: 'http://localhost:3001/suggestions',
        method: 'post',
        data: {username: ""},
        crossDomain: true
      })
      .then(function(success){
        var result = JSON.parse(success);
        var update="";
        for(var i=0; i<result['food'].length();i++){
            update+="<li>"+result['food'][i]+"</li">
        }
        $("#food").innerhtml(update);
        });
});

