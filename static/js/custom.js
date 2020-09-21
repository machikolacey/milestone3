   $(document).ready(function() {
        
  
           $(".button-collapse").sideNav({edge:"right"});
            //  $('.side-nav').sidenav();
               $('select').material_select();



        $('.searchcafe').keyup(function(event) {
        return $.getJSON(
            '/cafe_autocomplete/'+$('.searchcafe').attr('sortvalue'), 
             function (data) {
                console.log(data) ; 
                return process(data);
             });
        });  



        });
 function autoCompleteCafe (cafenames){
    let data = {};
    cafenames.forEach(function (cafename) {
        console.log(cafename.cafe_name)
       data[cafename.cafe_name] = "https://res.cloudinary.com/machikolacey/image/upload/v1597350037/milestone3/Julien-Plumart-Cafe_oztqap.jpg";
    });

    $('input.autocomplete').autocomplete({
      data: data
    });
}

        $('.datepicker').pickadate({
            selectMonths: true,
            selectYears: 10, 
            max: new Date(),
            selectMonths: true, 
            close: 'Ok',
            today: 'Today',
            clear: 'Clear',
            format: 'dd/mm/yyyy'
        });

        $('.datepicker').on('mousedown',function(event){
            event.preventDefault();
        });

        $('.sort').click(function(event) {
        return $.getJSON(
            '/sort_memories/'+$(this).val(), 
             function (data) {
                return process(data);
             });
        });  


function setCookie(cname, cvalue, exdays) {
  var d = new Date();
  d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
  var expires = "expires="+d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
  var name = cname + "=";
  var ca = document.cookie.split(';');
  for(var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
 function checkCookie(cname) {
  var val=getCookie(cname);
  if (val != "") {
   return true;
  } else {
   return false;
  }
}

