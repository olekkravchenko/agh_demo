import argparse
import time
import logging
import threading
logging.basicConfig(level=logging.INFO)


class DemoTestException(Exception):
    pass



def test_throughput(band:int , bandwidth:int, duration:int=10):
    if int(bandwidth) not in [5, 10, 15, 20]:
        raise DemoTestException(f'Invalid bandwidth {bandwidth}')
    if int(band) < 1 or int(band) > 17:
        raise DemoTestException(f'Invalid band {band}')
    # This is intentional error
    logging.info(f'Test througput for band/bandwidth {band}/{bandwidth}')
    for _ in range(duration//2):
        print('.', end='', flush=True)
        time.sleep(2)
    print()
    if int(band) in [1, 3, 5, 7] and int(bandwidth) in [5, 20]:
        raise DemoTestException(f'This combination of band/bandwidth {band}/{bandwidth}MGz does not work')
    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Enter band and bandwidth')
    parser.add_argument('-b, --band', type=int, dest='band')
    parser.add_argument('-w, --bandwidth', type=int, dest='bandwidth')
    parser.add_argument('-d, --duration', type=int, default=10, dest='duration')
    args = parser.parse_args() 
    test_throughput(args.band, args.bandwidth, duration=args.duration)
