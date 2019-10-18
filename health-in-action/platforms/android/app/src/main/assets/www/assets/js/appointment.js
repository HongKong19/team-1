$("#lol").submit(function(event){
    event.preventDefault();
    $.ajax({
        url: 'http://localhost:3001/appointment',
        method: 'post',
        data: {username: ""},
        crossDomain: true
      })
      .then(function(success){
        if (success === ""){
            alert("Success");
            window.open ('index.html','_self',false);
            console.log("worked");
        }
        });
});

