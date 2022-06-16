/*var dv = document.createElement('div');
dv.id = 'myid';
dv.className = 'ad-boxes'
dv.innerHTML = 'test';

chrome.tabs.onCreated.addListener((tab) => {
  	chrome.scripting.executeScript({
    		target: { tabId: tab.tabId },
    		files: ["content-script.js"]
 	});
});
*/
chrome.runtime.onMessage.addListener((message, sender) => {
	console.log(message.className + ": " + message.visibility);
});
/*
setInterval(() => {
	chrome.tabs.query({active: true}, (res) => {
		for (const tab of res) {
			chrome.scripting.executeScript({
    				target: { tabId: tab.id },
    				files: ["content-script.js"]
 			});
			console.log(tab.title);
			chrome.tabs.sendMessage(tab.id, {className: 'ad-boxes'}, (response) => {
				console.log('ad-boxes: ' + response.display);
			});
		}
	});

}, 2000);*/
