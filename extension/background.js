chrome.runtime.onMessage.addListener((message, sender) => {
	console.log(message.className + ": " + message.visibility);
});

