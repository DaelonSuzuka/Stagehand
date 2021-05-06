from stagehand.application import get_application
from stagehand.main_window import MainWindow

import asyncio
import functools
import sys
import qasync


def install_async(app, future, loop):
    def close_future(future, loop):
        loop.call_later(10, future.cancel)
        future.cancel()

    if hasattr(app, 'aboutToQuit'):
        getattr(app, 'aboutToQuit').connect(functools.partial(close_future, future, loop))


async def main():
    loop = asyncio.get_event_loop()
    future = asyncio.Future()

    app = get_application()

    install_async(app, future, loop)
    
    window = MainWindow()
    window.show()

    await future

    return True


if __name__ == "__main__":
    try:
        qasync.run(main())
    except (asyncio.exceptions.CancelledError):
        sys.exit(0)