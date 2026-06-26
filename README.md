# In-Place BaseGrade — Cerro Colorado, Peru (Field Study)

A bilingual, single-page web report rebuilding the 2018 Municipality of Cerro Colorado
final engineering report for the Añashuayco road in the In-Place BaseGrade design system.
One intro screen, then four tabs: full report and summary, in English and Spanish.

## What's here

```
inplace-cerro-colorado/
├── index.html                  Generated page (open this in a browser)
├── assets/
│   ├── css/styles.css          All styling (design tokens, components)
│   ├── js/app.js               Tab switching + CBR bar animation
│   └── img/                     37 images: field photos, drawings, lab certificates
├── src/
│   ├── build.py                Generates index.html from the content tables inside it
│   ├── extract_images.py       Regenerates assets/img/ from the source PDF
│   └── requirements.txt        Python deps for the scripts (Pillow, numpy)
├── source/                     Put the original scanned report PDF here
└── README.md
```

The page is fully static. To view it, open `index.html` in any browser, or serve the
folder (`python3 -m http.server` from this directory) and visit the local address.

## How it rebuilds

Two independent steps. You only need them if you change something.

1. **Edit the content.** All text, tables, and translations live in the `L()` function
   and the data lists inside `src/build.py`. Change a number, a paragraph, or a
   translation there, then regenerate the page:
   ```
   python3 src/build.py
   ```
   This rewrites `index.html`. It does not touch images.

2. **Regenerate the images from the PDF.** Drop the original scanned report in `source/`
   (any `*.pdf`), then:
   ```
   pip install -r src/requirements.txt      # Pillow, numpy
   # also needs poppler-utils on the system (provides pdftoppm)
   python3 src/extract_images.py
   ```
   This re-crops every field photo, both drawings, and all twelve lab certificates and
   writes them to `assets/img/`. Crop positions are tuned to this specific scan, so if
   the source PDF is ever replaced with a different scan, the crop boxes in
   `extract_images.py` may need small adjustments.

## Design system

Pulled from the live In-Place BaseGrade landing page so this matches it part for part.
- Palette: parchment `#f6f2ec`, ink `#1c1a17`, bronze `#9a7232`, rust `#782e18`, sage, stone.
- Type: Playfair Display (headlines), Barlow (body), Barlow Condensed, DM Mono (labels).
All tokens are CSS variables at the top of `styles.css`.

## Open decisions (flagged, not yet changed)

- **Product name.** Branded throughout as "In-Place BaseGrade" in both languages. The
  original cover note used "3MB" for the Spanish and international side. If the Spanish
  tabs should read 3MB, it is a small change in `build.py`.
- **Spanish tagline.** Currently "Su Estratega de Cimentación" for "Your Groundwork
  Strategist." Adjust in `build.py` (the `tagline` and `footer_tag` keys) if preferred.

## Note on the source material

This is a translation and redesign of a third-party municipal report. The original
describes the material as a polymer; it is a certified 100 percent organic binder, and
it appears in the original under earlier names (SSPMB, Sta'bl-Soil). All measurements and
figures are reproduced exactly as recorded. The signed laboratory certificates are
included in full in `assets/img/cert17.jpg` through `cert28.jpg`.
