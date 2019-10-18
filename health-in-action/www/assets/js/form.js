$("#userdet").submit(function(event){
    event.preventDefault();
    $.ajax({
        url: 'http://localhost:3001/userDetails',
        method: 'post',
        data: {name: $("name").val(), email: $("email").val(), weight: $("weight").val(), height: $("height").val(), blood_pressure: $("blood_pressure").val()},
        crossDomain: true
      })
      .then(function(success){
        if (success === ""){
            alert("Success");
        }
        });
});

