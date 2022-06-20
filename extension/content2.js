document.addEventListener('DOMContentLoaded', () => {
	fetch("http://localhost:8080/rules").then((res) => {
		res.json().then(res => {
			res.classNames.map((className) => {
				var dv = document.createElement('div');
				dv.innerHTML = "<div id=" + className + /*" src='http://www.example.com/?ad=true'*/">test</div>";
				var elem = dv.firstChild;
				document.body.appendChild(elem);	
				setTimeout(() => {
					chrome.runtime.sendMessage({
									className: className, 
									visibility: getComputedStyle(elem, null).display
					}, () => {
						//document.body.removeChild(elem);
						return 0;
					});
				}, 10000);
			});
		});
	});
});
