function copyToClipboard(element) {
    var myVar = document.getElementById(element);
    myVar.select();
    document.execCommand("copy");
}