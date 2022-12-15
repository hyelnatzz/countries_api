from collections import namedtuple

continent = {'name': 'Europe'}

Country = namedtuple('Country', 'name population currency cca official_lang')

norway = Country('Norway', 5425270, 'Norwegian krone', 'NOR', 'Norwegian')
moldova = Country('Moldova', 2603813, 'Moldovan leu', 'MDA', 'Romanian')
latvia = Country('Latvia', 1842226, 'Euro', 'LVA', 'Latvian')
estonia = Country('Estonia', 1331796, 'Euro', 'EST', 'Estonian')

countries = [norway, moldova, latvia, estonia]