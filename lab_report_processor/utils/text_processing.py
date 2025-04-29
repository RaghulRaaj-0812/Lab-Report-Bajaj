import re

def parse_lab_data(text):
    tests = []
    pattern = re.compile(r'([A-Za-z\s]+)\s*([\d\.]+)\s*([\d\.]+\s*-\s*[\d\.]+)')
    
    for line in text.split('\n'):
        if match := pattern.search(line):
            test_name = match.group(1).strip()
            value = float(match.group(2))
            low, high = map(float, match.group(3).split('-'))
            
            tests.append({
                "test_name": test_name,
                "value": value,
                "bio_reference_range": f"{low}-{high}",
                "lab_test_out_of_range": not (low <= value <= high)
            })
    
    return tests