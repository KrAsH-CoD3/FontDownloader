# FontDownloader

A powerful Python toolkit for managing, comparing, and downloading fonts from Google Fonts API, with special integration for Camoufox browser automation. This tool helps you maintain consistent font availability across different devices and browsers by identifying and downloading missing fonts.

## Purpose

FontDownloader is designed to solve the challenge of font consistency across different devices and browsers. It allows you to:

- **Compare font availability** between device pairs (e.g., PocoX3Pro vs RedmiNote10Pro)
- **Download missing fonts** from Google Fonts for specific browser/device combinations
- **Extract and organize font names** from Camoufox cache
- **Identify common and uncommon fonts** across different device configurations
- **Maintain a consistent font library** for web development and testing

## Features

- **Font Comparison**: Compare font availability between different devices and browsers
- **Automated Downloads**: Automatically download missing fonts from Google Fonts API
- **Font Normalization**: Intelligent font name normalization for accurate comparisons
- **Device Pair Analysis**: Analyze font differences between device pairs
- **Browser-Specific Font Management**: Handle fonts differently based on browser (Chrome, Firefox, etc.)
- **Font Organization**: Automatically organize downloaded fonts by browser and device

## Project Structure

```
FontDownloader/
├── main.py                    # Main font downloader script
├── font_diff_camoufox.py      # Compare device/browser font lists with Camoufox
├── getFontNames.py            # Extract font names from Camoufox cache
├── mobile.py                  # Mobile device simulation configuration
├── font_compare.py            # Additional font comparison utilities
├── pyproject.toml             # Project dependencies and configuration
├── uv.lock                    # Dependency lock file
└── Fonts/
    ├── CamoufoxFonts.txt      # Master list of all available fonts in Camoufox
    ├── Compared/              # Font comparison results
    │   ├── Camoufox/          # Master list of all available fonts in Camoufox
    │   │  ├── Common/         # Common fonts between Camoufox and device 
    │   │  └── Uncommon/       # Fonts not in Camoufox
    │   ├── Common/            # Common fonts between device pairs
    │   └── Uncommon/          # Fonts specific to device pairs
    │
    ├── Uncompared/            # Raw font lists before comparison
    │
    └── Downloaded_fonts/      # Downloaded font files
        └── Chrome/  # Downloaded Chrome fonts
        └── Firefox/ # Downloaded Firefox fonts
        
```

## Getting Started

### Prerequisites
### 1. Installation

```bash
git clone https://github.com/KrAsH-CoD3/FontDownloader.git
cd FontDownloader

# Install dependencies
uv sync
```

### 2. Setup Environment

Create a `.env` file in the project root:

```env
GOOGLE_FONTS_API_KEY=your_google_fonts_api_key_here
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
uv run main.py

# Compare font lists and generate common/uncommon lists
uv run font_diff_camoufox.py

# Extract font names from Camoufox cache
uv run getFontNames.py
```

## Detailed Usage

### Main Font Downloader (`main.py`)

Downloads fonts from Google Fonts API that are missing from your Camoufox installation, based on real device font pairs and browsers.

**Configuration:**
```python
BROWSER = "Firefox"  # or "Chrome"
DEVICE1 = "PocoX3Pro"
DEVICE2 = "RedmiNote10Pro"
```
- Fonts are downloaded to `Fonts/Downloaded_fonts/{DEVICE1}_{DEVICE2}/{BROWSER}/`
- Missing fonts are logged to `AAA_NOT_FOUND_FONTS.txt` in the download directory

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

Compares device pair font lists with your Camoufox master list to identify common and uncommon fonts.

**Configuration:**
```python
BROWSER = "Firefox"  # or "Chrome"
DEVICE1 = "PocoX3Pro"
DEVICE2 = "RedmiNote10Pro"
```

**Input:**
- `Fonts/Common/{DEVICE1}_{DEVICE2}/{BROWSER}Fonts.txt` - Font list for the browser/device pair

**Outputs:**
<!-- - `Fonts/Camoufox/Common/{DEVICE}_{BROWSER}.txt` - Fonts present in both lists
- `Fonts/Camoufox/Uncommon/{DEVICE}_{BROWSER}.txt` - Fonts only in device/browser -->
- `Fonts/Common/{DEVICE1}_{DEVICE2}/{BROWSER}Fonts.txt` - Common fonts (present in both Camoufox and device pair)
- `Fonts/Uncommon/{DEVICE1}_{DEVICE2}/{DEVICE1}/{BROWSER}.txt` - Fonts specific to first device
- `Fonts/Uncommon/{DEVICE1}_{DEVICE2}/{DEVICE2}/{BROWSER}.txt` - Fonts specific to second device

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

### Adding New Device Pairs/Browsers

1. **Add font lists:**
   - Create `Fonts/Common/{DEVICE1}_{DEVICE2}/{BROWSER}Fonts.txt` for common fonts
   - Create corresponding files in `Uncommon/{DEVICE1}_{DEVICE2}/` for device-specific fonts

2. **Update configuration:**
   - In `main.py` and `font_diff_camoufox.py`, update:
     ```python
     BROWSER = "YourBrowser"  # e.g., "Chrome" or "Firefox"
     DEVICE1 = "FirstDevice"  # e.g., "PocoX3Pro"
     DEVICE2 = "SecondDevice"  # e.g., "RedmiNote10Pro"
     ```

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

## Dependencies

See `pyproject.toml` for dependencies.

## Font Organization

### Font Organization

#### Common Fonts
Fonts that are common across device variants:
- `Fonts/Common/PocoX3Pro_RedmiNote10Pro/ChromeFonts.txt` - Common Chrome fonts between Poco X3 Pro and Redmi Note 10 Pro
- `Fonts/Common/PocoX3Pro_RedmiNote10Pro/FirefoxFonts.txt` - Common Firefox fonts between Poco X3 Pro and Redmi Note 10 Pro

#### Uncommon Fonts
Device-variant specific fonts that are not in the common set:
- `Fonts/Uncommon/PocoX3Pro_RedmiNote10Pro/PocoX3Pro/Chrome.txt` - Chrome fonts specific to Poco X3 Pro
- `Fonts/Uncommon/PocoX3Pro_RedmiNote10Pro/PocoX3Pro/Firefox.txt` - Firefox fonts specific to Poco X3 Pro
- `Fonts/Uncommon/PocoX3Pro_RedmiNote10Pro/RedmiNote10Pro/Chrome.txt` - Chrome fonts specific to Redmi Note 10 Pro
- `Fonts/Uncommon/PocoX3Pro_RedmiNote10Pro/RedmiNote10Pro/Firefox.txt` - Firefox fonts specific to Redmi Note 10 Pro

#### Downloaded Fonts
Actual font files downloaded from Google Fonts:
- `Fonts/Downloaded_fonts/PocoX3Pro_RedmiNote10ProChrome/` - Downloaded Chrome fonts
- `Fonts/Downloaded_fonts/PocoX3Pro_RedmiNote10ProFirefox/` - Downloaded Firefox fonts

## Troubleshooting

### Common Issues and Solutions

#### API and Authentication
**"Missing API Key" Error**
```
RuntimeError: Missing GOOGLE_FONTS_API_KEY in .env
```
- ✅ **Solution**:
  1. Verify `.env` file exists in the project root
  2. Ensure it contains: `GOOGLE_FONTS_API_KEY=your_key_here`
  3. Check for typos or extra spaces in the key
  4. Enable "Google Fonts Developer API" in Google Cloud Console

#### Font Issues
**"Font not found" Warnings**
- 🔍 **Diagnosis**:
  - Font might not exist in Google Fonts
  - Font name might be misspelled
  - Font might have a different name in Google Fonts
- 🛠️ **Solutions**:
  1. Search for the font on [Google Fonts](https://fonts.google.com/)
  2. Check `AAA_NOT_FOUND_FONTS.txt` for details
  3. Try alternative font names or variants

**Camoufox Cache Not Found**
- 🔍 **Troubleshooting**:
  1. Verify Camoufox is installed and has been run at least once
  2. Update the path in `getFontNames.py`:
     ```python
     # Windows default
     directory_path = r"C:\Users\{USER}\AppData\Local\camoufox\camoufox\Cache\fonts"
     
     # Linux/macOS alternative
     # directory_path = os.path.expanduser("~/.config/camoufox/cache/fonts")
     ```
  3. Ensure the path uses raw strings (`r"..."`) or escaped backslashes

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

**Happy font downloading! 🎨**