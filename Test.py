from BOT import main
from Final_DB import final_df, get_page2
from Get_Last import get_dernier, lastlast
from Send_Mail import main2
from Get_Link import main
import time

import pandas as pd
Time = 6000

def Bottt():
    last_seen_title = None

    while True:
        main()
        final_df()
        lastlast()
        main2()

        time.sleep(Time)


if __name__ == "__main__":
    print("main")
    Bottt()
