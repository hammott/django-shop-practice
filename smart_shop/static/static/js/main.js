$(document).ready(function () {
    if (window.location.pathname == '/login/user'){
        if ($.cookie('user_token')){
            window.location.href = '/';
            console.log('inja dorost ast')
        }
    };
    console.log('with href' , window.location.href)
    console.log('without href' , window.location)

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
                window.location.href = '/';
                   
            }
        });
        
    })

    $('#nav_logout').click(function(){
        $.ajax({
            type: "POST",
            url: "/user/api/auth/logout",
            data: {},
            dataType: "json",
            success: function(response) {
                console.log(response);
                $.removeCookie('user_token');
                $.removeCookie('user_email');
                $.removeCookie('user_name');
                window.location.href = '/';

            }
        });
    });

    let get_cookie = () => {
        var $name = $.cookie('user_name');
        var $email = $.cookie('user_email');
        var $token = $.cookie('user_token');
        if ($token){
            $('#singin_name').html('Hello '+ $name);
            $('#email_header').html($email);
            console.log($name);
        }
        else {
            console.log('EXPIRED');
        }
        
      }

    get_cookie();

    let showDropAccount = () => {
        
        $('#nav-login').on('mouseenter',function(){
            $('.login_drop').slideDown();
            console.log('mouseenter')
        });
        $('#nav-login').on('mouseleave',function(){
            $('.login_drop').hide(200);
            console.log('mouseleave')
        });
    }
    
    let showDropSigin = () => {
        $('#nav-login').on('mouseenter',function(){
            $('.login-button').slideDown();
        });
        $('#nav-login').on('mouseleave',function(){
            $('.login-button').hide(200);
            console.log('Login')
        });
    }

    var $token = $.cookie('user_token');
    if ($token){
        showDropAccount()
    }else{
        showDropSigin()
    };


});