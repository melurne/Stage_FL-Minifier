function sleep(time) {
	return new Promise((r) => setTimeout(r, time));
}

var dv = document.createElement('div');
dv.id = 'myid';
dv.className = 'ad-boxes'
dv.innerHTML = 'test';
document.body.appendChild(dv);

const style = getComputedStyle(dv, null);

chrome.runtime.sendMessage({
	className: "ad-boxes",
	visibility: style.display
})
document.body.removeChild(dv);
