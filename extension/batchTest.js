document.addEventListener('DOMContentLoaded', () => {
	fetch("http://localhost:8080/lists").then(res => {
		res.json().then(res => {
			for (list of lists) {

                let randomId = Math.random().toString(36).slice(2);
				var dv = document.createElement('div');
				dv.innerHTML = "<div id=" + randomId + " listname=" + list +" combination=""></div";
				var elem = dv.firstChild;
			}
		});
	});
});