id = "extension"

let reportsContainer = document.getElementsByClassName("reportsList")[0];
let timeline = document.getElementsByClassName("timeline")[0].getElementsByTagName('svg')[0];
const VIEWBOX_HEIGHT = 20;
const VIEWBOX_WIDTH = 1400;
const LINE_COLOR = "#47BDFF";
const FADED_LINE_COLOR = "#C7C7C7";
let selected;
let sorted;

function generateReports(data, reportsContainer) {
    for (date in data) {
        container = document.createElement('span');
        container.className = "report";
        reportsContainer.appendChild(container);

        reportTitle = document.createElement("div");
        reportTitle.innerHTML = date;
        reportTitle.style.position = "relative";
        container.appendChild(reportTitle);

        detected = document.createElement('span');
        detected.className = "detected";
        container.appendChild(detected);

        detectedSubtitle = document.createElement('div');
        detectedSubtitle.className = "report-subtitle";
        detectedSubtitle.innerHTML = data[date]["state"].length + " Lists detected";
        detected.appendChild(detectedSubtitle);

        detectedList = document.createElement('ul');
        detected.appendChild(detectedList);

        for (list of data[date]["state"]) {
            let tmp = document.createElement('li');
            tmp.className = "filter-list";
            tmp.innerHTML = "<div>" + list + "</div>";
            detectedList.appendChild(tmp);
        }


        added = document.createElement('span');
        added.className = "added";
        container.appendChild(added);

        addedSubtitle = document.createElement('div');
        addedSubtitle.className = "report-subtitle";
        addedSubtitle.innerHTML = data[date]["diffs"]["+"].length + " Lists added";
        added.appendChild(addedSubtitle);

        for (list of data[date]["diffs"]["+"]) {
            let tmp = document.createElement('li');
            tmp.className = "filter-list";
            tmp.innerHTML = "<div>" + list + "</div>";
            added.appendChild(tmp);
        }


        removed = document.createElement('span');
        removed.className = "removed";
        container.appendChild(removed);

        removedSubtitle = document.createElement('div');
        removedSubtitle.className = "report-subtitle";
        removedSubtitle.innerHTML = data[date]["diffs"]["-"].length + " Lists removed";
        removed.appendChild(removedSubtitle);

        for (list of data[date]["diffs"]["-"]) {
            let tmp = document.createElement('li');
            tmp.className = "filter-list";
            tmp.innerHTML = "<div>" + list + "</div>";
            removed.appendChild(tmp);
        }


        container.style.height = Math.max(...[parseInt(getComputedStyle(detected, null).height), parseInt(getComputedStyle(added, null).height), parseInt(getComputedStyle(removed, null).height)]) + "px";

        // console.log(container);
    }
}

function extractDate(fullDate) {
    return fullDate.split(' ')[0];
}

function generateTimeline(sortedData, svg) {
    let today = new Date()
    let coloredRatio = ((today.getMonth()+1)*30 + today.getDate())/365;
    let innerhtml =     
    "<line x1='0' y1='10' x2='" + coloredRatio*VIEWBOX_WIDTH + "' y2='10' stroke='" + LINE_COLOR + "' stroke-width='2'/>\n\
    <line x1='" + coloredRatio*VIEWBOX_WIDTH+1 + "' y1='10' x2='" + VIEWBOX_WIDTH + "' y2='10' stroke='" + FADED_LINE_COLOR + "' stroke-width='2'/>\n";

    for (date in sortedData) {
        year = date.split('-')[0]
        month = date.split('-')[1]
        day = date.split('-')[2];
        if ((new Date(date)).getTime() === (new Date(selected)).getTime()) {
            r = 6;
        }
        else {
            r = 4;
        }
        innerhtml = innerhtml + "<circle cx='" + (parseInt(month)*30+parseInt(day))*VIEWBOX_WIDTH/365 + "' cy='10' r='" + r + "' fill='" + LINE_COLOR + "'/>\n";
    }

    svg.innerHTML = innerhtml;
}

fetch("http://localhost:8080/analytics/" + id).then(raw => {
    raw.json().then(data => {
        sorted = {};
        for (date in data) {
            if (!(Object.keys(sorted).includes(extractDate(date)))) {
                sorted[extractDate(date)] = {};
            }
            sorted[extractDate(date)][date] = data[date];
            selected = extractDate(date);
        }
        regenerate(sorted);
    });
});

function regenerate(sorted) {
    reportsContainer.innerHTML = "";
    generateTimeline(sorted, timeline);
    generateReports(sorted[selected], reportsContainer);
    if (Object.keys(sorted).indexOf(selected) === 0) {
        document.getElementById('rightarrow').style.background = "#AAAAEE";
        document.getElementById('leftarrow').style.background = "#AAAAAA";
    }
    else if (Object.keys(sorted).indexOf(selected) === Object.keys(sorted).length -1) {
        document.getElementById('rightarrow').style.background = "#AAAAAA";
        document.getElementById('leftarrow').style.background = "#AAAAEE";
    }
    else {
        document.getElementById('rightarrow').style.background = "#AAAAEE";
        document.getElementById('leftarrow').style.background = "#AAAAEE";
    }
}

document.getElementById('year').addEventListener('change', () => {
    console.log(document.getElementById('year').value);
});

document.getElementById('rightarrow').addEventListener('click',() => {
    if (!(Object.keys(sorted).indexOf(selected) === Object.keys(sorted).length -1)) {
        selected = Object.keys(sorted)[Object.keys(sorted).indexOf(selected) + 1];
        regenerate(sorted)
    }
});

document.getElementById('leftarrow').addEventListener('click',() => {
    if (!(Object.keys(sorted).indexOf(selected) === 0)) {
        selected = Object.keys(sorted)[Object.keys(sorted).indexOf(selected) - 1];
        regenerate(sorted)
    }
});

