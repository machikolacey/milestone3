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