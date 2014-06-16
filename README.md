bda
===

planx junk


Steps:

    In meteor app server code
    // code to run on server at startup


if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
    Router.map(function () {
    this.route('serverRoute', {
      where: 'server',

      action: function () {
        var body = this.request.body;
        this.response.writeHead(200, {'Content-Type': 'text/html'});
        this.response.end('got: ' + JSON.stringify(body));      
      }
    });
    });
  });
}

Test the JSON echo route:

curl -H "Content-Type: application/json" -d '{"test": "this"}' codexcom01.cloudapp.net:3000/serverRoute

