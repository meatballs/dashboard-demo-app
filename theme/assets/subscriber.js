var connection = new autobahn.Connection({
   url: 'ws://127.0.0.1:8080/ws',
   realm: 'speedtest'}
);

connection.onopen = function (session) {
   var form = this;

   function onResult(args) {
      console.log(this)
      anvil.call(form, 'refresh_download_speed', args[0]['download']);
      document.getElementById('speed').innerHTML = args[0]['download'];
   }

   session.subscribe('results', onResult);
};

connection.open();
