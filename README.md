# FontDownloader 🔤

A Python toolkit for managing, comparing, and downloading fonts from Google Fonts API. Designed to work seamlessly with Camoufox browser automation and font fingerprinting projects.

## 🎯 Purpose

This project helps you:
- **Download missing fonts** from Google Fonts based on browser/device requirements
- **Compare font lists** between different browsers and devices
- **Extract font names** from Camoufox cache
- **Organize fonts** by browser and device compatibility
- **Simulate mobile devices** with accurate font fingerprinting

## 📁 Project Structure

```
FontDownloader/
├── main.py                    # Main font downloader script
├── font_diff_camoufox.py     # Font comparison utility
├── getFontNames.py           # Extract fonts from Camoufox cache
├── mobile.py                 # Mobile device simulation config
├── pyproject.toml            # Project dependencies
├── .env                      # API keys (create this file)
└── Fonts/
    ├── Camoufox/
    │   └── Fonts_names.txt   # Master list of all available fonts
    ├── Common/
    │   ├── Chrome.txt        # Common Chrome fonts
    │   └── Firefox.txt       # Common Firefox fonts
    ├── Uncommon/
    │   ├── Chrome/           # Device-specific Chrome fonts
    │   └── Firefox/          # Device-specific Firefox fonts
    └── Downloaded_fonts/     # Downloaded font files (organized by browser)
```

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd FontDownloader

# Install dependencies
pip install -r requirements.txt
# OR if using uv:
uv sync
```

### 2. Setup Environment

Create a `.env` file in the project root:

```env
GOOGLE_FONTS_API_KEY=your_google_fonts_api_key_here
# OR
API_KEY=your_google_fonts_api_key_here
```

**Get your Google Fonts API key:**
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable the Google Fonts Developer API
4. Create credentials (API Key)
5. Copy the API key to your `.env` file

### 3. Basic Usage

```bash
# Download missing fonts for Chrome
python main.py

# Compare font lists and generate common/uncommon lists
python font_diff_camoufox.py

# Extract font names from Camoufox cache
python getFontNames.py
```

## 📋 Detailed Usage

### Main Font Downloader (`main.py`)

Downloads fonts from Google Fonts API that are missing from your Camoufox installation.

**Configuration:**
- Change `BROWSER = "Chrome"` to `"Firefox"` for Firefox fonts
- Fonts are downloaded to `Fonts/Downloaded_fonts/{BROWSER}/`
- Missing fonts are logged to `AAA_NOT_FOUND_FONTS.txt`

**Features:**
- ✅ Smart font name normalization
- ✅ Duplicate detection (skips already downloaded fonts)
- ✅ Only downloads fonts not in Camoufox

**Example output:**
```
📦 Fetching Google Fonts metadata...
⬇️ Downloading: Roboto (regular)
🔁 Already downloaded: Arial (regular)
❌ Not found: CustomFont

✅ Downloaded:
  - Roboto (regular)
  - Open Sans (regular)

⚠️ Not Found:
  - CustomFont
```

### Font Comparison Tool (`font_diff_camoufox.py`)

Compares browser/device font lists with your Camoufox master list.

**Configuration:**
```python
BROWSER = "Firefox"  # or "Chrome"
DEVICE = "PocoX3Pro"  # or "RedmiNote10Pro"
```

**Outputs:**
- `Fonts/Camoufox/Common/{DEVICE}_{BROWSER}.txt` - Fonts present in both lists
- `Fonts/Camoufox/Uncommon/{DEVICE}_{BROWSER}.txt` - Fonts only in device/browser

### Font Name Extractor (`getFontNames.py`)

Extracts font names from your Camoufox cache directory.

**What it does:**
- Scans `C:\Users\{USER}\AppData\Local\camoufox\camoufox\Cache\fonts`
- Removes file extensions
- Saves clean font names to `Fonts/Camoufox/Fonts_names.txt`

### Mobile Device Simulation (`mobile.py`)

Configures Camoufox to simulate mobile devices with accurate fingerprinting.

**Features:**
- 📱 Android 13 Pixel 9 simulation
- 🎨 Accurate screen dimensions and pixel ratio
- 🔊 Audio/video device simulation
- 🌍 Geolocation and timezone settings
- 🎭 WebGL and Canvas fingerprinting

## 🛠️ Advanced Configuration

### Adding New Browsers/Devices

1. **Add font list:** Create `Fonts/Common/{BROWSER}.txt`
2. **Update main.py:** Change `BROWSER = "YourBrowser"`
3. **Update comparison script:** Modify `BROWSER` and `DEVICE` variables

### Font List Format

Font list files should contain one font name per line:
```
Arial
Roboto
Open Sans
Noto Sans CJK SC
```

### Customizing Download Behavior

**Change download directory:**
```python
DOWNLOADED_FONTS_DIR = Path("your/custom/path")
```

**Download specific variants:**
```python
# In main.py, modify the variant selection logic
variant = "bold" if "bold" in files else "regular"
```

## 🔧 Dependencies

See `pyproject.toml` for dependencies.

## 📊 Font Organization

### Common Fonts
Fonts that are widely available across browsers:
- `Fonts/Common/Chrome.txt` - Common Chrome fonts both mobile devices
- `Fonts/Common/Firefox.txt` - Common Firefox fonts both mobile devices

### Uncommon Fonts
Device-specific fonts organized by browser and device:
- `Fonts/Uncommon/Chrome/PocoX3Pro.txt` - Fonts not found in Chrome on PocoX3Pro
- `Fonts/Uncommon/Firefox/PocoX3Pro.txt` - Fonts not found in Firefox on PocoX3Pro

### Downloaded Fonts
Actual font files downloaded from Google Fonts:
- `Fonts/Downloaded_fonts/Chrome/` - Downloaded fonts for Chrome
- `Fonts/Downloaded_fonts/Firefox/` - Downloaded fonts for Firefox

## 🚨 Troubleshooting

### Common Issues

**"Missing API Key" Error:**
- Ensure `.env` file exists with valid `GOOGLE_FONTS_API_KEY`
- Check API key has Google Fonts Developer API enabled

**"Font not found" Warnings:**
- Some fonts may not be available on Google Fonts
- Check `AAA_NOT_FOUND_FONTS.txt` for details
- Verify font names are correctly formatted

**Permission Errors:**
- Ensure write permissions for `Fonts/` directory
- Run with administrator privileges if needed

**Camoufox Cache Not Found:**
- Update path in `getFontNames.py` to match your system
- Ensure Camoufox is installed and has been run at least once

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

**Happy font downloading! 🎨**