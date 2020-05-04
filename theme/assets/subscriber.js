var connection = new autobahn.Connection({
   url: 'ws://127.0.0.1:8080/ws',
   realm: 'speedtest'}
);

connection.onopen = function (session) {

   function onResult(args) {
   	  // No idea why this doesn't work but I hate js and life is too short to spend
      // any more time on it.
      var element = this;
      anvil.call(element, "refresh_download_speed", args[0]['download']);
      document.getElementById('speed').innerHTML = args[0]['download'];
   }

   session.subscribe('results', onResult);
};

connection.open();
