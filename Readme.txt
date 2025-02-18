# **Bagh Programming Language**  
### **Pre-Alpha v0.1**  

**Bagh** is a unique programming language that stands out because it uses **Bengali words for commands and syntax** instead of English. This makes programming more accessible for Bengali speakers, allowing them to write code in their native language while still maintaining the power of a structured programming language.  

This project is currently in **pre-alpha development**, meaning new features are still being added, and improvements are ongoing.  

---

## **Why Use Bagh?**  
✅ **First Bengali-Based Programming Language**  
✅ **Simple & Easy-to-Learn Syntax**  
✅ **Custom Interpreter & Compiler**  
✅ **Supports File Operations & Encryption**  
✅ **Includes Built-in Math & Random Functions**  
✅ **Designed for Script Execution & Automation**  
✅ **Lightweight & Open-Source**  

---

## **Bagh Uses Bengali Words Instead of English!**  

Unlike most programming languages that use English keywords (`print`, `if`, `for`, `while`, etc.), **Bagh replaces these with Bengali words** to make coding feel more natural for Bengali speakers.  

| **English in Other Languages** | **Bengali in Bagh** | **Description** |
|------------------|----------------|----------------|
| `print("Hello")` | `lekho("Hello")` | Prints text |
| `if (x > y):` | `jodi (x > y):` | If condition |
| `else:` | `jodi na:` | Else statement |
| `while (x < 10):` | `ghoomta (x < 10):` | Loop statement |
| `input("Name: ")` | `grohon("Name: ")` | Take user input |
| `read_file("data.txt")` | `poro_file("data.txt")` | Read from a file |
| `write_file("data.txt", "text")` | `lekho_file("data.txt", "text")` | Write to a file |

This makes it **easier for Bengali speakers to understand and write code** without having to memorize English keywords!  

---

## **How Bagh Works**  

Bagh is an interpreted language. Code written in **Bagh** is **compiled to bytecode**, which is then executed by the **Bagh Virtual Machine (BaghVM)**.  

### **Basic Structure of a Bagh Program**  
- Bagh uses **Bengali words** for commands, making it beginner-friendly.  
- Statements are written in **simple syntax** similar to Python but in Bengali.  
- Commands often require parentheses `( )` to pass arguments.  

Example:  
```bagh
lekho("হ্যালো, বাঘ!")  # Prints a message
gonona(5 + 3)          # Performs a mathematical calculation
```

---

## **Bagh Commands & Their Usage**  

### **1. Printing Output**  
```bagh
lekho("হ্যালো, বিশ্ব!")
```
🟢 **Outputs**: `হ্যালো, বিশ্ব!`  
This command prints text to the output console.  

---

### **2. Variables & Assignments**  
```bagh
x = ১০
y = ২০
lekho(x + y)
```
🟢 **Outputs**: `৩০`  
- Variables can store numbers or text.  
- They can be used in expressions.  

---

### **3. User Input**  
```bagh
name = grohon("তোমার নাম কী? ")
lekho("স্বাগতম, " + name)
```
🟢 **Takes user input and prints a greeting.**  

---

### **4. Math Operations**  
```bagh
result = gonona(১০ * ৫ - ২)
lekho(result)
```
🟢 **Outputs**: `৪৮`  
- `gonona(expression)` performs calculations.  
- Supports: `+`, `-`, `*`, `/`, `%`, `**` (exponentiation).  

---

### **5. Conditional Statements**  
```bagh
x = ১০
y = ২০
jodi (x > y):
    lekho("X বড়")
jodi na:
    lekho("Y বড়")
```
🟢 **Outputs**: `Y বড়`  
- `jodi(condition):` works like `if`.  
- `jodi na:` is the equivalent of `else`.  

---

### **6. Loops (Repetition)**  
```bagh
ghoomta (i = ০; i < ৫; i = i + ১):
    lekho("চলছে: " + i)
```
🟢 **Outputs**:  
```
চলছে: ০
চলছে: ১
চলছে: ২
চলছে: ৩
চলছে: ৪
```
- `ghoomta` is a loop that runs while a condition is true.  

---

### **7. Random Word Generator**  
```bagh
word = random_word(৫)
lekho("তৈরি শব্দ: " + word)
```
🟢 **Outputs**: `abcde` *(Random ৫-letter word)*  

---

### **8. File Handling**  
#### **Write to a File**  
```bagh
lekho_file("data.txt", "এটি কিছু লেখা।")
```
🟢 Creates a file **data.txt** and writes text inside it.  

#### **Read from a File**  
```bagh
content = poro_file("data.txt")
lekho(content)
```
🟢 Reads and prints the file’s content.  

---

### **9. Date & Time Functions**  
#### **Current Date**  
```bagh
today = tarikh()
lekho("আজকের তারিখ: " + today)
```
🟢 **Outputs**: `আজকের তারিখ: ২০২৫-০২-১৮`  

#### **Current Time**  
```bagh
now = somoy()
lekho("বর্তমান সময়: " + now)
```
🟢 **Outputs**: `বর্তমান সময়: ১৪:৪৫:৩০`  

---

### **10. Encryption & Hashing**  
#### **Encrypt Text (SHA-256 Hashing)**  
```bagh
hash_value = encrypt("হ্যালো")
lekho("হ্যাশড আউটপুট: " + hash_value)
```
🟢 **Outputs**: A long hashed string of `হ্যালো`.  

---

## **How to Run Bagh Code**  

### **Using Bagh IDE**  
1. Open **Bagh IDE**.  
2. Write Bagh code in the editor.  
3. Click **Run** to execute the script.  
4. View output in the console.  

### **Using Bagh Compiler & VM**  
1. Save your code as **script.bagh**.  
2. Run the compiler:  
   ```sh
   python BaghCompiler.py script.bagh
   ```
3. Execute with the **Bagh Virtual Machine (VM)**:  
   ```sh
   python BaghVM.py script.bagh
   ```

---

## **Planned Features for Future Updates**  
🔹 Functions & User-Defined Methods  
🔹 More File Handling Features  
🔹 Debugging & Error Reporting Improvements  
🔹 Advanced Encryption & Decryption  
🔹 GUI-Based Bagh Script Runner  

---

License  
Bagh is released under an **open-source license**:  
✅ **Free to Use & Modify**  
✅ **Credit to the Original Author is Required**  
✅ **Can be used for any purpose (including commercial)**  


Contributing  
We welcome contributions!  
1. Fork this repository  
2. Create a new branch  
3. Make changes & submit a pull request  

---

Contact & Support  
📧 Email: `fuqbucdoom@gmail.com` 

If you find any issues or have feature requests, feel free to **open an issue** in this repository!  

---

Now this README fully highlights **Bagh’s use of Bengali words**, making it stand out from other programming languages! 🚀🔥 Let me know if you need more refinements!
