# ============================================================
#  filter.py — Ontario project coordinator roles + Canada remote roles
# ============================================================

from config import (
    TITLE_FRAGMENTS,
    SENIORITY_EXCLUDE,
    PRIORITY_COMPANIES,
    COMPANIES_TO_SKIP,
    REMOTE_PHRASES,
    ONTARIO_LOCATION_MARKERS,
    CANADA_LOCATION_MARKERS,
)


def contains_any(text, terms):
    text = (text or "").lower()
    return any(term.lower() in text for term in terms)



def is_priority_company(company):
    company = (company or "").lower()
    return any(priority.lower() in company for priority in PRIORITY_COMPANIES)



def title_is_relevant(job):
    title = (job.get("title", "") or "").lower()
    return contains_any(title, TITLE_FRAGMENTS)



def is_ontario_role(job):
    location = (job.get("location", "") or "").lower()
    search_location = (job.get("search_location", "") or "").lower()
    combined = f"{location} {search_location}"
    return contains_any(combined, ONTARIO_LOCATION_MARKERS)



def is_canada_remote_role(job):
    title = (job.get("title", "") or "").lower()
    location = (job.get("location", "") or "").lower()
    search_location = (job.get("search_location", "") or "").lower()
    combined = f"{title} {location} {search_location}"
    return contains_any(combined, REMOTE_PHRASES) and contains_any(combined, CANADA_LOCATION_MARKERS)



def is_relevant(job):
    title = (job.get("title", "") or "").lower()
    company = (job.get("company", "") or "").lower()

    if any(skip.lower() in company for skip in COMPANIES_TO_SKIP):
        return False

    if any(exclude in title for exclude in SENIORITY_EXCLUDE):
        return False

    if not title_is_relevant(job):
        return False

    return is_ontario_role(job) or is_canada_remote_role(job)



def apply_filters(jobs):
    filtered = []

    for job in jobs:
        if is_relevant(job):
            job["priority"] = is_priority_company(job.get("company", ""))
            filtered.append(job)

    return filtered
