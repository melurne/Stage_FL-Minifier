let color = '#3aa757'

chrome.runtime.onInstalled.addListener(()=> {
	chrome.storage.sync.set({ color });
	console.log('Default background color set to %cgreen', `color: ${color}`);
});

chrome.tabs.onActivated.addListener((tab) => {
  console.log("trying");
  chrome.scripting.executeScript({
    target: { tabId: tab.tabId },
    files: ["content-script.js"]
  });
});
