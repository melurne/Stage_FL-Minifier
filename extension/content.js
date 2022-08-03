document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        fetch("http://localhost:8080/tests").then((res) => {
            res.json().then(res => {
                results = [];
                for (test of res[0].tests) {
                    var dv = document.createElement('div');
                    dv.innerHTML = test;
                    var elem = dv.firstChild;
                    document.body.appendChild(elem);
                    results.push(getComputedStyle(elem, null).display == "none");
                    document.body.removeChild(elem);
                }
            });
        });
    }, 10);

    // When we change the custom rules in uBO, the first time we run a test always return all falses
    
    setTimeout(() => {
        fetch("http://localhost:8080/tests").then((res) => {
            res.json().then(elems => {
                imgs = elems[0].tests.map(t => {
                    var dv = document.createElement('div');
                    dv.innerHTML = t;
                    return dv.firstChild;
                });
                results = [];
                for (elem of imgs) {
                    document.body.appendChild(elem);
                    results.push(getComputedStyle(elem, null).display == "none");
                    document.body.removeChild(elem);
                }
                console.log(results); 
                fetch("http://localhost:8080/result", {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({id:"extension", results: results})
                }).then(() => {
                    console.log("Data Logged");
                });
            });
        });
    }, 100);
});