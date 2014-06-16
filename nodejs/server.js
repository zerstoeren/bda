var http = require("http");
var url = require("url");

function start(route) {
  function onRequest(request, response) {
    var parsedURL = url.parse(request.url);
    console.log("Request for " + parsedURL.pathname + " received.");

    route(parsedURL, request);

    response.writeHead(200, {"Content-Type": "text/plain"});
    response.write("Processed route...");
    response.end();
  }

  http.createServer(onRequest).listen(8888);
  console.log("Server has started.");
}

exports.start = start;
