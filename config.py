# ============================================================
#  config.py — Project Coordinator alert preferences
# ============================================================

ALERT_NAME = "Ontario Project Coordinator & Canada Remote Alert"
ALERT_EMAIL = "oladeleolamide14@gmail.com"
SENDER_EMAIL = "oladeleolamide14@gmail.com"
MIN_JOBS_TO_EMAIL = 1
MAX_AGE_DAYS = 2
SEEN_JOBS_FILE = "seen_jobs_project_coord.json"

# LinkedIn searches:
# - Ontario, Canada: capture onsite / hybrid / remote Ontario roles
# - Canada: capture remote roles anywhere in Canada
LINKEDIN_SEARCH_LOCATIONS = [
    "Ontario, Canada",
    "Canada",
]

# Job Bank is Canada-focused. Keeping the location broad helps catch
# Ontario roles plus remote roles tagged at the national level.
JOBBANK_LOCATION = "Canada"
JOBBANK_DISTANCE_KM = "500"

# Search phrases sent to the scrapers.
SEARCH_KEYWORDS = [
    "Project Coordinator",
    "Senior Project Coordinator",
    "Project Control Coordinator",
    "Project Controls Coordinator",
    "PMO Coordinator",
    "Program Coordinator",
    "Implementation Coordinator",
    "Project Analyst",
    "Project Administrator",
    "Project Support Officer",
    "Project Management Coordinator",
    "PMO Analyst",
    "Delivery Coordinator",
    "Transformation Coordinator",
    "Change Coordinator",
    "Operations Coordinator",
    "Program Analyst",
    "Implementation Analyst",
]

# Title fragments used during filtering.
TITLE_FRAGMENTS = [
    "project coordinator",
    "senior project coordinator",
    "project control coordinator",
    "project controls coordinator",
    "pmo coordinator",
    "program coordinator",
    "implementation coordinator",
    "project analyst",
    "project administrator",
    "project support officer",
    "project management coordinator",
    "pmo analyst",
    "delivery coordinator",
    "transformation coordinator",
    "change coordinator",
    "operations coordinator",
    "program analyst",
    "implementation analyst",
]

# Titles we intentionally exclude so the alert stays coordinator-leaning.
SENIORITY_EXCLUDE = [
    "vice president",
    "vp",
    "chief",
    "director",
    "project manager",
    "program manager",
    "delivery manager",
    "portfolio manager",
    "intern",
    "co-op",
    "coop",
    "junior",
    "entry level",
    "entry-level",
    "student",
]

PRIORITY_COMPANIES = [
    "RBC", "Royal Bank", "TD", "TD Bank", "CIBC", "Scotiabank", "BMO",
    "Manulife", "Sun Life", "Canada Life", "Intact", "Aviva",
    "Metrolinx", "Hydro One", "Bell", "Rogers", "TELUS",
    "Shopify", "Mastercard", "IBM", "CGI", "Accenture",
    "Ontario Health", "eHealth Ontario", "TTC", "City of Toronto",
]

COMPANIES_TO_SKIP = []

REMOTE_PHRASES = [
    "remote",
    "work from home",
    "wfh",
    "virtual",
    "distributed",
    "home-based",
    "telecommute",
]

ONTARIO_LOCATION_MARKERS = [
    "ontario",
    "on, canada",
    "toronto",
    "north york",
    "scarborough",
    "etobicoke",
    "mississauga",
    "brampton",
    "oakville",
    "milton",
    "hamilton",
    "st. catharines",
    "st catharines",
    "niagara",
    "markham",
    "richmond hill",
    "vaughan",
    "ajax",
    "pickering",
    "oshawa",
    "whitby",
    "newmarket",
    "barrie",
    "waterloo",
    "kitchener",
    "cambridge",
    "guelph",
    "london",
    "windsor",
    "kingston",
    "ottawa",
    "peterborough",
    "sudbury",
    "thunder bay",
]

CANADA_LOCATION_MARKERS = [
    "canada",
    "ca",
    "alberta",
    "british columbia",
    "manitoba",
    "new brunswick",
    "newfoundland",
    "nova scotia",
    "ontario",
    "prince edward island",
    "quebec",
    "saskatchewan",
    "yukon",
    "northwest territories",
    "nunavut",
]
