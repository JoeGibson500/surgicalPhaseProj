import re

def clean_phase_name(phase_name):
    """
    Cleans phase names by removing unwanted text like "(partial)" or "(attempted)" or commas.
    """
    if not isinstance(phase_name, str): # Handle nan values 
        return ""

    phase = phase_name.strip().lower()
    phase = re.sub(r"\s*\(attempt\)|\s*\(partial\)", "", phase)
    return phase
