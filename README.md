# Key Generator

A simple encryption key generator written in Python. It uses Python's `secrets` module for cryptographically strong randomness, and has a tkinter GUI with a confirm-on-close prompt.

## Features

- Hex keys for AES-128 and AES-256
- Base64 keys compatible with `cryptography.fernet.Fernet`
- Alphanumeric keys with custom length
- Raw bytes as hex with custom length
- Copy button for the generated key

## Requirements

- Python 3.6 or newer
- `tkinter` (included with most Python installs)
- `cryptography` (only if you use the Fernet-compatible keys)

## Usage

```bash
python key_generator.py
```

Pick a key type, enter a length if it's needed, click **Generate**, and copy the result. You'll be asked to confirm before the window closes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
