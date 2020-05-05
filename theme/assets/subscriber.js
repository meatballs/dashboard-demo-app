var form;
var router_url;

function set_form() {
	form = this;
};

function set_router_url(url) {
    router_url = url;
};

var connection = new autobahn.Connection({
   url: router_url,
   realm: 'dashboard'}
);

connection.onopen = function (session) {
   
   function onSpeedTestResult(args) {
      anvil.call(form, 'raise_download_speed_event', args[0]['download'], args[0]['timestamp']);
   }

   session.subscribe('speedtest', onSpeedTestResult);
   
   function onCpuPercent(args) {
   	  anvil.call(form, 'raise_cpu_percent_event', cpu_percent=args[0]);
   }
   
   session.subscribe('cpu_percent', onCpuPercent);
};

connection.open();