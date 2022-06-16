document.addEventListener('DOMContentLoaded', () => {
	var dv = document.createElement('div');
	dv.id = "myId";
	dv.className = "hy";
	dv.innerHTML = "test";
	document.body.appendChild(dv);

	//await new Promise(r => setTimeout(r, 2000));

	chrome.runtime.sendMessage({className: "ad-boxes", visibility: getComputedStyle(dv, null).display});
});
