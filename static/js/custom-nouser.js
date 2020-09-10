   $('.modal').modal({
            dismissible: true, 
            complete: function() { 
              setCookie("popup", true, 240);
                
           
             } 
            }
        );

        if(checkCookie("popup") == false ){

                    $('#modal1').modal('open');
        }          