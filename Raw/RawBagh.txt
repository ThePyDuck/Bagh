import re
import sys
import os
import struct
import tkinter as tk
from tkinter import scrolledtext, filedialog, Menu, messagebox
import subprocess
import shutil
import random
import string
import datetime
import hashlib

class BaghCompiler:
    def __init__(self):
        self.bagh_keywords = {
            "lekho": "PRINT",
            "kaj": "FUNC",
            "ghoomta": "LOOP",
            "jodi": "IF",
            "jodi na": "ELSE",
            "nahole": "ELIF",
            "random_word": "RANDWORD",
            "grohon": "INPUT",
            "gonona": "MATH",
            "lekho_file": "WRITEFILE",
            "poro_file": "READFILE",
            "tarikh": "DATE",
            "somoy": "TIME",
            "encrypt": "ENCRYPT",
            "decrypt": "DECRYPT"
        }
        self.variables = {}
        self.functions = {}

    def compile_to_bytecode(self, bagh_code):
        bytecode = []
        lines = bagh_code.strip().split("\n")
        for line in lines:
            line = line.strip()
            if not line:
                continue

            if "(" in line and ")" in line:
                command = line.split("(")[0].strip()
                args = line.split("(")[1].rstrip(")").strip()
                if command in self.bagh_keywords:
                    bytecode.append(f"{self.bagh_keywords[command]} {args}")
                else:
                    print(f"Error: Unknown command '{command}'")
                continue

            words = line.split()
            command = words[0]
            if command in self.bagh_keywords:
                bytecode.append(f"{self.bagh_keywords[command]} {' '.join(words[1:])}")
            else:
                if len(words) < 2:
                    print(f"Error: Invalid variable assignment in line: {line}")
                else:
                    self.variables[words[0]] = " ".join(words[1:])
                    bytecode.append(f"VAR {' '.join(words)}")
        return bytecode

    def save_bytecode(self, bytecode, filename):
        with open(filename, "wb") as f:
            for instruction in bytecode:
                f.write(instruction.encode("utf-8") + b'\n')

class BaghVM:
    def execute_bytecode(self, filename, output_box):
        try:
            with open(filename, "rb") as f:
                bytecode = f.readlines()
            for instruction in bytecode:
                tokens = instruction.decode("utf-8").strip().split(" ", 1)
                if not tokens:
                    continue
                opcode = tokens[0]
                args = tokens[1:] if len(tokens) > 1 else []
                result = self.run_instruction(opcode, args)
                if result:
                    output_box.insert(tk.END, result + "\n")
                    output_box.see(tk.END)
                    print(result)  # Also print to console
        except FileNotFoundError:
            output_box.insert(tk.END, f"Error: File '{filename}' not found.\n")
        except Exception as e:
            output_box.insert(tk.END, f"Execution Error: {e}\n")

    def run_instruction(self, opcode, args):
        try:
            if opcode == "PRINT":
                return " ".join(args).strip("\"")
            elif opcode == "RANDWORD":
                return ''.join(random.choices(string.ascii_lowercase, k=int(args[0])))
            elif opcode == "INPUT":
                return input("Enter value: ")
            elif opcode == "MATH":
                return str(eval(" ".join(args)))
            elif opcode == "WRITEFILE":
                with open(args[0], "w") as f:
                    f.write(args[1])
                return f"Written to {args[0]}"
            elif opcode == "READFILE":
                with open(args[0], "r") as f:
                    return f.read()
            elif opcode == "DATE":
                return str(datetime.date.today())
            elif opcode == "TIME":
                return datetime.datetime.now().strftime("%H:%M:%S")
            elif opcode == "ENCRYPT":
                return hashlib.sha256(args[0].encode()).hexdigest()
            elif opcode == "DECRYPT":
                return "Error: Decryption not supported"
            else:
                return f"Unknown instruction: {opcode}"
        except Exception as e:
            return f"Runtime Error: {e}"

class BaghIDE:
    def __init__(self):
        self.editor = tk.Tk()
        self.editor.title("Bagh IDE")
        self.editor.geometry("900x600")

        menu_bar = Menu(self.editor)
        self.editor.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Exit", command=self.editor.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_help)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        
        menu_bar.add_command(label="Run", command=self.run_code)

        self.text_area = scrolledtext.ScrolledText(self.editor, wrap=tk.WORD, font=("Consolas", 12))
        self.text_area.pack(expand=True, fill='both')
        self.text_area.bind("<KeyRelease>", self.highlight_syntax)

        self.output_box = scrolledtext.ScrolledText(self.editor, wrap=tk.WORD, height=10, font=("Consolas", 12))
        self.output_box.pack(fill='x')

    def show_help(self):
        messagebox.showinfo("About Bagh IDE", "Bagh IDE - A simple IDE for the Bagh programming language.")

    def highlight_syntax(self, event=None):
        self.text_area.tag_remove("keyword", "1.0", tk.END)
        self.text_area.tag_remove("string", "1.0", tk.END)
        code = self.text_area.get("1.0", tk.END)
        keywords = {"lekho": "blue", "print": "cyan"}
        for kw, color in keywords.items():
            start_idx = "1.0"
            while True:
                start_idx = self.text_area.search(kw, start_idx, tk.END)
                if not start_idx:
                    break
                end_idx = f"{start_idx} + {len(kw)}c"
                self.text_area.tag_add(kw, start_idx, end_idx)
                self.text_area.tag_config(kw, foreground=color)
                start_idx = end_idx

    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.text_area.get("1.0", tk.END))
    
    def run_code(self):
        code = self.text_area.get("1.0", tk.END)
        compiler = BaghCompiler()
        bytecode = compiler.compile_to_bytecode(code)
        compiler.save_bytecode(bytecode, "temp.bagh")
        vm = BaghVM()
        vm.execute_bytecode("temp.bagh", self.output_box)
    
    def open(self):
        self.editor.mainloop()

if __name__ == "__main__":
    BaghIDE().open()
