var http = require("http");
var url = require("url");
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/test');

var Schema = mongoose.Schema;

var netflowSchema = new Schema({
  smac:  String,
  dmac: String,
  sip: String,
  dip: String
});

function start(route) {
  var db = mongoose.connection;
  db.on('error', console.error.bind(console, 'connection error:'));
  db.once('open', function callback () {
    // yay!
  });


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
