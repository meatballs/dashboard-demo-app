# Dashboard Demo

This repository demonstrates the use of an [Anvil](https://anvil.works) app as a front
end to a set of bots which communicate via a [crossbar](https://crossbar.io) router.

In this demo, bot the anvil app and the bot run on the same machine but, as long as all
have access to the same crossbar router, they can be spread over as many machines as
desired.

The bots can be used to perform background tasks asynchronously and publish results via
the router. The anvil app subscribes to the router and displays those results in real
time as they are received.

In this demo, there is a single bot which will:

* perform a broadband speed test every minute
* fetch the cpu load of the local machine every 10 seconds

## Installation

In order to run this demo, you will need access to a crossbar router. You can follow the
[installation instructions](https://crossbar.io/docs/Installation) to install a router
on your local machine.

To install the demo bot and anvil app, clone this repository to your local machine and
install the project's dependencies:

```
git clone https://github.com/meatballs/dashboard-demo-app.git
cd Dashboard_Demo
pip install -r requirements.txt
```

## Startup

To start your crossbar router, open a terminal session, navigate to the root folder
of this project and:

```
cd router
crossbar start
```

To start the bot, open a new terminal session, navigate to the root folder of this
project and:

```
python bot/bot.py
```

And, finally, to start the Anvil app, open a new terminal session, navigate to the root
folder of this project and:

```
anvil-app-server
```

You should now be able to navigate to http://localhost:3030 in your browser and see the
demo app running. It may take a minute or two for the first broadband speed test result
to appear but there is no need to refresh the browser.
