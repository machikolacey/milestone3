$("#formValidate").validate({
  rules: {
    description: {
        required: true,
        minlength: 2
    },
    photo: {
        required: true,
        minlength: 2
    },
    mobile_num: {
        required: true,
        minlength: 10,
        maxlength: 10
    },
    email: {
        required: true,
        email:true
    },
    pass: {
        required: true,
        minlength: 5
    },
    confirm_pass: {
        required: true,
        minlength: 5,
        equalTo: "#pass"
    }
},
//For custom messages
messages: {
    description: {
        required: "Please enter your first name.",
        minlength: "You sure you're named with one letter?"
    },
    photo: {
        required: "Please enter your last name.",
        minlength: "You sure you're named with one letter?"
    },
    email: {
        required: "Please enter your email address.",
        email: "Please enter a valid email address."
    },
    pass: {
        required: "Please enter a password.",
        minlength: "Password must be atleast 5 characters."
    },
    confirm_pass: {
        required: "Please confirm your password.",
        minlength: "Password must be atleast 5 characters.",
        equalTo: "Password does not match."
    }
}
});