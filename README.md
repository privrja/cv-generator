# CV Generator

A Python-based CV generator that creates professional PDF CVs using ReportLab with a modern two-column layout featuring a sidebar with contact information and skills.

## Features

- **Professional PDF Output**: Generates high-quality PDF documents using ReportLab
- **Modern Two-Column Layout**: Sidebar with contact info, skills, and languages on the left
- **Custom Styling**: Configurable colors, fonts, and spacing
- **Photo Support**: Rounded profile photo integration
- **Responsive Design**: Clean and professional appearance suitable for job applications

## Requirements

- Python 3.7+
- reportlab
- Pillow (PIL)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cv-generator.git
cd cv-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Setup

1. Update your personal information in `generate_cv.py`:
   - Replace `PHOTO` with your photo filename
   - Update contact information (phone, email, location, LinkedIn)
   - Modify work experience, education, and skills sections

2. Place your photo in the project directory (filename should match `PHOTO` variable)

3. Run the generator:
```bash
python generate_cv.py
```

4. The CV will be generated as `Jan_Privratsky_CV_EN.pdf` (or your configured output filename)

### Configuration

Edit the `CONFIG` section in `generate_cv.py`:

- `OUTPUT`: Output PDF filename
- `PHOTO`: Input photo filename
- Colors: Customize `GREEN`, `LIGHT_BG`, `LINK_BLUE`, `SIDEBAR_BG`, `SIDEBAR_TEXT`, `SIDEBAR_ACCENT`

## Customization

### Adding Sections

Edit the `main` list to add new CV sections:

```python
main.append(Paragraph("Your Section", styles["Section"]))
main.append(Paragraph("Your content here", styles["Body"]))
```

### Modifying Colors

Update HexColor values in the CONFIG section:

```python
GREEN = colors.HexColor("#your_color")
SIDEBAR_BG = colors.HexColor("#your_color")
```

### Adjusting Layout

Modify frame dimensions in the `LAYOUT` section:

```python
sidebar_frame = Frame(
    0,
    0,
    60 * mm,  # sidebar width
    A4[1],
    ...
)
```

## Project Structure

```
cv-generator/
├── generate_cv.py          # Main CV generator script
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── photo.jpg              # Your profile photo (not included)
├── photo_rounded.png      # Generated rounded photo (auto-created)
└── Jan_Privratsky_CV_EN.pdf # Generated CV output
```

## Technical Details

- **PDF Generation**: ReportLab's SimpleDocTemplate and Frame system for precise layout control
- **Photo Processing**: PIL (Pillow) for image rounding effect
- **Styling**: Custom ParagraphStyles for consistent formatting

## License

This project is open source and available for personal use.

## Author

Jan Privratský - Data & BI Professional

## Contributing

Feel free to fork this project and submit pull requests for improvements.
