from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import datetime
import os
import sys

import backtrader as bt
import matplotlib

from strategies.test_strategy import TestStrategy



def main():
    print("Hello, World!")
    cerebro = bt.Cerebro()
    #cerebro.addstrategy(TestStrategy, exitbars=10)
    strats = cerebro.optstrategy(
        TestStrategy,
        maperiod=range(11,30))

    # Add a FixedSize sizer according to the stake
    cerebro.addsizer(bt.sizers.FixedSize, stake=10)

    cerebro.broker.setcommission(commission=0.001)


    # Datas are in a subfolder of the samples. Need to find where the script is
    # because it could have been called from anywhere
    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath, '../../backtrader/datas/orcl-1995-2014.txt')

    # Create a Data Feed
    data = bt.feeds.YahooFinanceCSVData(
        dataname=datapath,
        # Do not pass values before this date
        fromdate=datetime.datetime(2000, 1, 1),
        # Do not pass values after this date
        todate=datetime.datetime(2000, 12, 31),
        reverse=False)

    # Add the Data Feed to Cerebro
    cerebro.adddata(data)
    cerebro.broker.setcash(1000.0)

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    #cerebro.plot()


if __name__ == '__main__':
    main()

