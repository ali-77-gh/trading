
import tkinter as tk
import MetaTrader5 as mt5
import pandas as pd

def get_data():
    symbol = entry.get()  
    if symbol:
        if not mt5.initialize():
            result_label.config(text="خطا در اتصال به MetaTrader5")
            return
    
        rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_H4, 0, 10)  
        if rates is None or len(rates) == 0:
            result_label.config(text="داده‌ای برای این نماد یافت نشد.")
            mt5.shutdown()
            return
        
        
        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'], unit='s')
        data = df[['time', 'open', 'high', 'low', 'close']]

        
        result_label.config(text=f"با موفقیت دریافت شد{symbol} داده های نماد")

       
        mt5.shutdown()
    else:
        result_label.config(text="لطفاً نماد را وارد کنید.")








window = tk.Tk()
window.geometry("800x600")
window.title("پیشبینی روند")

label = tk.Label(window , text="من ربات روندگیر هستم" , font=("Titr" , 20))
label.pack()

label = tk.Label(window , text=".نماد مورد نظر را وارد کنید")
label.pack()

entry = tk.Entry(window , width=20)
entry.pack()

button = tk.Button(text="دریافت  دیتا" , command=get_data)
button.pack()

result_label = tk.Label(window, text="", font=("Bnazanin", 12))
result_label.pack()


window.mainloop()


