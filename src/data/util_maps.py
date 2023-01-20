
import json
import unidecode 

import os

def remove_encoding_json(path = './src/main/data/maps'):
    arr = os.listdir(path)
    for i in arr:
        file_path = path+'/'+i 
        with open(file_path, 'rb') as f:
            data = json.load(f)
            for i in data['features']:
                i['properties']['name'] = unidecode.unidecode(i['properties']['name'])
        with open(file_path, "w+") as outfile:
            json_object = json.dumps(data)
            outfile.write(json_object)

class MapUtils:
    maps = {
        "Acre" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-ac-12.json", "Municípios" : "\meshes\counties\counties-ac-12.json" , "Latitude" : -8.77, "Longitude" :  -70.55 , "Zoom" : 5},
        "Alagoas" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-al-27.json", "Municípios" : "\meshes\counties\counties-al-27.json" , "Latitude" : -9.71, "Longitude" :  -36.70 , "Zoom" : 6},
        "Amapá" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-ap-16.json", "Municípios" : "\meshes\counties\counties-ap-16.json" , "Latitude" :  1.41, "Longitude" :  -51.77 , "Zoom" : 5},
        "Amazonas" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-am-13.json", "Municípios" : "\meshes\counties\counties-am-13.json" , "Latitude" : -4.07, "Longitude" :  -64.96 , "Zoom" : 3.9},
        "Bahia" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-ba-29.json", "Municípios" : "\meshes\counties\counties-ba-29.json" , "Latitude" : -13.46, "Longitude" :  -41.61 , "Zoom" : 4.4},
        "Ceará" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-ce-23.json", "Municípios" : "\meshes\counties\counties-ce-23.json" , "Latitude" : -5.38, "Longitude" :  -39.54 , "Zoom" : 5.2},
        "Distrito Federal" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-df-53.json", "Municípios" : "\meshes\counties\counties-df-53.json" , "Latitude" : -15.83, "Longitude" :  -47.86 , "Zoom" : 7.5},
        "Espírito Santo" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-es-32.json", "Municípios" : "\meshes\counties\counties-es-32.json" , "Latitude" : -19.59, "Longitude" :  -40.34 , "Zoom" : 5.7},
        "Goiás" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-go-52.json", "Municípios" : "\meshes\counties\counties-go-52.json" , "Latitude" : -16.64, "Longitude" :  -49.31 , "Zoom" : 4.5},
        "Maranhão" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-ma-21.json", "Municípios" : "\meshes\counties\counties-ma-21.json" , "Latitude" : -5.45, "Longitude" :  -45.30 , "Zoom" : 4.5},
        "Mato Grosso" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-mt-51.json", "Municípios" : "\meshes\counties\counties-mt-51.json" , "Latitude" : -12.64, "Longitude" :  -55.42 , "Zoom" : 4},
        "Mato Grosso do Sul" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-ms-50.json", "Municípios" : "\meshes\counties\counties-ms-50.json" , "Latitude" : -20.51, "Longitude" :  -54.54 , "Zoom" : 4.5},
        "Minas Gerais" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-mg-31.json", "Municípios" : "\meshes\counties\counties-mg-31.json" , "Latitude" : -18.80, "Longitude" :  -45.38 , "Zoom" : 4.5},
        "Pará" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-pa-15.json", "Municípios" : "\meshes\counties\counties-pa-15.json" , "Latitude" : -3.53, "Longitude" :  -53.29 , "Zoom" : 4.0},
        "Paraíba" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-pb-25.json", "Municípios" : "\meshes\counties\counties-pb-25.json" , "Latitude" : -7.06, "Longitude" :  -36.75 , "Zoom" : 6.1},
        "Paraná" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-pr-41.json", "Municípios" : "\meshes\counties\counties-pr-41.json" , "Latitude" : -24.59, "Longitude" :  -51.55 , "Zoom" : 5.4},
        "Pernambuco" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-pe-26.json", "Municípios" : "\meshes\counties\counties-pe-26.json" , "Latitude" : -8.28, "Longitude" :  -38.07 , "Zoom" : 5.3},
        "Piauí" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-pi-22.json", "Municípios" : "\meshes\counties\counties-pi-22.json" , "Latitude" : -6.91, "Longitude" :  -43.68 , "Zoom" : 4.6},
        "Rio de Janeiro" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-rj-33.json", "Municípios" : "\meshes\counties\counties-rj-33.json" , "Latitude" : -22.24, "Longitude" :  -43.01 , "Zoom" : 6},
        "Rio Grande do Norte" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-rn-24.json", "Municípios" : "\meshes\counties\counties-rn-24.json" , "Latitude" : -5.72, "Longitude" :  -36.72 , "Zoom" : 6.2},
        "Rio Grande do Sul" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-rs-43.json", "Municípios" : "\meshes\counties\counties-rs-43.json" , "Latitude" : -30.41, "Longitude" :  -53.22 , "Zoom" : 4.8},
        "Rondônia" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-ro-11.json", "Municípios" : "\meshes\counties\counties-ro-11.json" , "Latitude" :  -10.8, "Longitude" :  -63.22 , "Zoom" : 5},
        "Roraima" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-rr-14.json", "Municípios" : "\meshes\counties\counties-rr-14.json" , "Latitude" : 2.02, "Longitude" :  -61.90 , "Zoom" : 4.8},
        "Santa Catarina" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-sc-42.json", "Municípios" : "\meshes\counties\counties-sc-42.json" , "Latitude" : -27.63, "Longitude" :  -50.84 , "Zoom" : 5.5},
        "São Paulo" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-sp-35.json", "Municípios" : "\meshes\counties\counties-sp-35.json" , "Latitude" : -22.55, "Longitude" :  -48.74 , "Zoom" : 4.9},
        "Sergipe" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-se-28.json", "Municípios" : "\meshes\counties\counties-se-28.json" , "Latitude" : -10.60, "Longitude" :  -37.47 , "Zoom" : 6.4},
        "Tocantins" : {"Mesorregiões" : "\meshes\mesoregions\mesoregions-to-17.json", "Municípios" : "\meshes\counties\counties-to-17.json" , "Latitude" : -9.55, "Longitude" :  -48.25 , "Zoom" : 4.5}
}