id = "extension"

function updateLists() {
    listsSpan = document.getElementById("lists");
    // alert(listsSpan);
    fetch("http://localhost:8080/current/extension").then(res => {
        res.json().then((lists) => {
            for (l of lists) {
                
                let dv = document.createElement('div');
                dv.innerHTML = "<br>" + l + "</br>";
                listsSpan.appendChild(dv);
            }
        });
    });
}

// let but = document.getElementById("updateButton");
// but.addEventListener("click", updateLists());

updateLists()