# CliNika

**CliNika** is a smart automation script for a vet clinic.  
It cross-checks daily financial reports (in Excel format), detects errors, calculates salaries based on custom formula, and tracks inventory changes — all in one tool.

## 🔧 Features

- ✅ Cross-verification between daily and monthly reports
- ✅ Error detection in employee entries (services, amounts, duplicates, etc.)
- ✅ Automatic salary calculation per employee
- ✅ Daily inventory tracking and updates
- ✅ Export of results into `.txt` and `.xlsx` formats

## 📂 Input Format

The script expects:

- Daily reports:
    -WIP

- Monthly master report:  
  -WIP

- Inventory data:  
  -WIP

## 📤 Output

- A comparison report with:
  - Mismatches, missing entries, suspicious data
  - Salary breakdown for each employee
  - Updated inventory levels

- Example output: WIP

## 📦 Used Libraries

- `pandas` — data manipulation and Excel reading
- `openpyxl` — Excel writing
- `datetime` — date filtering
- `re` — data parsing/validation via regular expressions
- `pathlib` / `os` — file management

## 💡 Why It Matters

This project demonstrates real-world skills in:

- Automating Excel workflows
- Parsing, verifying and transforming structured data
- Building maintainable, modular Python scripts
- Designing tools for small business automation

## 🔧 Setup

```bash
pip install WIP