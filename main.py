import time

from bot_controller import BotController


# HERE YOU CAN SPECIFY WHICH COIN YOU WANT TO ANALYZE!

if __name__ == '__main__':
    markets_str = 'BTC'
    markets = markets_str.replace(' ', '').upper().split(',')
    markets = [f'{m}USDT' for m in markets]

    controller = BotController(markets)

    controller.start()

    while True:
        time.sleep(1)
        # inp = input('Press q to quit... ')

        # if inp.strip().lower() in ['q', 'quit']:
        #     controller.stop()
        #     break

    # print('Done.')
