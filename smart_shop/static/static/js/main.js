$(document).ready(function () {

    // $(window.location.href == '/login/user').ready(function(){
    //     if ($.cookie('user_token')){
    //         window.location = '/';
    //     }
    // })
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
            url: "/user/api/auth/login",
            data: {
                email : $email,
                password : $password,
            },
            dataType: "json",
            success: function(response) {
                $.cookie('user_token',response.auth_token.token,{ path: '/', expires: 7 });
                $.cookie('user_email',response.email,{ path: '/', expires: 7 });
                $.cookie('user_name',response.name,{ path: '/', expires: 7 });
                console.log(response.auth_token.token);
                console.log(response.name);
                console.log(response.email);
                window.location = '/';
                   
            }
        });
        
    })
    function get_cookie() {
        var $name = $.cookie('user_name');
        var $token = $.cookie('user_token');
        if ($token){
            $('#singin_name').html('Hello '+ $name);
            console.log($name);
        }
        else {
            console.log('EXPIRED');
        }
        
      }

    get_cookie();

});