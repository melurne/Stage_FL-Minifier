let id;
chrome.storage.sync.get(['extensionid'], (res) => {
    id = res.extensionid;
    document.getElementById("yourid").innerHTML = id;
    updateLists();
});

function updateLists() {
    listsSpan = document.getElementById("lists");
    // alert(listsSpan);
    fetch("http://localhost:8080/current/" + id).then(res => {
        res.json().then((lists) => {
            for (l of lists) {
                
                let dv = document.createElement('div');
                dv.innerHTML = "<br>" + l + "</br>";
                listsSpan.appendChild(dv);
            }
        });
    });
}

// Go to history page
let but = document.getElementById("history");
but.addEventListener("click", () => {
    chrome.tabs.create({url: "AnalyticsWindow/analytics.html"});
}); 

// Change extensionID
let commit = document.getElementById("commitid");
commit.addEventListener("click", () => {
    let newId = document.getElementById("extensionid").value;
    chrome.storage.sync.set({extensionid: newId}, ()=>{});
});

