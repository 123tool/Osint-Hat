import re
from bs4 import BeautifulSoup

class DataExtractor:
    def __init__(self):
        # Pola ekspresi reguler (Regex) standar industri intelijen digital
        self.email_regex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}')
        self.phone_regex = re.compile(r'\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}')
        self.doc_regex = re.compile(r'href=["\'](.*?\.pdf|.*?\.xlsx|.*?\.docx|.*?\.csv|.*?\.txt)["\']', re.IGNORECASE)

    def extract_metadata(self, html_content):
        """Membedah dokumen HTML untuk mengais metadata profil"""
        results = {
            "emails": [],
            "phones": [],
            "documents": [],
            "bio": ""
        }
        
        if not html_content:
            return results
            
        soup = BeautifulSoup(html_content, "html.parser")
        text_content = soup.get_text()

        # Ekstraksi berbasis pola
        results["emails"] = list(set(self.email_regex.findall(text_content)))
        results["phones"] = list(set([p.strip() for p in self.phone_regex.findall(text_content) if len(p.strip()) > 8]))
        results["documents"] = list(set(self.doc_regex.findall(html_content)))

        # Mencari deskripsi biografi dari tag meta media sosial universal
        meta_desc = soup.find("meta", attrs={"name": "description"}) or soup.find("meta", attrs={"property": "og:description"})
        if meta_desc and meta_desc.get("content"):
            results["bio"] = meta_desc["content"].strip()

        return results
