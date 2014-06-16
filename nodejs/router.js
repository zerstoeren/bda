var queryString = require("querystring");

function route(url, request) {
  console.log("About to route a request for " + url.pathname);
  switch(url.pathname) {
    case '/':
      console.log("root route");
      break;
    case '/netflow':
      console.log("netflow route");
      if (request.method == 'POST') {
        var body = '';
        request.on('data', function (data) {
          body += data;

            // lol Too much POST data, kill the connection!
            //if (body.length > 1e6)
            //    req.connection.destroy();
        });
        request.on('end', function () {
          var resultObject = JSON.parse(body);
          console.log("got post");
          console.log(resultObject);
	})
      }
      break;
    default:
      console.log("default route");
  }
}

exports.route = route;
