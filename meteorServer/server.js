
if(Meteorr.isServer) {
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
        path: '/get/:start/:end',
        template: 'testDetail',
        action: function() {
          console.log("in get code");
          console.log("args: " + this.params.start + " " + this.params.end);
          console.log("before read");
          var obj = Test.find().fetch();
          //var obj = Test.find({time: {$gte: this.params.start, $lte: this.params.end}}).fetch();
          console.log("after read");
          console.log("read: " + obj);
          console.log(obj.length);
          var json = JSON.stringify(obj);
          this.response.setHeader('Content-Type', 'application/json');
          this.response.end(json);
        }
      });
    });
  });
}
