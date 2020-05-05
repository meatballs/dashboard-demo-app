var form;

function set_form() {
	form = this;
}

var connection = new autobahn.Connection({
   url: 'ws://127.0.0.1:8080/ws',
   realm: 'speedtest'}
);

connection.onopen = function (session) {
   
   function onResult(args) {
      anvil.call(form, 'refresh_download_speed', args[0]);
   }

   session.subscribe('results', onResult);
};

connection.open();