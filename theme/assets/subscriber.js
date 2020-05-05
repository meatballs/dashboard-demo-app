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
      anvil.call(form, 'raise_event', 'x-download-speed-updated', args[0]);
   }

   session.subscribe('speedtest', onSpeedTestResult);
   
   function onCpuPercent(args) {
   	  anvil.call(form, 'raise_event', 'x-cpu-percent-updated', args[0]);
   }
   
   session.subscribe('cpu_percent', onCpuPercent);
};

connection.open();