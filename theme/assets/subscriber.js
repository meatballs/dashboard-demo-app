var form;

function set_form() {
	form = this;
}

var connection = new autobahn.Connection({
   url: 'ws://127.0.0.1:8080/ws',
   realm: 'dashboard'}
);

connection.onopen = function (session) {
   
   function onSpeedTestResult(args) {
   	  console.log(args[0]);
      anvil.call(form, 'raise_event', 'x-download-speed-updated', download=args[0]['download'], timestamp=args[0]['timestamp']);
   }

   session.subscribe('speedtest', onSpeedTestResult);
   
   function onCpuPercent(args) {
   	  anvil.call(form, 'raise_event', 'x-cpu-percent-updated', cpu_percent=args[0]);
   }
   
   session.subscribe('cpu_percent', onCpuPercent);
};

connection.open();