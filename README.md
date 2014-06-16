bda
===

planx junk


Steps:

    In meteor app: 
    // code to run on server at startup
    Router.map(function () {
    this.route('serverRoute', {
      where: 'server',

      action: function () {
        this.response.writeHead(200, {'Content-Type': 'text/html'});
        this.response.end('hello from server');
      }
    });
    });

