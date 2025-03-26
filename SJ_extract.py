from bs4 import BeautifulSoup
import requests 
import os
import re
import io
from PyPDF2 import PdfReader
import re
import spacy
import stanza
import spacy_conll

#code to access all the urls of the article; note: no division for reading level and/or field


def all_links(number_of_pages):
    """
    collect links from pages.
    
    Args:
        number_of_pages (int): Number of pages to extract
    
    Returns:
        list: List of all links
    """

    list_all_links = []

    for n in range(number_of_pages):

        url = 'https://www.sciencejournalforkids.org/?sf_paged=' + str(n) #url of articles for each page of the website
        html = requests.get(url).text
        soup = BeautifulSoup(html)
        pop = soup.find_all('h3', class_ ="elementor-post__title")
        
        
        link_ = [tag.find('a').attrs['href'] for tag in pop]
        list_all_links.extend(link_)

    return list_all_links

    

all_pages_links = list(set(all_links(33))) #I eliminated the duplicates (many urls have the same science field tag and are counted multiple times 
                                      #  by the website)


def extract_pdf_text(pdf_url, max_pages=3):
    """
    Extract text from a PDF file, limited to specified number of pages.
    
    Args:
        pdf_url (str): URL of the PDF file
        max_pages (int): Maximum number of pages to extract
    
    Returns:
        str: Extracted text from the PDF
    """
    try:
        r = requests.get(pdf_url)
        f = io.BytesIO(r.content)
        reader = PdfReader(f)
        
        pages_text = []
        for pageNumber in range(min(max_pages, len(reader.pages))):
            contents = reader.pages[pageNumber].extract_text()
            pages_text.append(contents.replace("\n", ""))
        
        return "".join(pages_text)
    except Exception as e:
        print(f"Error extracting PDF text: {e}")
        return ""

def process_links(all_links):
    """
    Process links and extract PDF texts for different school levels.
    
    Args:
        all_links (list): List of page URLs to process
    """
    for i, link in enumerate(all_links):
        try:
            # Get page content
            link_req = requests.get(link).text
            soup = BeautifulSoup(link_req, 'html.parser')
            
            # Extract reading levels
            rlv = soup.find("div", class_="elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-dc348d8").find_all("a")[:2]
            read_lv = [el.get_text() for el in rlv]
            
            # Find main PDF
            kid_art = soup.find("h3", class_="elementor-icon-box-title")
            pdf_1 = kid_art.find("a").attrs["href"]
            full_text = extract_pdf_text(pdf_1)
            
            # Process for Lower high school
            if "Lower high school" in read_lv:
                with open(f"/content/drive/MyDrive/computational_linguistics/EXAM_PROJECT/SJ_TXT_DATASET/Upper_reading/Lower_high_school/LH_{i}.txt", "w", encoding="utf8") as fout:
                    fout.write(full_text)
            
            # Process for Upper high school
            if "Upper high school" in read_lv:
                with open(f"/content/drive/MyDrive/computational_linguistics/EXAM_PROJECT/SJ_TXT_DATASET/Upper_reading/Upper_high_school/UH_{i}.txt", "w", encoding="utf8") as fout:
                    fout.write(full_text)
            
            # Process for Middle school
            if "Middle school" in read_lv:
                for el in soup.find_all("h6", class_="elementor-heading-title elementor-size-small"):
                    pdf_2 = el.find("a").attrs["href"]
                    if str(pdf_2).endswith("article_lower_level.pdf"):
                        full_text_2 = extract_pdf_text(pdf_2)
                        with open(f"/content/drive/MyDrive/computational_linguistics/EXAM_PROJECT/SJ_TXT_DATASET/Lower_reading/Middle_school/MID_{i}.txt", "w", encoding="utf8") as fout:
                            fout.write(full_text_2)
                    else:
                        with open(f"/content/drive/MyDrive/computational_linguistics/EXAM_PROJECT/SJ_TXT_DATASET/Lower_reading/Middle_school/MID_{i}.txt", "w", encoding="utf8") as fout:
                            fout.write(full_text)
            
            # Process for Elementary school
            if "Elementary school" in read_lv:
                for el in soup.find_all("h6", class_="elementor-heading-title elementor-size-small"):
                    pdf_2 = el.find("a").attrs["href"]
                    if str(pdf_2).endswith("article_lower_level.pdf"):
                        full_text_2 = extract_pdf_text(pdf_2)
                        with open(f"/content/drive/MyDrive/computational_linguistics/EXAM_PROJECT/SJ_TXT_DATABASE/Lower_reading/Elementary_school/EL_{i}.txt", "w", encoding="utf8") as fout:
                            fout.write(full_text_2)
                    else:
                        with open(f"/content/drive/MyDrive/computational_linguistics/EXAM_PROJECT/SJ_TXT_DATABASE/Lower_reading/Elementary_school/EL_{i}.txt", "w", encoding="utf8") as fout:
                            fout.write(full_text)
        
        except AttributeError:
            pass


process_links(all_links)
