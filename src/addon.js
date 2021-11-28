// function needed that is not included from chrome extension
var cssRules = `
.cbghelper_nowrap { 
    white-space: nowrap; 
}
`

function injectCSS() {
    var style = document.createElement('style');
    style.innerHTML = cssRules;
    document.getElementsByTagName('head')[0].appendChild(style);
}

injectCSS();