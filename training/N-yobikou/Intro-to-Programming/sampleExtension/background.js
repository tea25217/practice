chrome.browserAction.onClicked.addListener(function(tab) {
  chrome.tabs.executeScript(null, {file: "jquery-3.4.1.min.js"});     //$ is not defined対応
  chrome.tabs.executeScript(null, {file: "script.js"});
});