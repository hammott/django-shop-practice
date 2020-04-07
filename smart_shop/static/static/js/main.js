$(document).ready(function () {
    $('#submit').click(function(event){
        var $email= $('#login-email').val();
        var $password= $('#login-password').val();
        var input = {
            email : $email,
            password : $password,
        }
        console.log(input);
        var jsonConvertedData = JSON.stringify(input);
        console.log(jsonConvertedData)
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/user/api/auth/login",
            data: "jsonConvertedData",
            dataType: "application/json",
            success: function (response) {
                console.log('process is compelete')
                
            }
        });
    })
});