id = "extension"

let reportsContainer = document.getElementsByClassName("reportsList")[0];
let timeline = document.getElementsByClassName("timeline")[0];


fetch("http://localhost:8080/analytics/" + id).then(raw => {
    raw.json().then(data => {
        for (date in data) {
            container = document.createElement('span');
            container.className = "report";

            detected = document.createElement('span')
            detected.className = "detected"
            container.appendChild(detected);

            detectedSubtitle = document.createElement('div');
            detectedSubtitle.className = "report-subtitle";
            detectedSubtitle.innerHTML = data[date]["state"].length + " Lists detected";
            detected.appendChild(detectedSubtitle);

            reportsContainer.appendChild(container);

            // console.log(container);
        }
    });
});