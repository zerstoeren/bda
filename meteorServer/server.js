if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
    Router.map(function () {
      this.route('insert', {
        where: 'server',

        action: function () {
          Test = new Meteor.Collection("test");
          var body = this.request.body;
          this.response.writeHead(200, {'Content-Type': 'text/html'});
          this.response.end('got: ' + JSON.stringify(body));
          Test.insert(body);
        }
      });
      this.route('testDetail', {
        path: '/get/:_id',
        where: 'server',
        action: function() {
          Test = new Meteor.Collection("test");
          return Test.findOne({test: this.params._id});
        }
      });
    });
  });
