import re
import tkinter as tk
from tkinter import scrolledtext, filedialog, Menu, simpledialog
import datetime
import hashlib
import random

class BaghCompiler:
    def __init__(self):
        self.variables = {}

    def compile_to_bytecode(self, bagh_code):
        bytecode = []
        lines = bagh_code.strip().split("\n")

        for line in lines:
            line = line.strip()
            if not line:
                continue

            match = re.match(r'(\w+)\s*(.*)?', line)
            if match:
                command = match.group(1)
                args = match.group(2).strip() if match.group(2) else ""

                if "=" in line:
                    var_name, value = map(str.strip, line.split("=", 1))
                    bytecode.append(f"SET_VAR {var_name} {value}")
                elif command == "lekho":
                    bytecode.append(f"PRINT {args}")
                elif command == "kaj":
                    bytecode.append(f"FUNC_START {args}")
                elif command == "shesh":
                    bytecode.append("FUNC_END")
                elif command == "ghoomta":
                    if not args.isdigit():
                        return ["ERROR Loop count must be a number"]
                    bytecode.append(f"LOOP_START {args}")
                elif command == "jodi":
                    bytecode.append(f"IF {args}")
                elif command == "nahole":
                    bytecode.append("ELIF")
                elif command == "jodi na":
                    bytecode.append("ELSE")
                elif command == "tarikh":
                    bytecode.append("DATE")
                elif command == "somoy":
                    bytecode.append("TIME")
                elif command == "encrypt":
                    bytecode.append(f"ENCRYPT {args}")
                elif command == "grohon":
                    bytecode.append(f"INPUT {args}")
                elif command == "random":
                    bytecode.append(f"RANDOM {args}")
                elif command == "gonona":
                    bytecode.append(f"EXPRESSION {args}")
                elif command == "poro_file":
                    bytecode.append(f"READ_FILE {args}")
                elif command == "lekho_file":
                    bytecode.append(f"WRITE_FILE {args}")
                else:
                    bytecode.append(f"ERROR Unknown command: {line}")
        
        return bytecode

class BaghVM:
    def __init__(self):
        self.variables = {}

    def execute_bytecode(self, bytecode, output_box):
        i = 0
        console_output = []

        while i < len(bytecode):
            instruction = bytecode[i]
            tokens = instruction.split(" ", 2)
            opcode = tokens[0]
            args = tokens[1:] if len(tokens) > 1 else []

            if opcode == "SET_VAR":
                var_name, value = args
                try:
                    self.variables[var_name] = eval(value, {}, self.variables)
                except:
                    self.variables[var_name] = value
            elif opcode == "PRINT":
                expression = " ".join(args)
                try:
                    console_output.append(str(eval(expression, {}, self.variables)))
                except:
                    console_output.append(expression)
            elif opcode == "LOOP_START":
                try:
                    loop_count = int(args[0])
                    loop_body = []
                    i += 1
                    while i < len(bytecode) and bytecode[i] != "FUNC_END":
                        loop_body.append(bytecode[i])
                        i += 1
                    for _ in range(loop_count):
                        self.execute_bytecode(loop_body, output_box)
                except ValueError:
                    console_output.append("⚠ Loop Error: Invalid loop count")
                    return
            elif opcode == "IF":
                condition = " ".join(args).strip()
                if eval(condition, {}, self.variables):
                    console_output.append(f"Condition met: {condition}")
            elif opcode == "DATE":
                console_output.append(str(datetime.date.today()))
            elif opcode == "TIME":
                console_output.append(datetime.datetime.now().strftime("%H:%M:%S"))
            elif opcode == "ENCRYPT":
                console_output.append(hashlib.sha256(" ".join(args).encode()).hexdigest())
            elif opcode == "INPUT":
                var_name = args[0]
                self.variables[var_name] = simpledialog.askstring("Input", f"Enter value for {var_name}:")
            elif opcode == "RANDOM":
                start, end = map(int, args)
                console_output.append(str(random.randint(start, end)))
            elif opcode == "EXPRESSION":
                expression = " ".join(args)
                try:
                    result = eval(expression, {}, self.variables)
                    console_output.append(f"Result: {result}")
                except:
                    console_output.append("⚠ Error: Invalid expression")
            elif opcode == "READ_FILE":
                filename = args[0]
                try:
                    with open(filename, "r", encoding="utf-8") as file:
                        content = file.read()
                        console_output.append(f"File content: {content}")
                        self.variables["file_content"] = content
                except Exception as e:
                    console_output.append(f"⚠ Error reading file: {e}")
            elif opcode == "WRITE_FILE":
                filename = args[0]
                content = self.variables.get("file_content", "")
                try:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(content)
                    console_output.append(f"File written: {filename}")
                except Exception as e:
                    console_output.append(f"⚠ Error writing file: {e}")
            elif opcode == "ERROR":
                console_output.append(f"⚠ {args}")
                return

            i += 1

        for line in console_output:
            print(line)

        output_box.insert(tk.END, "\n".join(console_output) + "\n")
        output_box.see(tk.END)

class BaghIDE:
    def __init__(self):
        self.editor = tk.Tk()
        self.editor.title("Bagh IDE")
        self.editor.iconbitmap("bagh.ico")
        self.editor.geometry("900x600")

        menu_bar = Menu(self.editor)
        self.editor.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Exit", command=self.editor.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        self.text_area = scrolledtext.ScrolledText(self.editor, wrap=tk.WORD, font=("Consolas", 12))
        self.text_area.pack(expand=True, fill='both')

        self.output_box = scrolledtext.ScrolledText(self.editor, wrap=tk.WORD, height=10, font=("Consolas", 12))
        self.output_box.pack(fill='x')

        menu_bar.add_command(label="Run", command=self.run_code)

    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.text_area.get("1.0", tk.END))

    def run_code(self):
        self.output_box.delete("1.0", tk.END)
        code = self.text_area.get("1.0", tk.END).strip()

        if not code:
            self.output_box.insert(tk.END, "⚠ Error: No code to run!\n")
            return

        compiler = BaghCompiler()
        bytecode = compiler.compile_to_bytecode(code)

        if not bytecode or "ERROR" in bytecode[0]:
            self.output_box.insert(tk.END, "⚠ Compilation Error: Check your code!\n")
            return

        vm = BaghVM()
        vm.execute_bytecode(bytecode, self.output_box)

    def open(self):
        self.editor.mainloop()

if __name__ == "__main__":
    BaghIDE().open()
