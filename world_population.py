import json 

filename = 'json/population_data.json'

try:
    with open(filename) as f:
        pop_data = json.load(f)

    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            print(f'{country_name} : {str(population)}')
except FileNotFoundError:
    print('Arquivo não encontrado.')
