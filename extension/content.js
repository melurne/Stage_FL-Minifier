let extensionid;
chrome.storage.sync.get(['extensionid'], (res) => {
    extensionid = res.extensionid;
});

document.addEventListener('DOMContentLoaded', () => {
    let capsule = document.createElement('div');
    document.body.appendChild(capsule);
    setTimeout(() => {
        fetch("http://localhost:8080/tests").then((res) => {
            res.json().then(res => {
                results = [];
                for (test of res.tests) {
                    var dv = document.createElement('div');
                    dv.innerHTML = test;
                    var elem = dv.firstChild;
                    capsule.appendChild(elem);
                    setTimeout(results.push(getComputedStyle(elem, null).display == "none"), 10);
                }
                console.log(results);
            });
        });
    }, 10);

    // When we change the custom rules in uBO, the first time we run a test always return all falses
    
    setTimeout(() => {
        fetch("http://localhost:8080/tests").then((res) => {
            res.json().then(elems => {
                imgs = elems.tests.map(t => {
                    var dv = document.createElement('div');
                    dv.innerHTML = t;
                    return dv.firstChild;
                });
                results = [];
                for (elem of imgs) {
                    capsule.appendChild(elem);
                    setTimeout(results.push(getComputedStyle(elem, null).display == "none"), 10);   
                }
                console.log(results); 
                fetch("http://localhost:8080/result", {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({id:extensionid, results: results})
                }).then(() => {
                    document.body.removeChild(capsule);
                    console.log("Data Logged");
                });
            });
        });
    }, 100);
});