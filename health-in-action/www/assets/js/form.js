$("#userdet").submit(function(event){
    event.preventDefault();
    $.ajax({
        url: 'http://localhost:3001/signup',
        method: 'post',
        data: {username: $("#name").val(), password:"",weight: $("#weight").val(), height: $("#height").val(), bp: $("#blood_pressure").val(),sugar:$("#bloodsugar").val(),smoke:$("#smoking").val(),alcohol:$("#alcoholic").val(),foodpref:$("#preference").val()},
        crossDomain: true
      })
      .then(function(success){
        if (success === ""){
            alert("Success");
            window.open ('results.html','_self',false);
            console.log("worked");
        }
        });
});

