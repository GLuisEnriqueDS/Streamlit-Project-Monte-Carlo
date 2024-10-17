import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

currencies_dict  =  {'USD/JPY': 'USDJPY=X', 'USD/BRL': 'BRL=X', 'USD/ARS': 'ARS=X', 'USD/PYG': 'PYG=X', 'USD/UYU': 'UYU=X',
                     'USD/CNY': 'CNY=X', 'USD/KRW': 'KRW=X', 'USD/MXN': 'MXN=X', 'USD/IDR': 'IDR=X', 'USD/EUR': 'EUR=X',
                     'USD/CAD': 'CAD=X', 'USD/GBP': 'GBP=X', 'USD/CHF': 'CHF=X', 'USD/AUD': 'AUD=X', 'USD/NZD': 'NZD=X',
                     'USD/HKD': 'HKD=X', 'USD/SGD': 'SGD=X', 'USD/INR': 'INR=X', 'USD/RUB': 'RUB=X', 'USD/ZAR': 'ZAR=X',
                     'USD/SEK': 'SEK=X', 'USD/NOK': 'NOK=X', 'USD/TRY': 'TRY=X', 'USD/AED': 'AED=X', 'USD/SAR': 'SAR=X',
                     'USD/THB': 'THB=X', 'USD/DKK': 'DKK=X', 'USD/MYR': 'MYR=X', 'USD/PLN': 'PLN=X', 'USD/EGP': 'EGP=X',
                     'USD/CZK': 'CZK=X', 'USD/ILS': 'ILS=X', 'USD/HUF': 'HUF=X', 'USD/PHP': 'PHP=X', 'USD/CLP': 'CLP=X',
                     'USD/COP': 'COP=X', 'USD/PEN': 'PEN=X', 'USD/KWD': 'KWD=X', 'USD/QAR': 'USD/QAR'
                    }
crypto_dict = {'Bitcoin USD': 'BTC-USD', 'Ethereum USD': 'ETH-USD', 'Tether USDT USD': 'USDT-USD',
               'Bnb USD': 'BNB-USD', 'Solana USD': 'SOL-USD', 'Xrp USD': 'XRP-USD', 'Usd Coin USD': 'USDC-USD',
               'Lido Staked Eth USD': 'STETH-USD', 'Cardano USD': 'ADA-USD', 'Avalanche USD': 'AVAX-USD',
               'Dogecoin USD': 'DOGE-USD', 'Wrapped Tron USD': 'WTRX-USD', 'Tron USD': 'TRX-USD',
               'Polkadot USD': 'DOT-USD', 'Chainlink USD': 'LINK-USD', 'Toncoin USD': 'TON11419-USD',
               'Polygon USD': 'MATIC-USD', 'Wrapped Bitcoin USD': 'WBTC-USD', 'Shiba Inu USD': 'SHIB-USD',
               'Internet Computer USD': 'ICP-USD', 'Dai USD': 'DAI-USD', 'Litecoin USD': 'LTC-USD',
               'Bitcoin Cash USD': 'BCH-USD', 'Uniswap USD': 'UNI7083-USD', 'Cosmos USD': 'ATOM-USD',
               'Unus Sed Leo USD': 'LEO-USD', 'Ethereum Classic USD': 'ETC-USD', 'Stellar USD': 'XLM-USD',
               'Okb USD': 'OKB-USD', 'Near Protocol USD': 'NEAR-USD', 'Optimism USD': 'OP-USD',
               'Injective USD': 'INJ-USD', 'Aptos USD': 'APT21794-USD', 'Monero USD': 'XMR-USD',
               'Filecoin USD': 'FIL-USD', 'Lido Dao USD': 'LDO-USD', 'Celestia USD': 'TIA22861-USD',
               'Hedera USD': 'HBAR-USD', 'Wrapped Hbar USD': 'WHBAR-USD', 'Immutable USD': 'IMX10603-USD',
               'Wrapped Eos USD': 'WEOS-USD', 'Arbitrum USD': 'ARB11841-USD', 'Kaspa USD': 'KAS-USD',
               'Bitcoin Bep2 USD': 'BTCB-USD', 'Stacks USD': 'STX4847-USD', 'Mantle USD': 'MNT27075-USD',
               'First Digital Usd Usd': 'FDUSD-USD', 'Vechain USD': 'VET-USD', 'Cronos USD': 'CRO-USD',
               'Wrapped Beacon Eth USD': 'WBETH-USD', 'Trueusd USD': 'TUSD-USD', 'Sei USD': 'SEI-USD',
               'Maker USD': 'MKR-USD', 'Hex USD': 'HEX-USD', 'Rocket Pool Eth USD': 'RETH-USD',
               'Bitcoin Sv USD': 'BSV-USD', 'Render USD': 'RNDR-USD', 'Bittensor USD': 'TAO22974-USD',
               'The Graph USD': 'GRT6719-USD', 'Algorand USD': 'ALGO-USD', 'Ordi USD': 'ORDI-USD',
               'Aave USD': 'AAVE-USD', 'Thorchain USD': 'RUNE-USD', 'Quant USD': 'QNT-USD',
               'Multiversx USD': 'EGLD-USD', 'Sui USD': 'SUI20947-USD', 'Mina USD': 'MINA-USD',
               'Sats USD': '1000SATS-USD', 'Flow USD': 'FLOW-USD', 'Helium USD': 'HNT-USD',
               'Fantom USD': 'FTM-USD', 'Synthetix USD': 'SNX-USD', 'The Sandbox USD': 'SAND-USD',
               'Theta Network USD': 'THETA-USD', 'Axie Infinity USD': 'AXS-USD', 'Tezos USD': 'XTZ-USD',
               'Beam USD': 'BEAM28298-USD', 'Bittorrent(New) USD': 'BTT-USD', 'Kucoin Token USD': 'KCS-USD',
               'Dydx (Ethdydx) USD': 'ETHDYDX-USD', 'Ftx Token USD': 'FTT-USD', 'Astar USD': 'ASTR-USD',
               'Wemix USD': 'WEMIX-USD', 'Blur USD': 'BLUR-USD', 'Cheelee USD': 'CHEEL-USD',
               'Chiliz USD': 'CHZ-USD', 'Bitget Token USD': 'BGB-USD', 'Decentraland USD': 'MANA-USD',
               'Neo USD': 'NEO-USD', 'Osmosis USD': 'OSMO-USD', 'Eos USD': 'EOS-USD', 'Bonk USD': 'BONK-USD',
               'Kava USD': 'KAVA-USD', 'Woo USD': 'WOO-USD', 'Klaytn USD': 'KLAY-USD', 'Flare USD': 'FLR-USD',
               'Oasis Network USD': 'ROSE-USD', 'Iota USD': 'IOTA-USD', 'Usdd USD': 'USDD-USD',
               'Terra Classic USD': 'LUNC-USD'}
commodities_dict = { "BRENT CRUDE OIL LAST DAY FINANC": "BZ=F", "COCOA": "CC=F", "COFFEE": "KC=F", "COPPER": "HG=F",
                    "CORN FUTURES": "ZC=F", "COTTON": "CT=F", "HEATING OIL": "HO=F", "KC HRW WHEAT FUTURES": "KE=F",
                    "LEAN HOGS FUTURES": "HE=F", "LIVE CATTLE FUTURES": "LE=F", "MONT BELVIEU LDH PROPANE (OPIS)": "B0=F",
                    "NATURAL GAS": "NG=F", "ORANGE JUICE": "OJ=F", "GOLD": "GC=F", "OAT FUTURES": "ZO=F",
                    "PALLADIUM": "PA=F", "CRUDE OIL": "CL=F", "PLATINUM": "PL=F", "RBOB GASOLINE": "RB=F",
                    "RANDOM LENGTH LUMBER FUTURES": "LBS=F", "ROUGH RICE FUTURES": "ZR=F", "SILVER": "SI=F",
                    "SOYBEAN FUTURES": "ZS=F", "SOYBEAN OIL FUTURES": "ZL=F", "S&P COMPOSITE 1500 ESG TILTED I": "ZM=F",
                    "SUGAR": "SB=F", "WISDOMTREE INTERNATIONAL HIGH D": "GF=F"
                }
b3_stocks = {"3m": "MMMC34.SA", "Aes brasil": "AESB3.SA", "Af invest": "AFHI11.SA", "Afluente t": "AFLT3.SA", "Agribrasil": "GRAO3.SA",
    "Agogalaxy": "AGXY3.SA", "Alliar": "AALR3.SA", "Alper": "APER3.SA", "Google": "GOGL35.SA", "Alupar investimento": "ALUP4.SA",
    "American express": "AXPB34.SA", "Arcelor": "ARMT34.SA", "Att inc": "ATTB34.SA", "Auren energia": "AURE3.SA", "Banco do brasil": "BBAS3.SA",
    "Banco mercantil de investimentos": "BMIN3.SA", "Banco pan": "BPAN4.SA", "Bank america": "BOAC34.SA", "Banrisul": "BRSR3.SA",
    "Baumer": "BALM3.SA", "Bb seguridade": "BBSE3.SA", "Biomm": "BIOM3.SA", "Bmg": "BMGB4.SA", "Caixa agências": "CXAG11.SA",
    "Camden prop": "C2PT34.SA", "Camil": "CAML3.SA", "Carrefour": "CRFB3.SA", "Cartesia fiici": "CACR11.SA", "Casan": "CASN4.SA",
    "Ceb": "CEBR6.SA", "Ceee-d": "CEED4.SA", "Ceg": "CEGR3.SA", "Celesc": "CLSC4.SA", "Cemig": "CMIG4.SA", "Chevron": "CHVX34.SA",
    "Churchill dw": "C2HD34.SA", "Cisco": "CSCO34.SA", "Citigroup": "CTGP34.SA", "Clearsale": "CLSA3.SA", "Coca-cola": "COCA34.SA",
    "Coelce": "COCE6.SA", "Coinbase glob": "C2OI34.SA", "Colgate": "COLG34.SA", "Comgás": "CGAS3.SA", "Conocophillips": "COPH34.SA",
    "Copel": "CPLE6.SA", "Cpfl energia": "CPFE3.SA", "Csn": "CSNA3.SA", "Dexco": "DXCO3.SA", "Dexxos part": "DEXP3.SA",
    "Dimed": "PNVL3.SA", "Doordash inc": "D2AS34.SA", "Draftkings": "D2KN34.SA", "Ebay": "EBAY34.SA", "Enauta part": "ENAT3.SA",
    "Energisa mt": "ENMT3.SA", "Engie brasil": "EGIE3.SA", "Eqi receci": "EQIR11.SA", "Eucatex": "EUCA4.SA", "Exxon mobil": "EXXO34.SA",
    "Ferbasa": "FESA4.SA", "Fiagro jgp ci": "JGPX11.SA", "Fiagro riza ci": "RZAG11.SA", "Fii brio me ci": "BIME11.SA", "Fii cyrela ci es": "CYCR11.SA",
    "Fii gtis lg": "GTLG11.SA", "Fii husi ci es": "HUSI11.SA", "Fii js a finci": "JSAF11.SA", "Fii more crici er": "MORC11.SA", "Fii rooftopici": "ROOF11.SA",
    "Fleury": "FLRY3.SA", "Freeport": "FCXO34.SA", "Ft cloud cpt": "BKYY39.SA", "Ft dj intern": "BFDN39.SA", "Ft nasd cyber": "BCIR39.SA",
    "Ft nasd100 eq": "BQQW39.SA", "Ft nasd100 tc": "BQTC39.SA", "Ft nat gas": "BFCG39.SA", "Ft nyse biot drn": "BFBI39.SA", "Ft risi divid": "BFDA39.SA",
    "G2d investments": "G2DI33.SA", "Ge": "GEOO34.SA", "General shopping": "GSHP3.SA", "Gerd paranapanema": "GEPA4.SA", "Golias": "GOAU4.SA",
    "Godaddy inc": "G2DD34.SA", "Goldman sachs": "GSGI34.SA", "Grd": "IGBR3.SA", "Halliburton": "HALI34.SA", "Honeywell": "HONB34.SA",
    "Hp company": "HPQB34.SA", "Hypera pharma": "HYPE3.SA", "Ibm": "IBMB34.SA", "Iguatemi s.a.": "IGTI3.SA", "Infracommerce": "IFCM3.SA",
    "Intel": "ITLC34.SA", "Investo alug": "ALUG11.SA", "Investo ustk": "USTK11.SA", "Investo wrld": "WRLD11.SA", "Irb brasil re": "IRBR3.SA",
    "Isa cteep": "TRPL4.SA", "Itaú unibanco": "ITUB4.SA", "Itaúsa": "ITSA4.SA", "Jbs": "JBSS3.SA", "Johnson": "JNJB34.SA",
    "Jpmorgan": "JPMC34.SA", "Kingsoft chl": "K2CG34.SA", "Klabin s/a": "KLBN11.SA", "Livetech": "LVTC3.SA", "Locaweb": "LWSA3.SA",
    "Log": "LOGG3.SA", "Lps brasil": "LPSB3.SA", "Marfrig": "MRFG3.SA", "Mastercard": "MSCD34.SA", "Mdiasbranco": "MDIA3.SA",
    "Melnick": "MELK3.SA", "Meliuz": "CASH3.SA", "Mercado livre": "MELI34.SA", "Microsoft": "MSFT34.SA", "Mrv engenharia": "MRVE3.SA",
    "Natura": "NTCO3.SA", "Netflix": "NFLX34.SA", "Oi": "OIBR3.SA", "Oracle": "ORCL34.SA", "Pão de açúcar": "PCAR3.SA",
    "Petrobras": "PETR4.SA", "Petróleo": "PEAB3.SA", "Pfizer": "PFIZ34.SA", "Plascar": "PLAS3.SA", "Porto seguro": "PSSA3.SA",
    "Positivo": "POSI3.SA", "Procter": "PGCO34.SA", "Qualicorp": "QUAL3.SA", "Randon": "RAPT4.SA", "Raia drogasil": "RADL3.SA",
    "Renner": "LREN3.SA", "Rossi": "RSID3.SA", "Rumo s.a.": "RAIL3.SA", "Santander": "SANB11.SA", "Telefônica": "VIVT3.SA",
    "Tim": "TIMS3.SA", "Totvs": "TOTS3.SA", "Trisul": "TRIS3.SA", "Ultrapar": "UGPA3.SA", "Unipar": "UNIP6.SA", "Usiminas": "USIM5.SA",
    "Vale": "VALE3.SA", "Vivara": "VIVA3.SA", "Vulcabras": "VULC3.SA", "Weg": "WEGE3.SA", "Whirlpool": "WHRL3.SA", "Yduqs": "YDUQ3.SA"
}
indexes_dict ={'S&P GSCI': 'GD=F', 'IBOVESPA': '^BVSP', 'S&P/CLX IPSA': '^IPSA',
                    'MERVAL': '^MERV', 'IPC MEXICO': '^MXX', 'S&P 500': '^GSPC',
                    'Dow Jones Industrial Average': '^DJI', 'NASDAQ Composite': '^IXIC',
                    'NYSE COMPOSITE (DJ)': '^NYA', 'NYSE AMEX COMPOSITE INDEX': '^XAX',
                    'Russell 2000': '^RUT', 'CBOE Volatility Index': '^VIX',
                    'S&P/TSX Composite index': '^GSPTSE', 'FTSE 100': '^FTSE',
                    'DAX PERFORMANCE-INDEX': '^GDAXI', 'CAC 40': '^FCHI',
                    'ESTX 50 PR.EUR': '^STOXX50E', 'Euronext 100 Index': '^N100',
                    'BEL 20': '^BFX', 'MOEX Russia Index': 'IMOEX.ME', 'Nikkei 225': '^N225',
                    'HANG SENG INDEX': '^HSI', 'SSE Composite Index': '000001.SS',
                    'Shenzhen Index': '399001.SZ', 'STI Index': '^STI', 'S&P/ASX 200': '^AXJO',
                    'ALL ORDINARIES': '^AORD', 'S&P BSE SENSEX': '^BSESN', 'IDX COMPOSITE': '^JKSE',
                    'FTSE Bursa Malaysia KLCI': '^KLSE', 'S&P/NZX 50 INDEX GROSS': '^NZ50',
                    'KOSPI Composite Index': '^KS11', 'TSEC weighted index': '^TWII',
                    'TA-125': '^TA125.TA', 'Top 40 USD Net TRI Index': '^JN0U.JO', 'NIFTY 50': '^NSEI'
                    }
sp500_dict = {'3M': 'MMM', 'A. O. Smith': 'AOS', 'Abbott': 'ABT', 'AbbVie': 'ABBV', 'Accenture': 'ACN', 'Adobe Inc.': 'ADBE',
              'Advanced Micro Devices': 'AMD', 'AES Corporation': 'AES', 'Aflac': 'AFL', 'Agilent Technologies': 'A', 'Air Products and Chemicals': 'APD',
              'Airbnb': 'ABNB', 'Akamai': 'AKAM', 'Albemarle Corporation': 'ALB', 'Alexandria Real Estate Equities': 'ARE', 'Align Technology': 'ALGN',
              'Allegion': 'ALLE', 'Alliant Energy': 'LNT', 'Allstate': 'ALL', 'Google': 'GOOGL', 'Google': 'GOOG',
              'Altria': 'MO', 'Amazon': 'AMZN', 'Amcor': 'AMCR', 'Ameren': 'AEE', 'American Airlines Group': 'AAL', 'American Electric Power': 'AEP',
              'American Express': 'AXP', 'American International Group': 'AIG', 'American Tower': 'AMT', 'American Water Works': 'AWK', 'Ameriprise Financial': 'AMP',
              'AMETEK': 'AME', 'Amgen': 'AMGN', 'Amphenol': 'APH', 'Analog Devices': 'ADI', 'ANSYS': 'ANSS', 'Aon': 'AON',
              'APA Corporation': 'APA', 'Apple Inc.': 'AAPL', 'Applied Materials': 'AMAT', 'Aptiv': 'APTV', 'Arch Capital Group': 'ACGL', 'Archer-Daniels-Midland': 'ADM',
              'Arista Networks': 'ANET', 'Arthur J. Gallagher & Co.': 'AJG', 'Assurant': 'AIZ', 'AT&T': 'T', 'Atmos Energy': 'ATO', 'Autodesk': 'ADSK',
              'Automated Data Processing': 'ADP', 'AutoZone': 'AZO', 'Avalonbay Communities': 'AVB', 'Avery Dennison': 'AVY', 'Axon Enterprise': 'AXON', 'Baker Hughes': 'BKR',
              'Ball Corporation': 'BALL', 'Bank of America': 'BAC', 'Bank of New York Mellon': 'BK', 'Bath & Body Works, Inc.': 'BBWI', 'Baxter International': 'BAX', 'Becton Dickinson': 'BDX',
              'Berkshire Hathaway': 'BRK.B', 'Best Buy': 'BBY', 'Bio-Rad': 'BIO', 'Bio-Techne': 'TECH', 'Biogen': 'BIIB', 'BlackRock': 'BLK', 'Blackstone': 'BX',
              'Boeing': 'BA', 'Booking Holdings': 'BKNG', 'BorgWarner': 'BWA', 'Boston Properties': 'BXP', 'Boston Scientific': 'BSX', 'Bristol Myers Squibb': 'BMY', 'Broadcom Inc.': 'AVGO',
              'Broadridge Financial Solutions': 'BR', 'Brown & Brown': 'BRO', 'Brown–Forman': 'BF.B', 'Builders FirstSource': 'BLDR', 'Bunge Global SA': 'BG', 'Cadence Design Systems': 'CDNS',
              'Caesars Entertainment': 'CZR', 'Camden Property Trust': 'CPT', 'Campbell Soup Company': 'CPB', 'Capital One': 'COF', 'Cardinal Health': 'CAH', 'CarMax': 'KMX',
              'Carnival': 'CCL', 'Carrier Global': 'CARR', 'Catalent': 'CTLT', 'Caterpillar Inc.': 'CAT', 'Cboe Global Markets': 'CBOE', 'CBRE Group': 'CBRE', 'CDW': 'CDW',
              'Celanese': 'CE', 'Cencora': 'COR', 'Centene Corporation': 'CNC', 'CenterPoint Energy': 'CNP', 'Ceridian': 'CDAY', 'CF Industries': 'CF', 'CH Robinson': 'CHRW',
              'Charles River Laboratories': 'CRL', 'Charles Schwab Corporation': 'SCHW', 'Charter Communications': 'CHTR', 'Chevron Corporation': 'CVX', 'Chipotle Mexican Grill': 'CMG',
              'Chubb Limited': 'CB', 'Church & Dwight': 'CHD', 'Cigna': 'CI', 'Cincinnati Financial': 'CINF', 'Cintas': 'CTAS', 'Cisco': 'CSCO', 'Citigroup': 'C',
              'Citizens Financial Group': 'CFG', 'Clorox': 'CLX', 'CME Group': 'CME', 'CMS Energy': 'CMS', 'Coca-Cola Company (The)': 'KO', 'Cognizant': 'CTSH', 'Colgate-Palmolive': 'CL',
              'Comcast': 'CMCSA', 'Comerica': 'CMA', 'Conagra Brands': 'CAG', 'ConocoPhillips': 'COP', 'Consolidated Edison': 'ED', 'Constellation Brands': 'STZ', 'Constellation Energy': 'CEG',
              'CooperCompanies': 'COO', 'Copart': 'CPRT', 'Corning Inc.': 'GLW', 'Corteva': 'CTVA', 'CoStar Group': 'CSGP', 'Costco': 'COST', 'Coterra': 'CTRA', 'Crown Castle': 'CCI',
              'CSX': 'CSX', 'Cummins': 'CMI', 'CVS Health': 'CVS', 'Danaher Corporation': 'DHR', 'Darden Restaurants': 'DRI', 'DaVita Inc.': 'DVA', 'John Deere': 'DE', 'Delta Air Lines': 'DAL',
              'Dentsply Sirona': 'XRAY', 'Devon Energy': 'DVN', 'Dexcom': 'DXCM', 'Diamondback Energy': 'FANG', 'Digital Realty': 'DLR', 'Discover Financial': 'DFS', 'Dollar General': 'DG',
              'Dollar Tree': 'DLTR', 'Dominion Energy': 'D', 'Domino\'s': 'DPZ', 'Dover Corporation': 'DOV', 'Dow Inc.': 'DOW', 'DR Horton': 'DHI', 'DTE Energy': 'DTE', 'Duke Energy': 'DUK',
              'Dupont': 'DD', 'Eastman Chemical Company': 'EMN', 'Eaton Corporation': 'ETN', 'eBay': 'EBAY', 'Ecolab': 'ECL', 'Edison International': 'EIX', 'Edwards Lifesciences': 'EW',
              'Electronic Arts': 'EA', 'Elevance Health': 'ELV', 'Eli Lilly and Company': 'LLY', 'Emerson Electric': 'EMR', 'Enphase': 'ENPH', 'Entergy': 'ETR', 'EOG Resources': 'EOG',
              'EPAM Systems': 'EPAM', 'EQT': 'EQT', 'Equifax': 'EFX', 'Equinix': 'EQIX', 'Equity Residential': 'EQR', 'Essex Property Trust': 'ESS', 'Estée Lauder Companies (The)': 'EL',
              'Etsy': 'ETSY', 'Everest Re': 'EG', 'Evergy': 'EVRG', 'Eversource': 'ES', 'Exelon': 'EXC', 'Expedia Group': 'EXPE', 'Expeditors International': 'EXPD', 'Extra Space Storage': 'EXR',
              'ExxonMobil': 'XOM', 'F5, Inc.': 'FFIV', 'FactSet': 'FDS', 'Fair Isaac': 'FICO', 'Fastenal': 'FAST', 'Federal Realty': 'FRT', 'FedEx': 'FDX', 'Fidelity National Information Services': 'FIS',
              'Fifth Third Bank': 'FITB', 'First Solar': 'FSLR', 'FirstEnergy': 'FE', 'Fiserv': 'FI', 'FleetCor': 'FLT', 'FMC Corporation': 'FMC', 'Ford Motor Company': 'F', 'Fortinet': 'FTNT',
              'Fortive': 'FTV', 'Fox Corporation (Class A)': 'FOXA', 'Fox Corporation (Class B)': 'FOX', 'Franklin Templeton': 'BEN', 'Freeport-McMoRan': 'FCX', 'Garmin': 'GRMN', 'Gartner': 'IT',
              'GE Healthcare': 'GEHC', 'Gen Digital': 'GEN', 'Generac': 'GNRC', 'General Dynamics': 'GD', 'General Electric': 'GE', 'General Mills': 'GIS', 'General Motors': 'GM', 'Genuine Parts Company': 'GPC',
              'Gilead Sciences': 'GILD', 'Global Payments': 'GPN', 'Globe Life': 'GL', 'Goldman Sachs': 'GS', 'Halliburton': 'HAL', 'Hartford (The)': 'HIG', 'Hasbro': 'HAS', 'HCA Healthcare': 'HCA',
              'Healthpeak': 'PEAK', 'Henry Schein': 'HSIC', 'Hershey\'s': 'HSY', 'Hess Corporation': 'HES', 'Hewlett Packard Enterprise': 'HPE', 'Hilton Worldwide': 'HLT', 'Hologic': 'HOLX',
              'Home Depot (The)': 'HD', 'Honeywell': 'HON', 'Hormel Foods': 'HRL', 'Host Hotels & Resorts': 'HST', 'Howmet Aerospace': 'HWM', 'HP Inc.': 'HPQ', 'Hubbell Incorporated': 'HUBB',
              'Humana': 'HUM', 'Huntington Bancshares': 'HBAN', 'Huntington Ingalls Industries': 'HII', 'IBM': 'IBM', 'IDEX Corporation': 'IEX', 'IDEXX Laboratories': 'IDXX',
              'Illinois Tool Works': 'ITW', 'Illumina': 'ILMN', 'Incyte': 'INCY', 'Ingersoll Rand': 'IR', 'Insulet': 'PODD', 'Intel': 'INTC', 'Intercontinental Exchange': 'ICE',
              'International Flavors & Fragrances': 'IFF', 'International Paper': 'IP', 'Interpublic Group of Companies (The)': 'IPG', 'Intuit': 'INTU', 'Intuitive Surgical': 'ISRG',
              'Invesco': 'IVZ', 'Invitation Homes': 'INVH', 'IQVIA': 'IQV', 'Iron Mountain': 'IRM', 'J.B. Hunt': 'JBHT', 'Jabil': 'JBL', 'Jack Henry & Associates': 'JKHY', 'Jacobs Solutions': 'J',
              'Johnson & Johnson': 'JNJ', 'Johnson Controls': 'JCI', 'JPMorgan Chase': 'JPM', 'Juniper Networks': 'JNPR', 'Kellanova': 'K', 'Kenvue': 'KVUE', 'Keurig Dr Pepper': 'KDP',
              'KeyCorp': 'KEY', 'Keysight': 'KEYS', 'Kimberly-Clark': 'KMB', 'Kimco Realty': 'KIM', 'Kinder Morgan': 'KMI', 'KLA Corporation': 'KLAC', 'Kraft Heinz': 'KHC', 'Kroger': 'KR',
              'L3Harris': 'LHX'}
nasdaq_dict = {'Adobe Inc.': 'ADBE', 'ADP': 'ADP', 'Airbnb': 'ABNB', 'GOOGLE': 'GOOGL', 'GOOGLE': 'GOOG', 'Amazon': 'AMZN',
    'Advanced Micro Devices Inc.': 'AMD', 'American Electric Power': 'AEP', 'Amgen': 'AMGN', 'Analog Devices': 'ADI', 'Ansys': 'ANSS', 'Apple Inc.': 'AAPL',
    'Applied Materials': 'AMAT', 'ASML Holding': 'ASML', 'AstraZeneca': 'AZN', 'Atlassian': 'TEAM', 'Autodesk': 'ADSK', 'Baker Hughes': 'BKR',
    'Biogen': 'BIIB', 'Booking Holdings': 'BKNG', 'Broadcom Inc.': 'AVGO', 'Cadence Design Systems': 'CDNS', 'CDW Corporation': 'CDW',
    'Charter Communications': 'CHTR', 'Cintas': 'CTAS', 'Cisco': 'CSCO', 'Coca-Cola Europacific Partners': 'CCEP', 'Cognizant': 'CTSH', 'Comcast': 'CMCSA',
    'Constellation Energy': 'CEG', 'Copart': 'CPRT', 'CoStar Group': 'CSGP', 'Costco': 'COST', 'CrowdStrike': 'CRWD', 'CSX Corporation': 'CSX',
    'Datadog': 'DDOG', 'DexCom': 'DXCM', 'Diamondback Energy': 'FANG', 'Dollar Tree': 'DLTR', 'DoorDash': 'DASH', 'Electronic Arts': 'EA',
    'Exelon': 'EXC', 'Fastenal': 'FAST', 'Fortinet': 'FTNT', 'GE HealthCare': 'GEHC', 'Gilead Sciences': 'GILD', 'GlobalFoundries': 'GFS',
    'Honeywell': 'HON', 'Idexx Laboratories': 'IDXX', 'Illumina, Inc.': 'ILMN', 'Intel': 'INTC', 'Intuit': 'INTU', 'Intuitive Surgical': 'ISRG',
    'Keurig Dr Pepper': 'KDP', 'KLA Corporation': 'KLAC', 'Kraft Heinz': 'KHC', 'Lam Research': 'LRCX', 'Lululemon': 'LULU', 'Marriott International': 'MAR',
    'Marvell Technology': 'MRVL', 'MercadoLibre': 'MELI', 'Meta Platforms': 'META', 'Microchip Technology': 'MCHP', 'Micron Technology': 'MU', 'Microsoft': 'MSFT',
    'Moderna': 'MRNA', 'Mondelēz International': 'MDLZ', 'MongoDB Inc.': 'MDB', 'Monster Beverage': 'MNST', 'Netflix': 'NFLX', 'Nvidia': 'NVDA', 'NXP': 'NXPI',
    'O\'Reilly Automotive': 'ORLY', 'Old Dominion Freight Line': 'ODFL', 'Onsemi': 'ON', 'Paccar': 'PCAR', 'Palo Alto Networks': 'PANW', 'Paychex': 'PAYX',
    'PayPal': 'PYPL', 'PDD Holdings': 'PDD', 'PepsiCo': 'PEP', 'Qualcomm': 'QCOM', 'Regeneron': 'REGN', 'Roper Technologies': 'ROP', 'Ross Stores': 'ROST',
    'Sirius XM': 'SIRI', 'Splunk': 'SPLK', 'Starbucks': 'SBUX', 'Synopsys': 'SNPS', 'Take-Two Interactive': 'TTWO', 'T-Mobile US': 'TMUS', 'Tesla, Inc.': 'TSLA',
    'Texas Instruments': 'TXN', 'The Trade Desk': 'TTD', 'Verisk': 'VRSK', 'Vertex Pharmaceuticals': 'VRTX', 'Walgreens Boots Alliance': 'WBA',
    'Warner Bros. Discovery': 'WBD', 'Workday, Inc.': 'WDAY', 'Xcel Energy': 'XEL', 'Zscaler': 'ZS',
}
commodities_dict = {"Brent Crude Oil": "BZ=F", "Cocoa": "CC=F", "Coffee": "KC=F", "Copper": "HG=F", 
    "Corn Futures": "ZC=F", "Cotton": "CT=F", "Heating Oil": "HO=F", "KC HRW Wheat Futures": "KE=F", 
    "Lean Hogs Futures": "HE=F", "Live Cattle Futures": "LE=F", "Mont Belvieu LDH Propane (OPIS)": "B0=F", 
    "Natural Gas": "NG=F", "Orange Juice": "OJ=F", "OURO": "GC=F", "Oat Futures": "ZO=F", 
    "Palladium": "PA=F", "PETROLEO CRU": "CL=F", "Platinum": "PL=F", "RBOB Gasoline": "RB=F", 
    "Random Length Lumber Futures": "LBS=F", "Rough Rice Futures": "ZR=F", "Silver": "SI=F", 
    "Soybean Futures": "ZS=F", "Soybean Oil Futures": "ZL=F", "S&P Composite 1500 ESG Tilted I": "ZM=F", 
    "Sugar #11": "SB=F", "WisdomTree International High D": "GF=F"
}


assets_list = {'CURRENCIES': currencies_dict, 
               'CRYPTO': crypto_dict, 
               'B3_STOCKS': b3_stocks, 
               'SP500': sp500_dict, 
               'NASDAQ100': nasdaq_dict,
               'indexes': indexes_dict}

category = st.selectbox("Select Asset Category", list(assets_list.keys()))

selected_asset = st.selectbox("Select Asset", list(assets_list[category].keys()))

asset_symbol = assets_list[category][selected_asset]


def monte_carlo_simulation(stock_data, num_simulations, num_days):
    # Calculate daily returns
    daily_returns = stock_data['Close'].pct_change().dropna()

    # Calculate drift (mean daily return) and volatility (std deviation of daily returns)
    drift = daily_returns.mean()
    volatility = daily_returns.std()
    last_price = stock_data['Close'].iloc[-1]

    # Initialize an array to store the simulations
    simulations = np.zeros((num_days, num_simulations))

    # Simulate each price path
    for i in range(num_simulations):
        prices = [last_price]
        for d in range(1, num_days):
            # Simulate the next price based on drift and volatility (random walk)
            shock = np.random.normal(drift, volatility)
            next_price = prices[-1] * (1 + shock)
            prices.append(next_price)
        simulations[:, i] = prices

    return simulations

# Streamlit setup
st.title("Monte Carlo Simulation for Stock Price Forecasting")
# Input parameters
num_simulations = st.number_input("Number of Simulations", min_value=100, max_value=10000, value=1000)
num_days = st.number_input("Number of Days to Forecast", min_value=1, max_value=365, value=30)

# Fetch historical stock data
stock = yf.Ticker(asset_symbol)
hist = stock.history(period="1y")
# Perform Monte Carlo simulation
simulated_paths = monte_carlo_simulation(hist, num_simulations, num_days)

mean_prices = np.mean(simulated_paths, axis=1)

# Create a proper index for the future dates starting from the last known date in history
future_dates = pd.date_range(hist.index[-1], periods=num_days+1, freq='D')

# Plotting the simulation results with improved granularity and proper date indexing
plt.figure(figsize=(10, 6))
plt.plot(hist.index[-200:], hist['Close'][-200:], label='Historical Price', color='blue')

# Plot the simulated price paths
for i in range(100):  # Plot only 100 simulations for clarity
    plt.plot(future_dates, np.concatenate([[hist['Close'].iloc[-1]], simulated_paths[:, i]]), color='gray', alpha=0.1)

# Graficar la media de las simulaciones
plt.plot(future_dates, np.concatenate([[hist['Close'].iloc[-1]], mean_prices]), color='red', label='Mean Price', linewidth=2)

plt.title(f'{asset_symbol} - Monte Carlo Simulation ({num_simulations} Simulations, {num_days} Days)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(True)
plt.legend(['Historical Price'])

# Ensure the graph has proper spacing and granularity
plt.tight_layout()
st.pyplot(plt)

# Calculate and display the final average forecasted price
final_prices = simulated_paths[-1, :]
average_forecasted_price = np.mean(final_prices)
st.write(f"Average Forecasted Price after {num_days} days: ${average_forecasted_price:.2f}")

# Calculate Value at Risk (VaR) at 95% and 99% confidence levels
var_95 = np.percentile(final_prices, 5)  # VaR at 95% confidence level (5% worst-case scenario)
var_99 = np.percentile(final_prices, 1)  # VaR at 99% confidence level (1% worst-case scenario)

# Display simulated final prices as a histogram
plt.figure(figsize=(10, 6))
plt.hist(final_prices, bins=50, color='blue', edgecolor='black')
plt.axvline(var_95, color='red', linestyle='--', label=f'VaR (95%): {var_95:.0f}')
plt.axvline(var_99, color='orange', linestyle='--', label=f'VaR (95%): {var_99:.0f}')
plt.title(f'{asset_symbol} - Distribution of Final Prices ({num_simulations} Simulations)')
plt.xlabel('Price')
plt.legend()
plt.ylabel('Frequency')

# Ensure the distribution graph is properly displayed
plt.tight_layout()
st.pyplot(plt)

# Calculate the potential loss as the difference between the last historical price and VaR
last_historical_price = hist['Close'].iloc[-1]
potential_loss_95 = last_historical_price - var_95
potential_loss_99 = last_historical_price - var_99

# Display VaR results
st.write(f"VaR (95% Confidence) after {num_days} days: ${var_95:.2f}")
st.write(f"Potential Loss at 95% Confidence: ${potential_loss_95:.2f}")

st.write(f"VaR (99% Confidence) after {num_days} days: ${var_99:.2f}")
st.write(f"Potential Loss at 99% Confidence: ${potential_loss_99:.2f}")

