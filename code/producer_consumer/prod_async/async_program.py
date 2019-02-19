import datetime
import colorama
import random
import time


def main():
    # TODO: Create the asyncio loop

    t0 = datetime.datetime.now()
    print(colorama.Fore.WHITE + "App started.", flush=True)

    data = []  # TODO:  maybe a better data structure?

    # TODO: run these with asyncio.gather()
    generate_data(10, data)
    generate_data(10, data)
    process_data(20, data)

    # TODO: run_until_complete

    dt = datetime.datetime.now() - t0
    print(colorama.Fore.WHITE + "App exiting, total time: {:,.2f} sec.".format(dt.total_seconds()), flush=True)


def generate_data(num: int, data: list):
    for idx in range(1, num + 1):
        item = idx * idx
        # TODO: Use queue
        data.append((item, datetime.datetime.now()))

        print(colorama.Fore.YELLOW + " -- generated item {}".format(idx), flush=True)
        # TODO: Sleep better
        time.sleep(random.random() + .5)


def process_data(num: int, data: list):
    processed = 0
    while processed < num:
        # TODO: Use queue
        item = data.pop(0)
        if not item:
            time.sleep(.01)
            continue

        processed += 1
        value = item[0]
        t = item[1]
        dt = datetime.datetime.now() - t

        print(colorama.Fore.CYAN +
              " +++ Processed value {} after {:,.2f} sec.".format(value, dt.total_seconds()), flush=True)
        # TODO: Sleep better
        time.sleep(.5)


if __name__ == '__main__':
    main()
