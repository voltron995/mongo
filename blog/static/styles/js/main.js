window.addEventListener('load', function() {

	function addClass(o, c){
	    var re = new RegExp("(^|\\s)" + c + "(\\s|$)", "g");
	    if (re.test(o.className)) return;
	    o.className = (o.className + " " + c).replace(/\s+/g, " ").replace(/(^ | $)/g, "");
	}
 
	function removeClass(o, c){
	    var re = new RegExp("(^|\\s)" + c + "(\\s|$)", "g");
	    o.className = o.className.replace(re, "$1").replace(/\s+/g, " ").replace(/(^ | $)/g, "");
	}


	var $send    = document.querySelector('.js-usersend'),
		$sex     = document.querySelectorAll('.js-usersex'),
		$name    = document.querySelector('.js-username'),
		$email   = document.querySelector('.js-useremail'),
		$subject = document.querySelector('.js-usersubject'),
		$message = document.querySelector('.js-usermessage');
		// $modal   = document.querySelector('#myModal');
 
	function correctSex(collection) {
		if(!collection.length) {
			return;
		}

		for(var i = 0; i < collection.length; ++i) {
			if(collection[i].checked) {
				return collection[i].value;
			}
		}

		return false;
	}

	function validateEmail(email) { 
	    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	    return re.test(email);
	}

	$name.addEventListener('keydown', function(e){
		
		if (e.keyCode >= 47 && e.keyCode <=57) {
			e.preventDefault();
		}
		
	}, true);


	

	$email.addEventListener('keydown', function(e){
		var emailText = $email.value;
		
		if (validateEmail(emailText)) {
			removeClass($email, 'invalid');
		}
		else {
			addClass($email, 'invalid');
		}

	},true);

	$send.addEventListener('click', function() {


		if(!correctSex($sex)) {
			alert('Choose sex');
			return;
		}

		if($name.value === '' || /[\d+]/.test($name.value)) {
			alert('Wrong name');
			return;
		}

		if(!validateEmail($email.value)) {
			alert('Wrong email');
			return;
		}

		if($subject.value === '') {
			alert('Wrong subject');
			return;
		}

		if($message.value === '') {
			alert('Wrong message');
			return;
		}

		else {
			alert('Your message was sent');
			return;
		}
	});

});