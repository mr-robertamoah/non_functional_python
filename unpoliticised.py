import countries # type: ignore

def findUnpoliticisedIssueFromCountry(country: Country) -> list: # type: ignore
    issues = []

    for issue in country.issues:
        if not issue.politicised:
            issues.append(issue.name)
    
    return issues

issues = findUnpoliticisedIssueFromCountry(countries.Ghana)

print(", ".join(issues))
