if (Meteor.isClient) {
  Template.hello.greeting = function () {
    return "Welcome to marktest.";
  };

  Template.hello.events({
    'click input': function () {
      // template data, if any, is available in 'this'
      if (typeof console !== 'undefined')
        console.log("You pressed the button");
    }
  });
}

if (Meteor.isServer) {
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
      this.route('insertall', {
        where: 'server',

        action: function () {
          console.log("in insert all code");
          var body = this.request.body;
          this.response.writeHead(200, {'Content-Type': 'text/html'});
          this.response.end('got all');
          for (var testData in body) {
            Test.insert(testData);
          }
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
          //var obj = Test.find().fetch();
          var sdate = new Date(this.params.start * 1000);
          var edate = new Date(this.params.end * 1000);
          console.log(sdate.toISOString());
          console.log(edate.toISOString());
          var obj = Test.find({time: {$gte: sdate.toISOString(), $lte: edate.toISOString()}}).fetch();
          console.log("after read");
          //console.log("read: " + obj);
          //console.log(obj.length);
          var json = JSON.stringify(obj);
          this.response.setHeader('Content-Type', 'application/json');
          this.response.end(json);
        }
      });
      this.route('testDetail', {
        where: 'server',
        path: '/getall',
        template: 'testDetail',
        action: function() {
          console.log("in get all code");
          console.log("before read");
          var obj = Test.find().fetch();
          console.log("after read");
          //console.log("read: " + obj);
          //console.log(obj.length);
          var json = JSON.stringify(obj);
          this.response.setHeader('Content-Type', 'application/json');
          this.response.end(json);
        }
      });
      this.route('testDetail', {
        where: 'server',
        path: '/delete',
        template: 'testDetail',
        action: function() {
          console.log("in delete code");
          Test.remove({});
        }
      });
    });
  });
}

