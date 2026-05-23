import json
import os

class ReportManager:
    def __init__(self, target_name):
        self.target_name = target_name
        self.report_data = {
            "target": target_name,
            "profiles_found": [],
            "search_results": [],
            "extracted_contacts": {"emails": [], "phones": []},
            "documents_uncovered": []
        }

    def add_profile(self, profile):
        self.report_data["profiles_found"].append(profile)

    def add_search_hits(self, hits):
        self.report_data["search_results"].extend(hits)

    def update_metadata(self, meta_dict):
        self.report_data["extracted_contacts"]["emails"] = list(set(self.report_data["extracted_contacts"]["emails"] + meta_dict["emails"]))
        self.report_data["extracted_contacts"]["phones"] = list(set(self.report_data["extracted_contacts"]["phones"] + meta_dict["phones"]))
        self.report_data["documents_uncovered"] = list(set(self.report_data["documents_uncovered"] + meta_dict["documents"]))

    def save_json(self, custom_path=None):
        filename = custom_path if custom_path else f"osint_report_{self.target_name}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.report_data, f, indent=4, ensure_ascii=False)
        return filename

    def save_txt(self, custom_path=None):
        filename = custom_path if custom_path else f"osint_report_{self.target_name}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"=== OSINTHAT DIGITAL FOOTPRINT INVESTIGATION REPORT ===\n")
            f.write(f"Target Subjek: {self.target_name}\n\n")
            f.write(f"--- PROFIL TERVERIFIKASI ---\n")
            for p in self.report_data["profiles_found"]:
                f.write(f"[{p['platform']}] ({p['category']}) -> {p['url']} [Skor: {p.get('trust_score', 'N/A')}%]\n")
            f.write(f"\n--- KONTAK DIEKSTRAKSI ---\n")
            f.write(f"Emails: {', '.join(self.report_data['extracted_contacts']['emails'])}\n")
            f.write(f"Phones: {', '.join(self.report_data['extracted_contacts']['phones'])}\n")
        return filename
