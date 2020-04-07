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
            data: {
                email : $email,
                password : $password,
            },
            dataType: "json",
            success: function(response) {
                
                $.cookie('token',response.auth_token.token)
                $.cookie('email',response.email)
                $.cookie('name',response.name)

                $('#singin_name').html('Hello '+ $.cookie('name'))
                console.log(response.auth_token.token);
                console.log(response.name);
                console.log(response.email);

                
            }
        });
    })
});