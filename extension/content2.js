document.addEventListener('DOMContentLoaded', () => {
	fetch("http://localhost:8080/rules").then((res) => {
		res.json().then(res => {
			res.classNames.map((className) => {
				var dv = document.createElement('div');
				dv.id = "myId";
				dv.className = className;
				dv.innerHTML = "test";
				document.body.appendChild(dv);

				chrome.runtime.sendMessage({className: className, visibility: getComputedStyle(dv, null).display});
			});
		});
	});
});
