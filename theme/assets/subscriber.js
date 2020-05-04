try {
   var autobahn = require('autobahn');
} catch (e) {
   // when running in browser, AutobahnJS will
   // be included without a module system
}

var connection = new autobahn.Connection({
   url: 'ws://127.0.0.1:8080/ws',
   realm: 'speedtest'}
);

connection.onopen = function (session) {

   function onresult(args) {
      console.log("Got event:", args[0]);
      document.getElementById('WAMPEvent').innerHTML = "Events:"+ args[0];
   }

   session.subscribe('results', onresult);
};


console.log("hello world");
connection.open();
