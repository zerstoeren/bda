f (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
    Test = new Meteor.Collection("testobj");
    Router.map(function () {
      this.route('insert', {
        where: 'server',

        action: function () {
          console.log("in insert code");
          var body = this.request.body;
          this.response.writeHead(200, {'Content-Type': 'text/html'});
          this.response.end('got: ' + JSON.stringify(body));
          Test.insert(body);
        }
      });
      this.route('testDetail', {
        where: 'server',
        path: '/get/:mwid',
        action: function() {
          console.log("in get code");
          console.log("args: " + this.params.mwid);
          console.log("before read");
          var obj =  Test.findOne({test: this.params.mwid});
          console.log("read: " + obj);
          console.log("after read");
          console.log(JSON.stringify(obj));
        }
      });
    });
  });
}

