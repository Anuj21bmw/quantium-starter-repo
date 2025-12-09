# Quantium Starter Repo

This repository contains a Python Dash application setup for the Quantium project.

## Setup Instructions

### Prerequisites
- Python 3.9+ (this setup uses Python 3.12)
- Git
- VS Code (recommended IDE)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/vagabond-systems/quantium-starter-repo.git
   cd quantium-starter-repo
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install dash pandas
   pip install "dash[testing]"
   ```

4. **Run the test application**
   ```bash
   python app.py
   ```

## Project Structure

```
quantium-starter-repo/
├── venv/                 # Virtual environment
├── app.py               # Main Dash application
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Dependencies

- **dash**: Web framework for building analytical web applications
- **pandas**: Data manipulation and analysis library
- **plotly**: Interactive plotting library (included with dash)

## VS Code Setup

### Recommended Extensions
- Python (Microsoft)
- Pylance (Microsoft)
- Python Docstring Generator
- GitLens

### Python Interpreter Setup
1. Open VS Code in the project directory
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS)
3. Type "Python: Select Interpreter"
4. Choose the interpreter in your `venv` folder: `./venv/bin/python` (or `.\venv\Scripts\python.exe` on Windows)

## Testing

The project includes dash testing capabilities. You can run tests using pytest:

```bash
pytest
```

## Next Steps

1. Customize the `app.py` file for your specific use case
2. Add additional Python packages as needed
3. Create tests for your application
4. Deploy your application when ready

## Resources

- [Dash Documentation](https://dash.plotly.com/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Plotly Documentation](https://plotly.com/python/)
