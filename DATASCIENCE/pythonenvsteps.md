# 🛠️ Fix Broken Python Virtual Environment in VS Code (Windows)

If you see an error like:

```text
did not find executable at
C:\Users\Kunal\AppData\Local\Programs\Python\Python314\python.exe
```

it means your virtual environment (`.venv`) is pointing to a Python installation that no longer exists.

---

# Step 1: Delete the Old Virtual Environment

Deactivate the virtual environment (if active):

```powershell
deactivate
```

> If you get `'deactivate' is not recognized`, ignore it.

Delete the `.venv` folder:

```powershell
Remove-Item -Recurse -Force .venv
```

Or simply delete the `.venv` folder using File Explorer.

---

# Step 2: Create a New Virtual Environment

If Python 3.13 is installed:

```powershell
py -3.13 -m venv .venv
```

If that doesn't work, use:

```powershell
python -m venv .venv
```

---

# Step 3: Activate the Virtual Environment

```powershell
.\.venv\Scripts\Activate
```

You should now see:

```text
(.venv)
```

---

# Step 4: Upgrade pip

```powershell
python -m pip install --upgrade pip
```

---

# Step 5: Install Required Packages

```powershell
pip install numpy pandas matplotlib seaborn jupyter ipykernel
```

---

# Step 6: Register the Jupyter Kernel

```powershell
python -m ipykernel install --user --name=MSCIT
```

---

# Step 7: Select the Correct Kernel in VS Code

Open your Jupyter Notebook (`.ipynb`).

Click the **Python Interpreter** shown in the **top-right corner**.

Select:

```text
MSCIT (.venv)
```

If it isn't visible:

1. Click **Select Another Kernel**
2. Choose **Python Environments**
3. Select **.venv**

---

# Step 8: Verify the Python Interpreter

Run the following cell:

```python
import sys

print(sys.executable)
```

Expected output:

```text
C:\Users\Kunal\OneDrive\Desktop\MSCIT\.venv\Scripts\python.exe
```

---

# Step 9: Test the Installed Packages

Run:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Everything is working!")
```

Expected output:

```text
Everything is working!
```

---

# If You Still Get Errors

Run these commands in the terminal and copy the output:

```powershell
where python
```

```powershell
py -0p
```

```powershell
python --version
```

```powershell
py --version
```

---

# Expected Folder Structure

```text
MSCIT/
│
├── .venv/
│   ├── Scripts/
│   │   ├── python.exe
│   │   ├── Activate.ps1
│   │   └── pip.exe
│   └── ...
│
├── EDA.ipynb
└── requirements.txt
```

---

# Quick Installation Commands

Create virtual environment:

```powershell
python -m venv .venv
```

Activate:

```powershell
.\.venv\Scripts\Activate
```

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Install packages:

```powershell
pip install numpy pandas matplotlib seaborn jupyter ipykernel
```

Register Jupyter kernel:

```powershell
python -m ipykernel install --user --name=MSCIT
```

---

# 🎉 You're Done!

You can now use:

- ✅ NumPy
- ✅ Pandas
- ✅ Matplotlib
- ✅ Seaborn
- ✅ Jupyter Notebook
- ✅ VS Code Notebook Support

without any Python interpreter errors.