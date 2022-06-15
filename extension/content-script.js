function sleep(time) {
	return new Promise((r) => setTimeout(r, time));
}
/*
var dv = document.createElement('div');
dv.id = 'myid';
dv.className = 'ad-boxes'
dv.innerHTML = 'test';
*/
chrome.runtime.onMessage.addListener((req, sender, sendResponse) => {
	var dv = document.createElement('div');
	dv.id = 'myid';
	dv.className = req.className
	dv.innerHTML = 'test';

	document.body.appendChild(dv);
	const style = getComputedStyle(dv, null);
	sendResponse({display: style.display});
	document.body.removeChild(dv);
});


/*
chrome.runtime.sendMessage({
	className: "ad-boxes",
	visibility: style.display
})*/
