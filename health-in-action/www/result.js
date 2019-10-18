
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
            update+="<li>"+result['food'][i]+"</li>";
        }
        $("#food").innerhtml(update);
        update="";
        for(var i=0; i<result['exercise'].length();i++){
            update+="<li>"+result['exercise'][i]+"</li>";
        }
        $("#exercise").innerhtml(update);
        update="";
        for(var i=0; i<result['goals'].length();i++){
            update+='<li>'+result['goals'][i]+'</br><div class="progress"><div class="progress-bar" role="progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div></div></li>';
        }
        $("#goals").innerhtml(update);
        });
});

