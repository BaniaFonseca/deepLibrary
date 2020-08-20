pdfDoc = null
canvas = document.getElementById('cnv');
ctx = canvas.getContext('2d');
scale = 1.5;
numPage = 1;


var pdfjsLib = window['pdfjs-dist/build/pdf'];
var loadingTask = pdfjsLib.getDocument('./demo.pdf');
loadingTask.promise.then(function(pdf) {
    alert('ola')
});
