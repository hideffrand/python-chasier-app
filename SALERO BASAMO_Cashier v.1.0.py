import subprocess
import platform
import tkinter as tk
from tkinter import ttk
import random


def create_receipt(items):
    receipt = """
    
           Rumah Makan
          SALERO BASAMO
         Masakan  Padang 
            Prasmanan
________________________________
Tanggal: {}

Menu             Jml     price
--------------------------------
{}

Total:\t\t Rp.{}
________________________________

          Terima kasih.
  Jangan lupa datang kembali :)
________________________________
   
       Regency One Ruko.10
         0895 0402 7351

""".format(get_current_date(), format_items(items), calculate_total(items))

    return receipt


def get_current_date():
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_items(items):
    formatted_items = ""
    for item in items:
        formatted_items += "{}\t  {}   Rp.{}\n".format(
            item['name'], item['quantity'], item['price'])

    return formatted_items


def calculate_total(items):
    total = 0
    for item in items:
        total += (item['quantity'] * item['price'])

    return total


def open_file(file_path):
    if platform.system() == "Windows":
        subprocess.call(["start", file_path], shell=True)
    elif platform.system() == "Darwin":
        subprocess.call(["open", file_path])
    elif platform.system() == "Linux":
        subprocess.call(["xdg-open", file_path])
    else:
        print("Unsupported operating system.")


def main():
    menu = [
        "Nasi Rendang Daging",
        "Nasi Kikil",
        "Nasi Gulai Ikan",
        "Nasi Ayam Grg Laos",
        "Nasi Ayam Bakar",
        "Nasi Ikan Tuna Goreng",
        "Nasi Ikan Bakar",
        "Nasi Ikan Tuna Sambal",
        "Nasi Telor Dadar",
        "Nasi Telor Bulat",
        "Nasi Perkedel + Sayur",
        "Nasi Gulai Cincang",
        "Nasi Udang Goreng",
        "",
        "Rendang Daging",
        "Kikil",
        "Gulai Ikan",
        "Ayam Grg Laos",
        "Ayam Bakar",
        "Ikan Tuna Goreng",
        "Ikan Bakar",
        "Ikan Tuna Sambal",
        "Telor Dadar",
        "Telor Bulat",
        "Perkedel + Sayur",
        "Gulai Cincang",
        "Udang Goreng",
        "Kerupuk",
        "Tahu",
        "",
        "Es Jeruk",
        "Es Teh",
        "Teh Hangat",
        "Jeruk Hangat",
        "Es Good Day / Cofee Mix",
        "Soda Gembira",
        "Es Extra Jos",
        "Kopi Panas",
        "Kopi Susu",
        "",
        "Kotak"
    ]

    reduced_menu_name = {
        "Nasi Rendang Daging": "Ns Rendang    ",
        "Nasi Kikil": "Ns Kikil      ",
        "Nasi Gulai Ikan": "Ns Gulai Ikan ",
        "Nasi Ayam Grg Laos": "Ns Ayam Laos  ",
        "Nasi Ayam Bakar": "Ns Ayam Bakar ",
        "Nasi Ikan Tuna Goreng": "Nasi Tuna Grg ",
        "Nasi Ikan Bakar": "Ns Ikan Bakar ",
        "Nasi Ikan Tuna Sambal": "Ns Tuna Sambl",
        "Nasi Telor Dadar": "Ns Telur Dadar",
        "Nasi Telor Bulat": "Ns Telur Bulat",
        "Nasi Perkedel + Sayur": "Ns Perkedel   ",
        "Nasi Gulai Cincang": "Nasi Gulai Ccg",
        "Nasi Udang Goreng": "Nasi Udang    ",
        "Rendang Daging": "Rendang Daging",
        "Kikil": "Kikil         ",
        "Gulai Ikan": "Gulai Ikan    ",
        "Ayam Grg Laos": "Ayam Grg Laos ",
        "Ayam Bakar": "Ayam Bakar   ",
        "Ikan Tuna Goreng": "Ikan Tuna Grg ",
        "Ikan Bakar": "Ikan Bakar    ",
        "Ikan Tuna Sambal": "Ikan Tuna Smbl",
        "Telor Dadar": "Telor Dadar   ",
        "Telor Bulat": "Telor Bulat   ",
        "Perkedel + Sayur": "Perkdl + Sayur",
        "Gulai Cincang": "Gulai Cincang ",
        "Udang Goreng": "Udang Goreng  ",
        "Kerupuk": "Kerupuk       ",
        "Tahu": "Tahu          ",
        "Es Jeruk": "Es Jeruk      ",
        "Es Teh": "Es Teh        ",
        "Teh Hangat": "Teh Hangat    ",
        "Jeruk Hangat": "Jeruk Hangat  ",
        "Es Good Day / Cofee Mix": "Es Good day   ",
        "Soda Gembira": "Es Soda Gmbira",
        "Es Extra Jos": "Es Extra Jos  ",
        "Kopi Panas": "Kopi Panas    ",
        "Kopi Susu": "Kopi Susu     ",
        "Kotak": "Kotak         "
    }

    price = {
        "Nasi Rendang Daging": 15_000,
        "Nasi Kikil": 15_000,
        "Nasi Gulai Ikan": 17_000,
        "Nasi Ayam Grg Laos": 13_000,
        "Nasi Ayam Bakar": 13_000,
        "Nasi Ikan Tuna Goreng": 15_000,
        "Nasi Ikan Bakar": 16_000,
        "Nasi Ikan Tuna Sambal": 15_000,
        "Nasi Telor Dadar": 12_000,
        "Nasi Telor Bulat": 10_000,
        "Nasi Perkedel + Sayur": 10_000,
        "Nasi Gulai Cincang": 17_000,
        "Nasi Udang Goreng": 17_000,
        "Rendang Daging": 10_000,
        "Kikil": 10_000,
        "Gulai Ikan": 13_000,
        "Ayam Grg Laos": 8_000,
        "Ayam Bakar": 8_000,
        "Ikan Tuna Goreng": 10_000,
        "Ikan Bakar": 10_000,
        "Ikan Tuna Sambal": 10_000,
        "Telor Dadar": 7_000,
        "Telor Bulat": 5_000,
        "Perkedel + Sayur": 5_000,
        "Gulai Cincang": 12_000,
        "Udang Goreng": 12_000,
        "Kerupuk": 1_000,
        "Tahu": 2_000,
        "Es Jeruk": 4_000,
        "Jeruk Hangat": 4_000,
        "Es Teh": 3_000,
        "Teh Hangat": 3_000,
        "Es Good Day / Cofee Mix": 4_000,
        "Soda Gembira": 0,
        "Es Extra Jos": 0,
        "Kopi Panas": 3_000,
        "Kopi Susu": 3_000,
        "Kotak": 1_000
    }

    window = tk.Tk()
    window.geometry("300x600")
    window.title('SALERO BASAMO_Cashier v.1.0')
    window.attributes('-fullscreen', True)
    window.config(pady=150)

    header_frame = ttk.Frame(window)
    header_frame.pack(pady=50, fill='x')
    ttk.Label(header_frame, text='____________________________________',
              font="BOLD").pack(padx=10, pady=1)
    ttk.Label(header_frame, text='                                    ',
              font="BOLD").pack(padx=10, pady=1)
    ttk.Label(header_frame, text='RURMAH MAKAN',
              font="BOLD").pack(padx=10, pady=1)
    ttk.Label(header_frame, text='SALERO BASAMO',
              font="BOLD").pack(padx=10, pady=1)
    ttk.Label(header_frame, text='MASAKAN PADANG PRASMANAN',
              font="BOLD").pack(padx=10, pady=1)
    ttk.Label(header_frame, text='____________________________________',
              font="BOLD").pack(padx=10, pady=1)

    input_frame = ttk.Frame(window)
    input_frame.pack()

    quantity = tk.StringVar()
    options = tk.StringVar()
    options.set('Nasi')
    order_list = []
    grand_total = []

    def insert_order_to_order_list():
        menu_name = options.get()
        menu_name_simplified = reduced_menu_name[menu_name]
        quantity_value = int(quantity.get())
        price_value = int(price[menu_name])
        order_dictionary = {
            'name': menu_name_simplified,
            'quantity': quantity_value,
            'price': price_value
        }
        order_list.append(order_dictionary)
        stat = random.randint(0, 10000000000)
        stat = str(stat)
        label_status.config(text=stat)

    def process_create_receipt():
        get_total = calculate_total(order_list)
        grand_total.append(get_total)
        print(grand_total)
        receipt = create_receipt(order_list)
        file_path = 'receipt.txt'
        with open(file_path, 'w') as file:
            file.write(receipt)
        open_file(file_path)
        order_list.clear()
        label_status.config(text='------Done-----')

    label_menu_name = ttk.Label(input_frame, text='Menu', font="BOLD")
    label_menu_name.grid(row=0, column=0)

    label_quantity = ttk.Label(input_frame, text='quantity', font="BOLD")
    label_quantity.grid(row=0, column=1)

    input_menu_name = tk.OptionMenu(input_frame, options, *menu)
    input_menu_name.grid(row=1, column=0, pady=20)
    input_menu_name.config(width=20, bg='WHITE', font="BOLD")

    input_quantity = tk.Entry(
        input_frame, textvariable=quantity, font="BOLD", width=20)
    input_quantity.grid(row=1, column=1)
    input_quantity.insert(1, "1")

    label_status = ttk.Label(window, text='status', font="BOLD")
    label_status.pack(pady=100)

    button_input = tk.Button(input_frame, text='Input', command=insert_order_to_order_list,
                             height=2, width=20, bg='YELLOW', font="BOLD")
    button_input.grid(row=2, column=0)

    button_create_receipt = tk.Button(
        input_frame, text='Cetak Struk', command=process_create_receipt, height=2, width=20, bg='LIGHTGREEN', font="BOLD")
    button_create_receipt.grid(row=2, column=1)

    window.mainloop()


if __name__ == "__main__":
    main()
