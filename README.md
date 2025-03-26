# Science Journal for Kids Text Scraper

## Project Overview

This project is designed to scrape, organize and analyze the readability of the educational texts from the Science Journal for Kids website. The primary goal is to collect and categorize scientific texts based on their readability levels for different educational stages.

## Motivation

The project aims to create a structured dataset of scientific texts that can be used for linguistic research, text complexity analysis, and educational purposes. By systematically collecting texts from various school levels, researchers can study how scientific content is adapted for different age groups.

## Features

- Web scraping using BeautifulSoup
- PDF text extraction
- Automatic text categorization by school level
- Preservation of original website structure in file organization

## Dataset Structure

The collected texts are organized into the following directory structure:
```
SJ_TXT_DATASET/
│
├── Upper_reading/
│   ├── Lower_high_school/
│   └── Upper_high_school/
│
└── Lower_reading/
    ├── Middle_school/
    └── Elementary_school/
```

### Naming Convention
- `LH_X.txt`: Lower High School texts
- `UH_X.txt`: Upper High School texts
- `MID_X.txt`: Middle School texts
- `EL_X.txt`: Elementary School texts

Where `X` represents the iteration number during scraping.

## Prerequisites

- Python 3.8+
- Libraries:
  - `requests`
  - `beautifulsoup4`
  - `pypdf`

## Installation

1. Clone the repository
2. Install required dependencies from requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```python
# Assuming you have a list of links to scrape
all_links = [...]  # Your list of webpage URLs
process_links(all_links)
```

## Limitations and Considerations

- Texts are limited to the first 3 pages of each PDF
- Readability labels are based on the website's original categorization
- Some texts may have multiple readability level indicators

## Data Collection Notes

- Texts are collected using BeautifulSoup for HTML parsing
- PDF text extraction is performed using PyPDF
- Each text is assigned a unique identifier during the scraping process
- Texts with the same ID in different folders belong to the same iteration of scraping

## Future Improvements

- Implement more robust error handling
- Add logging mechanisms
- Create a configuration file for customizable scraping parameters
- Develop additional preprocessing tools (e.g., sentence tokenization, complexity analysis)

## Potential Research Applications

- Linguistic analysis of scientific texts
- Text complexity studies
- Educational material readability assessment
- Natural language processing research

## License

[Specify your license here]

## Contact

[Your contact information or project maintainer details]
