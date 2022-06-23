const testFunc = require("./includeTest.js");

document.addEventListener('DOMContentLoaded', () => {
	fetch("http://localhost:8080/rules").then((res) => {
		res.json().then(res => {
			res.classNames.map((className) => {
				/*fetch("http://localhost:8080/scripts/" + className).then((res) => {
						res.text().then(res => {
							console.log(res);
						});
				});*/
				testFunc("Include Works");
				var dv = document.createElement('div');
				dv.innerHTML = "<script id='tester'>\
					console.log(\"testing\");\
					</script>";
				var elem = dv.firstChild;
				document.body.appendChild(elem);	
				setTimeout(() => {
					chrome.runtime.sendMessage({
									className: className, 
									visibility: getComputedStyle(elem, null).display
					}, () => {
						document.body.removeChild(elem);
						//return 0;
					});
				}, 100000);
			});
		});
	});
});
