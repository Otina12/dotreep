# dotreep

The Windows file system is slow at analyzing directory sizes, so I created **dotreep**.  
`dotreep` is a Python command-line tool that prints a directory tree with file sizes, sorted by descending size.  
The solution uses a simple **Composite Design Pattern**.

---

## ✨ Features
- Recursively scans all directories.
- Prints a tree structure with aligned sizes.
- Sorts files and folders by descending size.

---

## ⚙️ Installation

```bash
git clone https://github.com/Otina12/dotreep.git
cd dotreep
pip install -e .
```

---

## 🖥️ Usage

### Show tree for the current directory
```bash
dotreep
```

### Analyze a specific folder
```bash
dotreep D:\MyProjects
```

### Display help
```bash
dotreep --help
```

---

## 📂 Example Output

```
└── Projects | Size: 170 bytes
    ├── Reports | Size: 120 bytes
    |   ├── main.py | Size: 92 bytes
    |   └── data.csv | Size: 28 bytes
    └── archive.zip | Size: 50 bytes
```

---

## ✅ Requirements
- Python 3.7 or newer

---

## 📄 License
MIT License
