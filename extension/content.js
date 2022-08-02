document.addEventListener('DOMContentLoaded', () => {
    let el = document.createElement('div')
    document.body.appendChild(el);
    console.log(getComputedStyle(el, null).display)
    setTimeout(() => {
        fetch("http://localhost:8080/tests").then((res) => {
            res.json().then(res => {
                console.log(res[0].tests)
                results = [];
                for (test of res[0].tests) {
                    var dv = document.createElement('div');
                    dv.innerHTML = test;
                    var elem = dv.firstChild;
                    document.body.appendChild(elem);
                    console.log(getComputedStyle(elem, null).display)
                    results.push(getComputedStyle(elem, null).display == "none");
                }
                console.log(results); 
                // fetch("http://localhost:8080/result", {
                //     method: 'POST',
                //     headers: {
                //         'Accept': 'application/json',
                //         'Content-Type': 'application/json'
                //     },
                //     body: JSON.stringify({id:"extension", results: results})
                // }).then(() => {
                //     console.log("Data posted");
                // });
            });
        });
    }, 1000);

    // When we change the custom rules in uBO, the first time we run a test always return all falses
    
    setTimeout(() => {
        fetch("http://localhost:8080/tests").then((res) => {
            res.json().then(res => {
                console.log(res[0].tests)
                results = [];
                for (test of res[0].tests) {
                    var dv = document.createElement('div');
                    dv.innerHTML = test;
                    var elem = dv.firstChild;
                    document.body.appendChild(elem);
                    console.log(getComputedStyle(elem, null).display)
                    results.push(getComputedStyle(elem, null).display == "none");
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
                    console.log("Data posted");
                });
            });
        });
    }, 2000);
});