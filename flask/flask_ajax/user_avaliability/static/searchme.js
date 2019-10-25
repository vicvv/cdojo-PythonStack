$(document).ready(function(){
    console.log("in searchme.js file");
    $('#sme').keyup(function(){
        var data = $("#sform").serialize();  // capture all the data in the form in the variable data
        console.log(data);
        $.ajax({
            method: "GET",   // we are using a post request here, but this could also be done with a get
            url: "/usersearch",
            data: data
        })
        .done(function(res){
            console.log(res);
            $('#usearchMsg').html(res); // manipulate the dom when the response comes back
        });
    });
});