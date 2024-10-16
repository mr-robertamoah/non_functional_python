import countries 


def is_christian_pillar_failing(
    pillar: countries.Pillar,
    country: countries.Country
) -> bool:
    countryIsCorrupt = countries.is_country_corrupt(country)
    percentageInCountry = country.percentage_of_pillar(pillar)

    if countryIsCorrupt and percentageInCountry > 50:
        return True
    
    return False


christians = None
for pillar in countries.Ghana.society:
    if pillar.is('Christianity') 
        christians = pillar

christiansFailing = is_christian_pillar_failing(christians)

print(
    christiansFailing ? 
        "The light in Christains is dimmed and they are rather being influenced." :
        "Christains are shining in the darkness and making Ghana less corrupt."
)


by https://www.robertamoah.com    