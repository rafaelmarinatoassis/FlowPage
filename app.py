import tkinter as tk
import threading
import time
import keyboard

class ChromeTabSwitcherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("🔁 Troca Automática de Abas - Chrome")
        self.master.geometry("400x450")
        self.master.resizable(False, False)
        self.master.configure(bg="#f0f4f7")

        self.entries = []
        self.running = False

        self.font = ("Segoe UI", 10)

        # Seção de configuração
        self.config_frame = tk.Frame(master, bg="#f0f4f7")
        self.config_frame.pack(pady=10)

        tk.Label(self.config_frame, text="Quantidade de abas (máx 10):", font=self.font, bg="#f0f4f7").pack(side=tk.LEFT)
        self.tab_count_entry = tk.Entry(self.config_frame, width=5, font=self.font)
        self.tab_count_entry.insert(0, "3")
        self.tab_count_entry.pack(side=tk.LEFT, padx=5)
        self.set_button = tk.Button(self.config_frame, text="Configurar", font=self.font, command=self.create_entries)
        self.set_button.pack(side=tk.LEFT, padx=5)

        # Mensagem de aviso
        self.message_label = tk.Label(master, text="", font=("Segoe UI", 9), fg="red", bg="#f0f4f7")
        self.message_label.pack()

        # Área de entradas
        self.entries_frame = tk.Frame(master, bg="#f0f4f7")
        self.entries_frame.pack(pady=5)

        # Controles
        self.control_frame = tk.Frame(master, bg="#f0f4f7")
        self.control_frame.pack(pady=20)

        self.start_button = tk.Button(self.control_frame, text="▶ Iniciar", font=self.font, width=10, bg="#d0f0c0", command=self.start_switching)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.control_frame, text="⏹ Parar", font=self.font, width=10, bg="#f9c0c0", command=self.stop_switching)
        self.stop_button.pack(side=tk.LEFT, padx=10)

    def show_message(self, msg):
        self.message_label.config(text=msg)
        self.master.after(3000, lambda: self.message_label.config(text=""))  # limpa após 3 segundos

    def create_entries(self):
        for widget in self.entries_frame.winfo_children():
            widget.destroy()
        self.entries.clear()

        try:
            count = int(self.tab_count_entry.get())
            if count > 10:
                count = 10
                self.tab_count_entry.delete(0, tk.END)
                self.tab_count_entry.insert(0, "10")
                self.show_message("Máximo permitido é 10 abas!")

            for i in range(count):
                row = tk.Frame(self.entries_frame, bg="#f0f4f7")
                row.pack(pady=2)

                tk.Label(row, text=f"Aba {i+1}:", font=self.font, width=10, anchor="w", bg="#f0f4f7").pack(side=tk.LEFT)

                tab_entry = tk.Entry(row, width=5, font=self.font)
                tab_entry.insert(0, str(i + 1))
                tab_entry.pack(side=tk.LEFT, padx=5)

                tk.Label(row, text="Tempo (s):", font=self.font, bg="#f0f4f7").pack(side=tk.LEFT)

                time_entry = tk.Entry(row, width=5, font=self.font)
                time_entry.insert(0, "10")
                time_entry.pack(side=tk.LEFT, padx=5)

                self.entries.append((tab_entry, time_entry))
        except ValueError:
            self.show_message("Digite um número válido!")

    def start_switching(self):
        if not self.running and self.entries:
            self.running = True
            threading.Thread(target=self.switch_tabs, daemon=True).start()

    def stop_switching(self):
        self.running = False

    def switch_tabs(self):
        while self.running:
            for tab_entry, delay_entry in self.entries:
                if not self.running:
                    break
                try:
                    tab = int(tab_entry.get())
                    delay = float(delay_entry.get())
                    if 1 <= tab <= 9:
                        keyboard.press_and_release(f'ctrl+{tab}')
                        time.sleep(delay)
                except ValueError:
                    continue

if __name__ == "__main__":
    root = tk.Tk()
    app = ChromeTabSwitcherApp(root)
    root.mainloop()
