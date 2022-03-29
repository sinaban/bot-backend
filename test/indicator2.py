indicator_properties = {
        'BBANDS': {'IndicatorName': 'BBANDS', 'description': 'Bollinger Bands', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 5, 'nbdevup': 2, 'nbdevdn': 2, 'matype': 0}},
        'DEMA': {'IndicatorName': 'DEMA', 'description': 'Double Exponential Moving Average', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 30}}, 
        'EMA': {'IndicatorName': 'EMA', 'description': 'Exponential Moving Average', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 30}}, 
        'HT_TRENDLINE': {'IndicatorName': 'HT_TRENDLINE', 'description': 'Hilbert Transform - Instantaneous Trendline', 'params': {'suffix': '', 'CandlePricePoint': 'close'}}, 
        'KAMA': {'IndicatorName': 'KAMA', 'description': 'Kaufman Adaptive Moving Average', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 30}}, 
        'MA': {'IndicatorName': 'MA', 'description': 'Moving average', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 30, 'matype': 0}}, 
        'MAMA': {'IndicatorName': 'MAMA', 'description': 'MESA Adaptive Moving Average', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'fastlimit': 0, 'slowlimit': 0}}, 
        'MAVP': {'IndicatorName': 'MAVP', 'description': 'Moving average with variable period', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'periods': '', 'minperiod': 2, 'maxperiod': 30, 'matype': 0}}, 
        'MIDPOINT': {'IndicatorName': 'MIDPOINT', 'description': 'MidPoint over period', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 14}}, 
        'MIDPRICE': {'IndicatorName': 'MIDPRICE', 'description': 'Midpoint Price over period', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'timeperiod': 14}}, 
        'SAR': {'IndicatorName': 'SAR', 'description': 'Parabolic SAR', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'acceleration': 0, 'maximum': 0}}, 
        'SAREXT': {'IndicatorName': 'SAREXT', 'description': 'Parabolic SAR - Extended', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'startvalue': 0, 'offsetonreverse': 0, 'accelerationinitlong': 0, 'accelerationlong': 0, 'accelerationmaxlong': 0, 'accelerationinitshort': 0, 'accelerationshort': 0, 'accelerationmaxshort': 0}}, 
        'SMA': {'IndicatorName': 'SMA', 'description': 'Simple Moving Average', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 30}}, 
        'T3': {'IndicatorName': 'T3', 'description': 'Triple Exponential Moving Average', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 5, 'vfactor': 0}}, 
        'TEMA': {'IndicatorName': 'TEMA', 'description': 'Triple Exponential Moving Average', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 30}}, 
        'TRIMA': {'IndicatorName': 'TRIMA', 'description': 'Triangular Moving Average', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 30}}, 
        'WMA': {'IndicatorName': 'WMA', 'description': 'Weighted Moving Average', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 30}}, 
        'ADX': {'IndicatorName': 'ADX', 'description': 'Average Directional Movement Index', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close', 'timeperiod': 14}}, 
        'ADXR': {'IndicatorName': 'ADXR', 'description': 'Average Directional Movement Index Rating', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close', 'timeperiod': 14}}, 
        'APO': {'IndicatorName': 'APO', 'description': 'Absolute Price Oscillator', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'fastperiod': 12, 'slowperiod': 26, 'matype': 0}}, 
        'AROON': {'IndicatorName': 'AROON', 'description': 'Aroon', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'timeperiod': 14}}, 
        'AROONOSC': {'IndicatorName': 'AROONOSC', 'description': 'Aroon Oscillator', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'timeperiod': 14}}, 
        'BOP': {'IndicatorName': 'BOP', 'description': 'Balance Of Power', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CCI': {'IndicatorName': 'CCI', 'description': 'Commodity Channel Index', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close', 'timeperiod': 14}}, 
        'CMO': {'IndicatorName': 'CMO', 'description': 'Chande Momentum Oscillator', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 14}}, 
        'DX': {'IndicatorName': 'DX', 'description': 'Directional Movement Index', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close', 'timeperiod': 14}}, 
        'MACD': {'IndicatorName': 'MACD', 'description': 'Moving Average Convergence/Divergence', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'fastperiod': 12, 'slowperiod': 26, 'signalperiod': 9}}, 
        'MACDEXT': {'IndicatorName': 'MACDEXT', 'description': 'MACD with controllable MA type', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'fastperiod': 12, 'fastmatype': 0, 'slowperiod': 26, 'slowmatype': 0, 'signalperiod': 9, 'signalmatype': 0}}, 
        'MACDFIX': {'IndicatorName': 'MACDFIX', 'description': 'Moving Average Convergence/Divergence Fix 12/26', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'signalperiod': 9}}, 
        'MFI': {'IndicatorName': 'MFI', 'description': 'Money Flow Index', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close', 'volume': '', 'timeperiod': 14}}, 
        'MINUS_DI': {'IndicatorName': 'MINUS_DI', 'description': 'Minus Directional Indicator', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close', 'timeperiod': 14}}, 
        'MINUS_DM': {'IndicatorName': 'MINUS_DM', 'description': 'Minus Directional Movement', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'timeperiod': 14}}, 
        'MOM': {'IndicatorName': 'MOM', 'description': 'Momentum', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 10}}, 
        'PLUS_DI': {'IndicatorName': 'PLUS_DI', 'description': 'Plus Directional Indicator', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close', 'timeperiod': 14}}, 
        'PLUS_DM': {'IndicatorName': 'PLUS_DM', 'description': 'Plus Directional Movement', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'timeperiod': 14}}, 
        'PPO': {'IndicatorName': 'PPO', 'description': 'Percentage Price Oscillator', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'fastperiod': 12, 'slowperiod': 26, 'matype': 0}}, 
        'ROC': {'IndicatorName': 'ROC', 'description': 'Rate of change : ((price/prevPrice)-1)*100', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 10}}, 
        'ROCP': {'IndicatorName': 'ROCP', 'description': 'Rate of change Percentage: (price-prevPrice)/prevPrice', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 10}}, 
        'ROCR': {'IndicatorName': 'ROCR', 'description': 'Rate of change ratio: (price/prevPrice)', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 10}}, 
        'ROCR100': {'IndicatorName': 'ROCR100', 'description': 'Rate of change ratio 100 scale: (price/prevPrice)*100', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 10}}, 
        'RSI': {'IndicatorName': 'RSI', 'description': 'Relative Strength Index', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 14}}, 
        'STOCH': {'IndicatorName': 'STOCH', 'description': 'Stochastic', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close', 'fastk_period': 5, 'slowk_period': 3, 'slowk_matype': 0, 'slowd_period': 3, 'slowd_matype': 0}}, 
        'STOCHF': {'IndicatorName': 'STOCHF', 'description': 'Stochastic Fast', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close', 'fastk_period': 5, 'fastd_period': 3, 'fastd_matype': 0}}, 
        'STOCHRSI': {'IndicatorName': 'STOCHRSI', 'description': 'Stochastic Relative Strength Index', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 14, 'fastk_period': 5, 'fastd_period': 3, 'fastd_matype': 0}}, 
        'TRIX': {'IndicatorName': 'TRIX', 'description': '1-day Rate-Of-Change (ROC) of a Triple Smooth EMA', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 30}}, 
        'ULTOSC': {'IndicatorName': 'ULTOSC', 'description': 'Ultimate Oscillator', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close', 'timeperiod1': 7, 'timeperiod2': 14, 'timeperiod3': 28}}, 
        'WILLR': {'IndicatorName': 'WILLR', 'description': "Williams' %R", 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close', 'timeperiod': 14}}, 
        'AD': {'IndicatorName': 'AD', 'description': 'Chaikin A/D Line', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close', 'volume': ''}}, 
        'ADOSC': {'IndicatorName': 'ADOSC', 'description': 'Chaikin A/D Oscillator', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close', 'volume': '', 'fastperiod': 3, 'slowperiod': 10}}, 
        'OBV': {'IndicatorName': 'OBV', 'description': 'On Balance Volume', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'volume': ''}},
        'ATR': {'IndicatorName': 'ATR', 'description': 'Average True Range', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close', 'timeperiod': 14}}, 
        'NATR': {'IndicatorName': 'NATR', 'description': 'Normalized Average True Range', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close', 'timeperiod': 14}}, 
        'TRANGE': {'IndicatorName': 'TRANGE', 'description': 'True Range', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'AVGPRICE': {'IndicatorName': 'AVGPRICE', 'description': 'Average Price', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'MEDPRICE': {'IndicatorName': 'MEDPRICE', 'description': 'Median Price', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low'}}, 
        'TYPPRICE': {'IndicatorName': 'TYPPRICE', 'description': 'Typical Price', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'WCLPRICE': {'IndicatorName': 'WCLPRICE', 'description': 'Weighted Close Price', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'HT_DCPERIOD': {'IndicatorName': 'HT_DCPERIOD', 'description': 'Hilbert Transform - Dominant Cycle Period', 'params': {'suffix': '', 'CandlePricePoint': 'close'}}, 
        'HT_DCPHASE': {'IndicatorName': 'HT_DCPHASE', 'description': 'Hilbert Transform - Dominant Cycle Phase', 'params': {'suffix': '', 'CandlePricePoint': 'close'}}, 
        'HT_PHASOR': {'IndicatorName': 'HT_PHASOR', 'description': 'Hilbert Transform - Phasor Components', 'params': {'suffix': '', 'CandlePricePoint': 'close'}}, 
        'HT_SINE': {'IndicatorName': 'HT_SINE', 'description': 'Hilbert Transform - SineWave', 'params': {'suffix': '', 'CandlePricePoint': 'close'}}, 
        'HT_TRENDMODE': {'IndicatorName': 'HT_TRENDMODE', 'description': 'Hilbert Transform - Trend vs Cycle Mode', 'params': {'suffix': '', 'CandlePricePoint': 'close'}}, 
        'CDL2CROWS': {'IndicatorName': 'CDL2CROWS', 'description': 'Two Crows', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDL3BLACKCROWS': {'IndicatorName': 'CDL3BLACKCROWS', 'description': 'Three Black Crows', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDL3INSIDE': {'IndicatorName': 'CDL3INSIDE', 'description': 'Three Inside Up/Down', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDL3LINESTRIKE': {'IndicatorName': 'CDL3LINESTRIKE', 'description': 'Three-Line Strike', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDL3OUTSIDE': {'IndicatorName': 'CDL3OUTSIDE', 'description': 'Three Outside Up/Down', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDL3STARSINSOUTH': {'IndicatorName': 'CDL3STARSINSOUTH', 'description': 'Three Stars In The South', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDL3WHITESOLDIERS': {'IndicatorName': 'CDL3WHITESOLDIERS', 'description': 'Three Advancing White Soldiers', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLABANDONEDBABY': {'IndicatorName': 'CDLABANDONEDBABY', 'description': 'Abandoned Baby', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close', 'penetration': 0}}, 
        'CDLADVANCEBLOCK': {'IndicatorName': 'CDLADVANCEBLOCK', 'description': 'Advance Block', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLBELTHOLD': {'IndicatorName': 'CDLBELTHOLD', 'description': 'Belt-hold', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLBREAKAWAY': {'IndicatorName': 'CDLBREAKAWAY', 'description': 'Breakaway', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLCLOSINGMARUBOZU': {'IndicatorName': 'CDLCLOSINGMARUBOZU', 'description': 'Closing Marubozu', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLCONCEALBABYSWALL': {'IndicatorName': 'CDLCONCEALBABYSWALL', 'description': 'Concealing Baby Swallow', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLCOUNTERATTACK': {'IndicatorName': 'CDLCOUNTERATTACK', 'description': 'Counterattack', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLDARKCLOUDCOVER': {'IndicatorName': 'CDLDARKCLOUDCOVER', 'description': 'Dark Cloud Cover', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close', 'penetration': 0}}, 
        'CDLDOJI': {'IndicatorName': 'CDLDOJI', 'description': 'Doji', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLDOJISTAR': {'IndicatorName': 'CDLDOJISTAR', 'description': 'Doji Star', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLDRAGONFLYDOJI': {'IndicatorName': 'CDLDRAGONFLYDOJI', 'description': 'Dragonfly Doji', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLENGULFING': {'IndicatorName': 'CDLENGULFING', 'description': 'Engulfing Pattern', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLEVENINGDOJISTAR': {'IndicatorName': 'CDLEVENINGDOJISTAR', 'description': 'Evening Doji Star', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close', 'penetration': 0}}, 
        'CDLEVENINGSTAR': {'IndicatorName': 'CDLEVENINGSTAR', 'description': 'Evening Star', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close', 'penetration': 0}}, 
        'CDLGAPSIDESIDEWHITE': {'IndicatorName': 'CDLGAPSIDESIDEWHITE', 'description': 'Up/Down-gap side-by-side white lines', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLGRAVESTONEDOJI': {'IndicatorName': 'CDLGRAVESTONEDOJI', 'description': 'Gravestone Doji', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLHAMMER': {'IndicatorName': 'CDLHAMMER', 'description': 'Hammer', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLHANGINGMAN': {'IndicatorName': 'CDLHANGINGMAN', 'description': 'Hanging Man', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLHARAMI': {'IndicatorName': 'CDLHARAMI', 'description': 'Harami Pattern', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLHARAMICROSS': {'IndicatorName': 'CDLHARAMICROSS', 'description': 'Harami Cross Pattern', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLHIGHWAVE': {'IndicatorName': 'CDLHIGHWAVE', 'description': 'High-Wave Candle', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLHIKKAKE': {'IndicatorName': 'CDLHIKKAKE', 'description': 'Hikkake Pattern', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLHIKKAKEMOD': {'IndicatorName': 'CDLHIKKAKEMOD', 'description': 'Modified Hikkake Pattern', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLHOMINGPIGEON': {'IndicatorName': 'CDLHOMINGPIGEON', 'description': 'Homing Pigeon', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLIDENTICAL3CROWS': {'IndicatorName': 'CDLIDENTICAL3CROWS', 'description': 'Identical Three Crows', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLINNECK': {'IndicatorName': 'CDLINNECK', 'description': 'In-Neck Pattern', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLINVERTEDHAMMER': {'IndicatorName': 'CDLINVERTEDHAMMER', 'description': 'Inverted Hammer', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLKICKING': {'IndicatorName': 'CDLKICKING', 'description': 'Kicking', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLKICKINGBYLENGTH': {'IndicatorName': 'CDLKICKINGBYLENGTH', 'description': 'Kicking - bull/bear determined by the longer marubozu', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLLADDERBOTTOM': {'IndicatorName': 'CDLLADDERBOTTOM', 'description': 'Ladder Bottom', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLLONGLEGGEDDOJI': {'IndicatorName': 'CDLLONGLEGGEDDOJI', 'description': 'Long Legged Doji', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLLONGLINE': {'IndicatorName': 'CDLLONGLINE', 'description': 'Long Line Candle', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLMARUBOZU': {'IndicatorName': 'CDLMARUBOZU', 'description': 'Marubozu', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLMATCHINGLOW': {'IndicatorName': 'CDLMATCHINGLOW', 'description': 'Matching Low', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLMATHOLD': {'IndicatorName': 'CDLMATHOLD', 'description': 'Mat Hold', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close', 'penetration': 0}}, 
        'CDLMORNINGDOJISTAR': {'IndicatorName': 'CDLMORNINGDOJISTAR', 'description': 'Morning Doji Star', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close', 'penetration': 0}}, 
        'CDLMORNINGSTAR': {'IndicatorName': 'CDLMORNINGSTAR', 'description': 'Morning Star', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close', 'penetration': 0}}, 
        'CDLONNECK': {'IndicatorName': 'CDLONNECK', 'description': 'On-Neck Pattern', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLPIERCING': {'IndicatorName': 'CDLPIERCING', 'description': 'Piercing Pattern', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLRICKSHAWMAN': {'IndicatorName': 'CDLRICKSHAWMAN', 'description': 'Rickshaw Man', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLRISEFALL3METHODS': {'IndicatorName': 'CDLRISEFALL3METHODS', 'description': 'Rising/Falling Three Methods', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLSEPARATINGLINES': {'IndicatorName': 'CDLSEPARATINGLINES', 'description': 'Separating Lines', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLSHOOTINGSTAR': {'IndicatorName': 'CDLSHOOTINGSTAR', 'description': 'Shooting Star', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLSHORTLINE': {'IndicatorName': 'CDLSHORTLINE', 'description': 'Short Line Candle', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLSPINNINGTOP': {'IndicatorName': 'CDLSPINNINGTOP', 'description': 'Spinning Top', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLSTALLEDPATTERN': {'IndicatorName': 'CDLSTALLEDPATTERN', 'description': 'Stalled Pattern', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLSTICKSANDWICH': {'IndicatorName': 'CDLSTICKSANDWICH', 'description': 'Stick Sandwich', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLTAKURI': {'IndicatorName': 'CDLTAKURI', 'description': 'Takuri (Dragonfly Doji with very long lower shadow)', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLTASUKIGAP': {'IndicatorName': 'CDLTASUKIGAP', 'description': 'Tasuki Gap', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLTHRUSTING': {'IndicatorName': 'CDLTHRUSTING', 'description': 'Thrusting Pattern', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLTRISTAR': {'IndicatorName': 'CDLTRISTAR', 'description': 'Tristar Pattern', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLUNIQUE3RIVER': {'IndicatorName': 'CDLUNIQUE3RIVER', 'description': 'Unique 3 River', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLUPSIDEGAP2CROWS': {'IndicatorName': 'CDLUPSIDEGAP2CROWS', 'description': 'Upside Gap Two Crows', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'CDLXSIDEGAP3METHODS': {'IndicatorName': 'CDLXSIDEGAP3METHODS', 'description': 'Upside/Downside Gap Three Methods', 'params': {'suffix': '', 'CandleOpen': 'Open', 'CandleHigh': 'high', 'CandleLow': 'low', 'self.CandleClose': 'close'}}, 
        'BETA': {'IndicatorName': 'BETA', 'description': 'Beta', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'timeperiod': 5}}, 
        'CORREL': {'IndicatorName': 'CORREL', 'description': "Pearson's Correlation Coefficient (r)", 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low', 'timeperiod': 30}}, 
        'LINEARREG': {'IndicatorName': 'LINEARREG', 'description': 'Linear Regression', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 14}}, 
        'LINEARREG_ANGLE': {'IndicatorName': 'LINEARREG_ANGLE', 'description': 'Linear Regression Angle', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 14}}, 
        'LINEARREG_INTERCEPT': {'IndicatorName': 'LINEARREG_INTERCEPT', 'description': 'Linear Regression Intercept', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 14}}, 
        'LINEARREG_SLOPE': {'IndicatorName': 'LINEARREG_SLOPE', 'description': 'Linear Regression Slope', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 14}}, 
        'STDDEV': {'IndicatorName': 'STDDEV', 'description': 'Standard Deviation', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 5, 'nbdev': 1}}, 
        'TSF': {'IndicatorName': 'TSF', 'description': 'Time Series Forecast', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 14}}, 
        'VAR': {'IndicatorName': 'VAR', 'description': 'Variance', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 5, 'nbdev': 1}}, 
        'ACOS': {'IndicatorName': 'ACOS', 'description': 'Vector Trigonometric ACos', 'params': {'suffix': '', 'CandlePricePoint': 'close'}}, 
        'ASIN': {'IndicatorName': 'ASIN', 'description': 'Vector Trigonometric ASin', 'params': {'suffix': '', 'CandlePricePoint': 'close'}}, 
        'ATAN': {'IndicatorName': 'ATAN', 'description': 'Vector Trigonometric ATan', 'params': {'suffix': '', 'CandlePricePoint': 'close'}}, 
        'CEIL': {'IndicatorName': 'CEIL', 'description': 'Vector Ceil', 'params': {'suffix': '', 'CandlePricePoint': 'close'}}, 
        'COS': {'IndicatorName': 'COS', 'description': 'Vector Trigonometric Cos', 'params': {'suffix': '', 'CandlePricePoint': 'close'}}, 
        'COSH': {'IndicatorName': 'COSH', 'description': 'Vector Trigonometric Cosh', 'params': {'suffix': '', 'CandlePricePoint': 'close'}}, 
        'EXP': {'IndicatorName': 'EXP', 'description': 'Vector Arithmetic Exp', 'params': {'suffix': '', 'CandlePricePoint': 'close'}}, 
        'FLOOR': {'IndicatorName': 'FLOOR', 'description': 'Vector Floor', 'params': {'suffix': '', 'CandlePricePoint': 'close'}}, 
        'LN': {'IndicatorName': 'LN', 'description': 'Vector Log Natural', 'params': {'suffix': '', 'CandlePricePoint': 'close'}}, 
        'LOG10': {'IndicatorName': 'LOG10', 'description': 'Vector Log10', 'params': {'suffix': '', 'CandlePricePoint': 'close'}}, 'SIN': {'IndicatorName': 'SIN', 'description': 'Vector Trigonometric Sin', 'params': {'suffix': '', 'CandlePricePoint': 'close'}}, 
        'SINH': {'IndicatorName': 'SINH', 'description': 'Vector Trigonometric Sinh', 'params': {'suffix': '', 'CandlePricePoint': 'close'}}, 
        'SQRT': {'IndicatorName': 'SQRT', 'description': 'Vector Square Root', 'params': {'suffix': '', 'CandlePricePoint': 'close'}}, 
        'TAN': {'IndicatorName': 'TAN', 'description': 'Vector Trigonometric Tan', 'params': {'suffix': '', 'CandlePricePoint': 'close'}}, 
        'TANH': {'IndicatorName': 'TANH', 'description': 'Vector Trigonometric Tanh', 'params': {'suffix': '', 'CandlePricePoint': 'close'}}, 
        'ADD': {'IndicatorName': 'ADD', 'description': 'Vector Arithmetic Add', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low'}}, 
        'DIV': {'IndicatorName': 'DIV', 'description': 'Vector Arithmetic Div', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low'}}, 
        'MAX': {'IndicatorName': 'MAX', 'description': 'Highest value over a specified period', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 30}}, 
        'MAXINDEX': {'IndicatorName': 'MAXINDEX', 'description': 'Index of highest value over a specified period', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 30}}, 
        'MIN': {'IndicatorName': 'MIN', 'description': 'Lowest value over a specified period', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 30}}, 
        'MININDEX': {'IndicatorName': 'MININDEX', 'description': 'Index of lowest value over a specified period', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 30}}, 
        'MINMAX': {'IndicatorName': 'MINMAX', 'description': 'Lowest and highest values over a specified period', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 30}}, 
        'MINMAXINDEX': {'IndicatorName': 'MINMAXINDEX', 'description': 'Indexes of lowest and highest values over a specified period', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 30}}, 
        'MULT': {'IndicatorName': 'MULT', 'description': 'Vector Arithmetic Mult', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low'}}, 
        'SUB': {'IndicatorName': 'SUB', 'description': 'Vector Arithmetic Substraction', 'params': {'suffix': '', 'CandleHigh': 'high', 'CandleLow': 'low'}}, 
        'SUM': {'IndicatorName': 'SUM', 'description': 'Summation', 'params': {'suffix': '', 'CandlePricePoint': 'close', 'timeperiod': 30}}
        }