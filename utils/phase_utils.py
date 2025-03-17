import re

def clean_phase_name(phase_name):

    if not isinstance(phase_name, str):  # remove nan values
        return ""

    phase = phase_name.strip().lower()
    phase = re.sub(r"\s*\(attempt\)|\s*\(partial\)", "", phase)
    phase = re.sub(r",", "", phase)
    phase = re.sub(r"though", "through", phase)
    
    return phase
