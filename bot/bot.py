import asyncio

import psutil
import txaio
from autobahn.asyncio.component import Component, run
from speedtest import Speedtest

component_kwargs = {
    "transports": "ws://localhost:8080/ws",
    "realm": "dashboard",
}

monitor = Component(**component_kwargs)


txaio.use_asyncio()
logger = txaio.make_logger()


@monitor.on_join
async def run_speedtest(session, details):
    # Not sure why we need this but the first published result never gets picked
    # up by the subscriber.
    session.publish("speedtest")
    while True:
        s = Speedtest()
        logger.info("Starting speedtest...")
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, s.get_best_server)
        await loop.run_in_executor(None, s.download)
        result = {key: s.results.dict()[key] for key in ["download", "timestamp"]}
        logger.info(f"Speedtest completed: {result['download'] / 10 ** 6:.2f} Mbps")
        session.publish("speedtest", result)
        await asyncio.sleep(60)


@monitor.on_join
async def get_cpu_temp(session, details):
    while True:
        result = psutil.cpu_percent()
        logger.info(f"cpu percent: {result}")
        session.publish("cpu_percent", result)
        await asyncio.sleep(10)


if __name__ == "__main__":
    run([monitor])
