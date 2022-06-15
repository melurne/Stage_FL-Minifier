chrome.runtime.onInstalled.addListener(()=> {
	chrome.storage.sync.set({ color });
	console.log('Default background color set to %cgreen', `color: ${color}`);
});

chrome.tabs.onActivated.addListener((tab) => {
  	chrome.scripting.executeScript({
    		target: { tabId: tab.tabId },
    		files: ["content-script.js"]
 	});
});

chrome.runtime.onMessage.addListener((message, sender) => {
	console.log(message.className + ": " + message.visibility);
});
