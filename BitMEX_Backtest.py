import locale
import np
locale.setlocale(locale.LC_ALL, 'en_US')
from datetime import datetime, timedelta
import csv

fake_data = [
    ['147.6', '3750.5', '2019-01-04 19:00:00', 'buy'],
    ['150.15', '3788', '2019-01-06 02:00:00', 'sell'],
    ['104.7', '3422', '2019-01-30 06:00:00', 'buy'],
    ['106.3', '3417', '2019-01-31 14:00:00', 'sell'],
    ['103.45', '3364.5', '2019-02-07 01:00:00', 'buy'],
    ['120.65', '3575.5', '2019-02-13 17:00:00', 'sell'],
    ['121.55', '3585.5', '2019-02-16 08:00:00', 'buy'],
    ['140.75', '3981', '2019-03-16 23:00:00', 'sell'],
    ['136.25', '3982', '2019-03-22 14:00:00', 'buy'],
    ['176.7', '5213', '2019-04-09 20:00:00', 'sell'],
    ['164.3', '5074', '2019-04-14 16:00:00', 'buy'],
    ['153.8', '5139.5', '2019-04-28 20:00:00', 'sell'],
    ['152.25', '5141', '2019-04-30 00:00:00', 'buy'],
    ['170.2', '5836.5', '2019-05-07 21:00:00', 'sell'],
    ['166.55', '6041', '2019-05-09 19:00:00', 'buy'],
    ['242.8', '7417.5', '2019-05-17 03:00:00', 'sell'],
    ['245.8', '7716', '2019-05-19 03:00:00', 'buy'],
    ['269.4', '8682.5', '2019-05-29 01:00:00', 'sell'],
    ['262.6', '8510', '2019-05-31 21:00:00', 'buy'],
    ['244.25', '7871.5', '2019-06-08 21:00:00', 'sell'],
    ['234.3', '7664', '2019-06-10 11:00:00', 'buy'],
    ['270.6', '9275.5', '2019-06-18 04:00:00', 'sell'],
    ['268.6', '9268', '2019-06-19 23:00:00', 'buy'],
    ['309', '11762.5', '2019-06-30 10:00:00', 'sell'],
    ['288.35', '10676', '2019-07-02 22:00:00', 'buy'],
    ['308.25', '12972', '2019-07-10 10:00:00', 'sell'],
    ['211.4', '9695.5', '2019-07-18 00:00:00', 'buy'],
    ['227.25', '10681', '2019-07-21 10:00:00', 'sell'],
    ['209.2', '9564.5', '2019-07-24 17:00:00', 'buy'],
    ['228.85', '11707', '2019-08-06 18:00:00', 'sell'],
    ['209.75', '11324', '2019-08-11 11:00:00', 'buy'],
    ['191.75', '10316.5', '2019-08-24 08:00:00', 'sell'],
    ['192.15', '10463.5', '2019-08-26 02:00:00', 'buy'],
    ['176.4', '10897', '2019-09-06 17:00:00', 'sell'],
    ['172.55', '10431', '2019-09-07 12:00:00', 'buy'],
    ['181.1', '10244.5', '2019-09-10 11:00:00', 'sell'],
    ['178.2', '10125.5', '2019-09-12 10:00:00', 'buy'],
    ['215.3', '9970', '2019-09-21 18:00:00', 'sell'],
    ['166.05', '7755', '2019-09-30 07:00:00', 'buy'],
    ['175.05', '8057', '2019-10-06 04:00:00', 'sell'],
    ['171.05', '7828.5', '2019-10-07 07:00:00', 'buy'],
    ['184.25', '8306.5', '2019-10-11 12:00:00', 'sell'],
    ['182.2', '8345', '2019-10-13 10:00:00', 'buy'],
    ['173.3', '8251', '2019-10-22 11:00:00', 'sell'],
    ['163', '7476', '2019-10-25 08:00:00', 'buy'],
    ['186.25', '9206.5', '2019-10-30 09:00:00', 'sell'],
    ['183.3', '9216.5', '2019-11-01 23:00:00', 'buy'],
    ['189.3', '9286', '2019-11-07 07:00:00', 'sell'],
    ['181', '8479', '2019-11-17 05:00:00', 'buy'],
    ['182.8', '8443', '2019-11-18 07:00:00', 'sell'],
    ['148.1', '7166.5', '2019-11-25 15:00:00', 'buy'],
    ['153.65', '7719.5', '2019-11-30 10:00:00', 'sell'],
    ['146.75', '7378', '2019-12-06 15:00:00', 'buy'],
    ['148.1', '7419.5', '2019-12-09 16:00:00', 'sell'],
    ['143.95', '7179.5', '2019-12-12 14:00:00', 'buy'],
    ['143.1', '7181', '2019-12-14 10:00:00', 'sell'],
    ['129.05', '6953.5', '2019-12-18 20:00:00', 'buy'],
    ['127.35', '7162', '2019-12-21 06:00:00', 'sell'],
    ['130.45', '7184.5', '2020-01-01 11:00:00', 'buy'],
    ['129.95', '7173.5', '2020-01-01 23:00:00', 'sell'],
    ['139.65', '7886.5', '2020-01-10 13:00:00', 'buy'],
    ['176.4', '9385.5', '2020-01-29 20:00:00', 'sell'],
    ['175.75', '9355.5', '2020-01-30 09:00:00', 'buy'],
    ['187.85', '9273', '2020-02-04 06:00:00', 'sell'],
    ['188.85', '9195', '2020-02-05 03:00:00', 'buy'],
    ['224.45', '10065', '2020-02-10 05:00:00', 'sell'],
    ['259.7', '9663', '2020-02-17 19:00:00', 'buy'],
    ['269.6', '9760.5', '2020-02-24 14:00:00', 'sell'],
    ['221.65', '8544', '2020-02-28 19:00:00', 'buy'],
    ['238.75', '8887', '2020-03-07 22:00:00', 'sell'],
    ['116.75', '5355', '2020-03-18 20:00:00', 'buy'],
    ['135.9', '6653.5', '2020-03-27 11:00:00', 'sell'],
    ['130.45', '6252.5', '2020-03-30 08:00:00', 'buy'],
    ['141.4', '6738', '2020-04-04 00:00:00', 'sell'],
    ['143.35', '6754', '2020-04-04 20:00:00', 'buy'],
    ['184.6', '7192', '2020-04-20 08:00:00', 'sell'],
    ['195', '7711', '2020-04-28 04:00:00', 'buy'],
    ['212.45', '9745.5', '2020-05-09 20:00:00', 'sell'],
    ['188.05', '8708', '2020-05-12 05:00:00', 'buy'],
    ['199.85', '9564.5', '2020-05-15 15:00:00', 'sell'],
    ['199.6', '9390', '2020-05-16 08:00:00', 'buy'],
    ['207.35', '9156.5', '2020-05-24 13:00:00', 'sell'],
    ['201.75', '8815', '2020-05-27 03:00:00', 'buy'],
    ['238.2', '9540', '2020-06-01 07:00:00', 'sell'],
    ['239.6', '9553.5', '2020-06-03 16:00:00', 'buy'],
    ['242.45', '9737.5', '2020-06-05 19:00:00', 'sell'],
    ['236.05', '9412.5', '2020-06-13 11:00:00', 'buy'],
    ['231.2', '9373.5', '2020-06-18 16:00:00', 'sell'],
    ['229.35', '9365', '2020-06-21 02:00:00', 'buy']
]

# _leverage: Represents the amount of leverage on short-side (2, 3, 4 ...)
# _actions: CSV file for the buy / sell actions.
# _shortCoinData: CSV file for the coin that is being shorted.
# _shortCoinSymbol: XBTUSD, ETHUSD, XRPUSD, or BCHUSD
# _startingCapital: Amount of capital to start with, recommend $10,000.
# _fee: 0.00075 is base fee for BitMEX, increase this to account for slippage (e.g. 0.003)
def short_flat_backtest(_leverage, _actions, _shortCoinData, _shortCoinSymbol, _fundingData, _startingCapital, _fee):

    xbt_usd = open("xbt_hourly_abstract.csv", "r")
    xbt_usd_data = xbt_usd.read().split('\n')
    xbt_arr = []

    for line in xbt_usd_data:
        if (line == ''):
            continue
        xbt_arr.append(line.split(','))

    short_coin = open(_shortCoinData, "r")
    short_coin_data = short_coin.read().split('\n')
    short_arr = []

    for line in short_coin_data:
        if (line == ''):
            continue
        short_arr.append(line.split(','))

    actions = open(_actions, "r")
    actions_data = actions.read().split('\n')
    actions_arr = []

    for line in actions_data:
        if (line == ''):
            continue
        actions_arr.append(line.split(','))

    funding = open(_fundingData, "r")
    funding_data = funding.read().split('\n')
    funding_arr = []

    for line in funding_data:
        if (line == ''):
            continue
        funding_arr.append(line.split(','))

    flat_gains = []
    short_gains = []
    total_gains = []
    funding_gains = []

    executed_orders = []

    def Average(list):
        return sum(list) / len(list)

    # Iterate through actions, and compare each buy/sell action against
    # the correct date and price for <CRYPTO> when flat (on a buy) or for
    # the selected <CRYPTO> when short (on a sell).
    for i in actions_arr:

        # Compare dates.

        # "%m/%d/%Y %H:%M"
        # "%Y-%m-%d %H:%M:%S"
        action_date = datetime.strptime(i[1], "%Y-%m-%d %H:%M:%S")

        for j in short_arr:
            short_date = datetime.strptime(j[0], "%Y-%m-%d %H:%M:%S")
            if action_date == short_date:

                for k in xbt_arr:
                    xbt_date = datetime.strptime(k[0], "%Y-%m-%d %H:%M:%S")
                    if action_date == xbt_date:
                        # Determine if action is buy-to-close or sell-to-open.
                        if i[0] == 'buy':
                            print('buy-to-close ' + _shortCoinSymbol + ' @ ' + j[4] + ' w/ XBTUSD @ ' + k[4] + ' on ' + i[1])
                            executed_orders.append([j[4], k[4], i[1], 'buy'])
                        else:
                            print('sell-to-open ' + _shortCoinSymbol + ' @ ' + j[3] + ' w/ XBTUSD @ ' + k[4] + ' on ' + i[1])
                            executed_orders.append([j[3], k[4], i[1], 'sell'])
                        # print('match', i[1], action_date, short_date)
                        # print('prices:', j[4], i[2], (float(j[4]) - float(i[2])) / float(j[4]) * 100)

    # Fetch BTC amount to start account with, relative to initial capital.
    btc_owned = _startingCapital / float(executed_orders[0][1])
    contracts_owned = 0
    funding_total = 0

    firstBuy = True
    firstSell = True

    # Generate BitMEX returns based on executed orders.
    for i in range(0, len(executed_orders)):
        # Handle first buy or sell.
        if firstBuy or firstSell:
            firstBuy = False
            firstSell = False
            if executed_orders[i][3] == 'buy':
                print() # Do nothing on first buy.
            else:
                print(
                    's.t.o. ' + _shortCoinSymbol +
                    ' @ ' + executed_orders[i][0] +
                    ' w/ XBTUSD @ ' + executed_orders[i][1] +
                    ' on ' + executed_orders[i][2]
                )

                # Figure out BTC value per contract.
                btc_per_contract = 0

                if _shortCoinSymbol == 'ETHUSD' or _shortCoinSymbol == 'BCHUSD':
                    btc_per_contract = float(executed_orders[i][0]) / 1000000
                if _shortCoinSymbol == 'XBTUSD':
                    btc_per_contract = 1 / float(executed_orders[i][1])
                if _shortCoinSymbol == 'XRPUSD':
                    btc_per_contract = float(executed_orders[i][0]) / 5000

                # Sell that many contracts, based on leverage.
                contracts_owned = btc_owned / btc_per_contract * _leverage * -1
                fee = abs(contracts_owned * btc_per_contract * _fee)
                btc_owned -= fee
                print('XBT', btc_owned)
                print('Contracts', contracts_owned)
                print()

        # Handle remaining buy or sell, sequentially.
        else:
            if executed_orders[i][3] == 'buy':

                # Calculate position value, hourly rolling.

                # Calculate funding rate, gain or loss.
                dt_start = datetime.strptime(executed_orders[i-1][2], "%Y-%m-%d %H:%M:%S")
                dt_stop = datetime.strptime(executed_orders[i][2], "%Y-%m-%d %H:%M:%S")

                # Unlikely to catch immediate funding the first hour of position.
                dt_start += timedelta(hours=1)

                # Iterate through each hour of the position (for funding rate calculation).
                while dt_stop > dt_start:
                    # print(dt_start)
                    for j in funding_arr:
                        # print(j)
                        funding_dt = datetime.strptime(j[0], '"%Y-%m-%dT%H:%M:%S.000Z"')
                        # Upon match with funding rate datetime, calculate position value.
                        # Add or remove BTC accordingly from account.
                        if funding_dt == dt_start:
                            # print('funding match', j[3], dt_start)
                            # To calculate position value, fetch current XBTUSD and _shortCoin price
                            xbt_price = 0
                            short_coin_price = 0
                            if _shortCoinSymbol == 'ETHUSD' or _shortCoinSymbol == 'BCHUSD' or _shortCoinSymbol == 'XRPUSD':
                                for k in short_arr:
                                    dt_short = datetime.strptime(k[0], "%Y-%m-%d %H:%M:%S")
                                    if dt_short == funding_dt:
                                        short_coin_price = k[3]
                            else:
                                for k in xbt_arr:
                                    dt_xbt = datetime.strptime(k[0], "%Y-%m-%d %H:%M:%S")
                                    if dt_xbt == funding_dt:
                                        xbt_price = k[3]

                            btc_per_contract = 0

                            # PnL Calculation
                            if _shortCoinSymbol == 'ETHUSD' or _shortCoinSymbol == 'BCHUSD':
                                btc_per_contract = float(short_coin_price) / 1000000
                            if _shortCoinSymbol == 'XBTUSD':
                                btc_per_contract = 1 / float(xbt_price)
                            if _shortCoinSymbol == 'XRPUSD':
                                btc_per_contract = float(short_coin_price) / 5000

                            funding = btc_per_contract * abs(contracts_owned) * float(j[3].replace('"',''))

                            # print('XBT', xbt_price, _shortCoinSymbol, short_coin_price)
                            print(
                                'Funding Rate: ',
                                funding,
                                'XBT',
                                ' on ',
                                funding_dt
                            )
                            btc_owned += funding
                            funding_total += funding

                    dt_start += timedelta(hours=1)


                # PnL Calculation exiting short position
                exit_price = float(executed_orders[i][0])
                entry_price = float(executed_orders[i-1][0])
                delta = exit_price - entry_price
                btc_pnl = 0

                # PnL Calculation
                if _shortCoinSymbol == 'ETHUSD' or _shortCoinSymbol == 'BCHUSD':
                    btc_pnl = delta * (.000001) * contracts_owned
                if _shortCoinSymbol == 'XBTUSD':
                    btc_pnl = contracts_owned * (1 / entry_price - 1 / exit_price)
                if _shortCoinSymbol == 'XRPUSD':
                    btc_pnl = delta * (.0002) * contracts_owned

                btc_owned += btc_pnl

                # Calculate fee, then buy-to-close current amount of contracts_owned.
                fee = abs(contracts_owned * btc_per_contract * _fee)
                btc_owned -= fee
                contracts_owned = 0

                print(
                    'b.t.c. ' + _shortCoinSymbol +
                    ' @ ' + executed_orders[i][0] +
                    ' w/ XBTUSD @ ' + executed_orders[i][1] +
                    ' on ' + executed_orders[i][2]
                )

                print('XBT', btc_owned)
                print('Contracts', contracts_owned)
                print()


            else:
                print(
                    's.t.o. ' + _shortCoinSymbol +
                    ' @ ' + executed_orders[i][0] +
                    ' w/ XBTUSD @ ' + executed_orders[i][1] +
                    ' on ' + executed_orders[i][2]
                )

                # Calculate BTC value, hourly rolling.

                # Figure out BTC value per contract.
                btc_per_contract = 0

                if _shortCoinSymbol == 'ETHUSD' or _shortCoinSymbol == 'BCHUSD':
                    btc_per_contract = float(executed_orders[i][0]) / 1000000
                if _shortCoinSymbol == 'XBTUSD':
                    btc_per_contract = 1 / float(executed_orders[i][1])
                if _shortCoinSymbol == 'XRPUSD':
                    btc_per_contract = float(executed_orders[i][0]) / 5000

                # Sell that many contracts, based on leverage.
                contracts_owned = btc_owned / btc_per_contract * _leverage * -1
                fee = abs(contracts_owned * btc_per_contract * _fee)
                btc_owned -= fee
                print('XBT', btc_owned)
                print('Contracts', contracts_owned)
                print()

    print('XBT Final', btc_owned)
    print('Funding Total', funding_total, 'XBT')
    print('XBT to USD', btc_owned * float(executed_orders[len(executed_orders) - 1][1]))

    actions.close()

short_flat_backtest(
    2.5,
    "ichimoku_results_eth.csv",
    "eth_hourly_abstract.csv",
    "ETHUSD",
    "eth_funding_history.csv",
    10000,
    0.005
)

# "ResultsClosedPositions_BTC_1h.csv"
# "ResultsClosedPositions_BCH_1h.csv"
# "ResultsClosedPositions_ETH_1h.csv"
# "ResultsClosedPositions_LTC_1h.csv"
# "xrp_hourly_2020.csv"
# "xbt_hourly_2019_to_2020.csv"
# "eth_hourly_2019_to_2020.csv"
# "bch_hourly_2020.csv"