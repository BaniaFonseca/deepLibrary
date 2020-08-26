// const getpage = new Promise((resolve, reject) => {
//     $.ajax({
//       url: 'pdfloader',
//       data: {
//         'edocpage'  : document.getElementById('page_num'),
//         'edocid': 123,
//         'edoctype'  : 'book' 
//       },
//       dataType: 'json',
//       success: function (data) 
//       {
//         pdfData = atob(data.pdfbase64data);
//         resolve(pdfData);
//       },
//       error: function(result) {
//         reject(null);
//     }
//   });

//     // if(condition) {    
//     //     resolve(temp);  
//     // } else {    
//     //     reject('Promise is rejected');  
//     // }
// });

// getpage.then((data) => {  
//   alert(data);
// });

// getpage.then(function(value) {
//   alert(value);
// }, function(reason) {
//   alert(reason);
// });

// function getpage(n)
// {
//   var pdfData
//   $.ajax
//   ({
//     url: 'pdfloader',
//     data: {
//       'edocpage'  : n,
//       'edocid': 123,
//       'edoctype'  : 'book' 
//     },
//     dataType: 'json',
//     success: function (data) 
//     {
//       pdfData = atob(data.pdfbase64data)
//     }
//   });
  
//     return pdfData;
// }

function temp(n)
{
  $.ajax({
    url: 'pdfloader',
    data: {
      'edocpage'  : n,
      'edocid': 123,
      'edoctype'  : 'book' 
    },
    dataType: 'json',
    success: function (data) 
    {
      var pdfData = atob(data.pdfbase64data)
      // If absolute URL from the remote server is provided, configure the CORS
  // header on that server.
  // var url = 'https://raw.githubusercontent.com/mozilla/pdf.js/ba2edeae/web/compressed.tracemonkey-pldi-09.pdf';
  // var url = '/static/demo.pdf'
  // Loaded via <script> tag, create shortcut to access PDF.js exports.
  var pdfjsLib = window['pdfjs-dist/build/pdf'];
  
  // The workerSrc property shall be specified.
  
  pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://mozilla.github.io/pdf.js/build/pdf.worker.js';
  
  var pdfDoc = null,
      pageNum = n;
      pageRendering = false;
      pageNumPending = null;
      scale = 1.5;
      canvas = document.getElementById('the-canvas');
      ctx = canvas.getContext('2d');
      
      
  /**
   * Get page info from document, resize canvas accordingly, and render page.
   * @param num Page number.
   */
  function renderPage(num) {
    pageRendering = true;
    // Using promise to fetch the page
    pdfDoc.getPage(num).then(function(page) {
      var viewport = page.getViewport({scale: scale});
      canvas.height = viewport.height;
      canvas.width = viewport.width;
  
      // Render PDF page into canvas context
      var renderContext = {
        canvasContext: ctx,
        viewport: viewport
      };
      
      var renderTask = page.render(renderContext);
  
      // Wait for rendering to finish
      renderTask.promise.then(function() {
        pageRendering = false;
        if (pageNumPending !== null) {
          // New page rendering is pending
          renderPage(pageNumPending);
          pageNumPending = null;
        }
      });
    });
  
    // Update page counters
    document.getElementById('page_num').textContent = num;
  }
  
  /**
   * If another page rendering in progress, waits until the rendering is
   * finised. Otherwise, executes rendering immediately.
   */
  function queueRenderPage(num) {
    if (pageRendering) {
      pageNumPending = num;
    } else {
      renderPage(num);
    }
  }
  
  // renderPage(num);
  /**
   * Displays previous page.
   */
  function onPrevPage() {
    if (pageNum <= 1) {
      return;
    }
    pageNum--;
    queueRenderPage(pageNum);
  }
  // document.getElementById('prev').addEventListener('click', onPrevPage);
  
  /**
   * Displays next page.
   */
  function onNextPage() {
    if (pageNum >= pdfDoc.numPages) {
      return;
    }
    pageNum++;
    queueRenderPage(pageNum);
  }
  // document.getElementById('next').addEventListener('click', onNextPage);
  
  /**
   * Asynchronously downloads PDF.
   */
  
  // pdfjsLib.getDocument({data: pdfData}).promise.then(function(pdfDoc_) {
  
  // var url = 'https://raw.githubusercontent.com/mozilla/pdf.js/ba2edeae/examples/learning/helloworld.pdf';
  var url = 'http://localhost:9000/edocuments/cl.pdf'; 
  // {data: pdfData}
  pdfjsLib.getDocument(url).promise.then(function(pdfDoc_) {
    pdfDoc = pdfDoc_;
    document.getElementById('page_count').textContent = pdfDoc.numPages;
    // Initial/first page rendering
    renderPage(1);
    // renderPage(pageNum);
  });
  
  }});
}

pageNum = 600
// temp(pageNum);

window.onscroll = function(ev) 
{
    if ((window.innerHeight + window.scrollY) >= document.body.scrollHeight) 
    {
        // if (pageNum >= pdfDoc.numPages) 
        // {
        //     return;
        // }
        pageNum++;
        // temp(pageNum);
        //queueRenderPage(pageNum);
    }
    
    if ((window.scrollY) < 1) 
    {
        // if (pageNum <= 1) 
        // {
        // return;
        // }
        pageNum--;
        // temp(pageNum);
        // queueRenderPage(pageNum);
    }
};

function temp2(n)
{
      // If absolute URL from the remote server is provided, configure the CORS
  // header on that server.
  // var url = 'https://raw.githubusercontent.com/mozilla/pdf.js/ba2edeae/web/compressed.tracemonkey-pldi-09.pdf';
  // var url = '/static/demo.pdf'
  // Loaded via <script> tag, create shortcut to access PDF.js exports.
  var pdfjsLib = window['pdfjs-dist/build/pdf'];
  
  // The workerSrc property shall be specified.
  
  pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://mozilla.github.io/pdf.js/build/pdf.worker.js';
  
  var pdfDoc = null,
      pageNum = n;
      pageRendering = false;
      pageNumPending = null;
      scale = 1.5;
      canvas = document.getElementById('the-canvas');
      ctx = canvas.getContext('2d');
      
      
  /**
   * Get page info from document, resize canvas accordingly, and render page.
   * @param num Page number.
   */
  function renderPage(num) {
    pageRendering = true;
    // Using promise to fetch the page
    pdfDoc.getPage(num).then(function(page) {
      var viewport = page.getViewport({scale: scale});
      canvas.height = viewport.height;
      canvas.width = viewport.width;
      
      // canvas.height = window.innerHeight
      // canvas.width = window.innerWidth
  
      // Render PDF page into canvas context
      var renderContext = {
        canvasContext: ctx,
        viewport: viewport
      };
      
      var renderTask = page.render(renderContext);
  
      // Wait for rendering to finish
      renderTask.promise.then(function() {
        pageRendering = false;
        if (pageNumPending !== null) {
          // New page rendering is pending
          renderPage(pageNumPending);
          pageNumPending = null;
        }
      });
    });
  
    // Update page counters
    document.getElementById('page_num').textContent = n;
  }
  
  /**
   * If another page rendering in progress, waits until the rendering is
   * finised. Otherwise, executes rendering immediately.
   */
  function queueRenderPage(num) {
    if (pageRendering) {
      pageNumPending = num;
    } else {
      renderPage(num);
    }
  }
  
  // renderPage(num);
  /**
   * Displays previous page.
   */
  function onPrevPage() {
    if (pageNum <= 1) {
      return;
    }
    pageNum--;
    queueRenderPage(pageNum);
  }
  // document.getElementById('prev').addEventListener('click', onPrevPage);
  
  /**
   * Displays next page.
   */
  function onNextPage() {
    if (pageNum >= pdfDoc.numPages) {
      return;
    }
    pageNum++;
    queueRenderPage(pageNum);
  }
  // document.getElementById('next').addEventListener('click', onNextPage);
  
  /**
   * Asynchronously downloads PDF.
   */
  
  // pdfjsLib.getDocument({data: pdfData}).promise.then(function(pdfDoc_) {
  
  // var url = 'https://raw.githubusercontent.com/mozilla/pdf.js/ba2edeae/examples/learning/helloworld.pdf';
  // var url = 'http://localhost:9000/edocuments/cl.pdf'; 

  var url = '/lwviewer/'+$("#type").data('value')+'/'+$("#id").data('value')+'/'+'/'+n 
  
  // {data: pdfData}
  pdfjsLib.getDocument(url).promise.then(function(pdfDoc_) {
    pdfDoc = pdfDoc_;
    // document.getElementById('page_count').textContent = pdfDoc.numPages;
    // Initial/first page rendering
    renderPage(1);
    // renderPage(pageNum);
  });
}


temp2(15)