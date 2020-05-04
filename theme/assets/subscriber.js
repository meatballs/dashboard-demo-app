var connection = new autobahn.Connection({
   url: 'ws://127.0.0.1:8080/ws',
   realm: 'speedtest'}
);

connection.onopen = function (session) {

   function onResult(args) {
      console.log("Got event:", args[0]);
      anvil.call(this, refresh_download_speed, args[0]['download']);
   }

   session.subscribe('results', onResult);
};

connection.open();
