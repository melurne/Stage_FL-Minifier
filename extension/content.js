document.addEventListener('DOMContentLoaded', () => {
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
    }, 10);
});