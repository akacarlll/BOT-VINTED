from BOT import main
from yikes import final_df, get_page2
from Get_Last import get_dernier, lastlast
from Mail import main2
from BOT import main
import time

import pandas as pd
Time = 100000
df = pd.read_csv("C:\\Users\\carlf\\OneDrive\\Bureau\\Technique de programmation\\BOT VINTED\\vinted_data.csv")
df_last = pd.read_csv("C:\\Users\\carlf\\OneDrive\\Bureau\\Technique de programmation\\BOT VINTED\\final_data.csv")


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