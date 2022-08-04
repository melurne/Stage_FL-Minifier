id = "extension"
fetch("http://localhost:8080/statistics/" + id).then(raw => {
    raw.json().then(data => {
        
    });
});