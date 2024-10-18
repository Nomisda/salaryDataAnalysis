import re

def extract_experience(text):
    # Regex für Jahre oder Monate in Berufserfahrung
    match_years = re.search(r'(\d+\.?\d*)\s*(Jahre?|J|j)', text)  # Erfassung von Jahren
    match_months = re.search(r'(\d+\.?\d*)\s*(Monate?|m)', text)  # Erfassung von Monaten

    experience_in_months = 0

    if match_years:
        experience_in_months += float(match_years.group(1)) * 12  # Konvertiere Jahre in Monate
    if match_months:
        experience_in_months += float(match_months.group(1))  # Füge Monate hinzu

    # Nur zurückgeben, wenn Erfahrung extrahiert werden konnte
    return experience_in_months if experience_in_months > 0 else None

# Funktion zur Extraktion des Gehalts
def extract_salary(text):
    # Regex für das Gehalt: Erstes Vorkommen einer Zahl nach "Gesamtjahresbrutto" oder eine Zahl mit "k"
    match_salary = re.search(r'Gesamtjahresbrutto:\s*[~]?(\d+[.,]?\d*[kK]?)', text)
    
    if match_salary:
        salary_str = match_salary.group(1).replace('.', '').replace(',', '.')
        
        # Prüfe, ob das Gehalt mit 'k' für Tausender angegeben wurde
        if 'k' in salary_str.lower():
            salary = float(salary_str.lower().replace('k', '')) * 1000
        else:
            salary = float(salary_str)
        
        return salary  # Rückgabe als Float
    return None
