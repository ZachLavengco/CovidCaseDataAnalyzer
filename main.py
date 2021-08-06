import urllib.request
import json
import csv

# gathers country code data from website
response = urllib.request.urlopen("https://raw.githubusercontent.com/pomber/covid19/master/docs/countries.json")
contents = response.read()
country_names = json.loads(contents)

# gathers data from updated country confirmed cases
data_url = "https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json"
c = urllib.request.urlopen(data_url)
cases = c.read()
cases_data = json.loads(cases)

# puts all confirmed cases in a list per country
country_list = {}
for country in cases_data:
  country_list[country] = []
  for case_date in range(len(cases_data[country])):
    country_list[country].append(cases_data[country][case_date]["confirmed"])   

# makes list with number of days taken from 100 to 10000
from_100_to_10000 = {}    
for country in country_list:  
  count = 0 
  for confirmed in range(len(country_list[country])):
    if 100 <= country_list[country][confirmed] <= 10000:
      count += 1
    if country_list[country][confirmed] > 10000:
      break
  if country_list[country][confirmed] < 10000:
    count = 0
  if count > 0:
    from_100_to_10000[country] = []
    from_100_to_10000[country].append(count)

# block of code finds min and max days taken for above
days_min = 50  # just a starting point for loop below
country_min = ''
days_max = 0
country_max = ''
for country in from_100_to_10000:  
  if from_100_to_10000[country][0] < days_min:
    days_min = from_100_to_10000[country][0]
    country_min = country
  if from_100_to_10000[country][0] > days_max:
    days_max = from_100_to_10000[country][0]
    country_max = country

# code tests whether country code from website is in csv file
two_code_list = []
three_code_list = []
with open('country_codes.csv', mode='r') as cc:
  country_codes_list = csv.DictReader(cc)
  for dict in country_names:
    if "code" in country_names[dict]:
      two_code_list.append(country_names[dict]["code"])
    if "ZW" in two_code_list:    # breaks list so it doesn't keep iterating
      break
  for row in country_codes_list:
    country = row["Country"]
    if row['Alpha-2 code'][2:4] in two_code_list:
      three_code_list.append(row['Alpha-3 code'][2:5])

# puts Alpha-3 country codes in dictionary as keys with 2018 poplation per country as values
pop_2018 = {}
with open('population_data.csv', mode="r") as pd:
  pop_data_list = csv.DictReader(pd)
  for row in pop_data_list:
    capita_pop = row["2018"]
    country = row["Country Code"]
    if country in three_code_list:
      pop_2018[country] = capita_pop 


# takes confirmed cases numbers from 2020-2-10 and receives heighest per capita infection %
num_feb_10 = 0
country_abr_feb_10 = ''
country_full_feb_10 = ''
per_cap_feb_10 = {}
max_percap_feb_10 = 0
max_country_percap_feb_10 = ''
for country in country_list:
  num_feb_10 = country_list[country][19]
  try:
    country_full_feb_10 = country
  except:
    pass
  with open('population_data.csv', mode="r") as pd:  
    pop_data_list = csv.DictReader(pd)
    for row in pop_data_list:
      if row["Country Name"] == country_full_feb_10:
        country_abr_feb_10 = row["Country Code"]
        try:
          if pop_2018[country_abr_feb_10] != '':
            if num_feb_10/int(pop_2018[country_abr_feb_10]) > 0:
              per_cap_feb_10[country] = (num_feb_10/int(pop_2018[country_abr_feb_10])) * 100
        except:
          pass
for country in per_cap_feb_10:
  if per_cap_feb_10[country] > max_percap_feb_10:
    max_percap_feb_10 = per_cap_feb_10[country]
    max_country_percap_feb_10 = country

# takes confirmed cases numbers from 2020-3-10 and receives heighest per capita infection %
num_mar_10 = 0
country_abr_mar_10 = ''
country_full_mar_10 = ''
per_cap_mar_10 = {}
max_percap_mar_10 = 0
max_country_percap_mar_10 = ''
for country in country_list:
  num_mar_10 = country_list[country][48]
  try:
    country_full_mar_10 = country
  except:
    pass
  with open('population_data.csv', mode="r") as pd:  
    pop_data_list = csv.DictReader(pd)
    for row in pop_data_list:
      if row["Country Name"] == country_full_mar_10:
        country_abr_mar_10 = row["Country Code"]
        try:
          if pop_2018[country_abr_mar_10] != '':
            if num_mar_10/int(pop_2018[country_abr_mar_10]) > 0:
              per_cap_mar_10[country] = num_mar_10/int(pop_2018[country_abr_mar_10]) * 100
        except:
          pass
for country in per_cap_mar_10:
  if per_cap_mar_10[country] > max_percap_mar_10:
    max_percap_mar_10 = per_cap_mar_10[country]
    max_country_percap_mar_10 = country

# takes confirmed cases numbers from 2020-4-10 and receives heighest per capita infection %
num_apr_10 = 0
country_abr_apr_10 = ''
country_full_apr_10 = ''
per_cap_apr_10 = {}
max_percap_apr_10 = 0
max_country_percap_apr_10 = ''
for country in country_list:
  num_apr_10 = country_list[country][79]
  try:
    country_full_apr_10 = country
  except:
    pass
  with open('population_data.csv', mode="r") as pd:  
    pop_data_list = csv.DictReader(pd)
    for row in pop_data_list:
      if row["Country Name"] == country_full_apr_10:
        country_abr_apr_10 = row["Country Code"]
        try:
          if pop_2018[country_abr_apr_10] != '':
            if num_apr_10/int(pop_2018[country_abr_apr_10]) > 0:
              per_cap_apr_10[country] = num_apr_10/int(pop_2018[country_abr_apr_10]) * 100
        except:
          pass
for country in per_cap_apr_10:
  if per_cap_apr_10[country] > max_percap_apr_10:
    max_percap_apr_10 = per_cap_apr_10[country]
    max_country_percap_apr_10 = country


answer_list = 'project3_656470455.txt'
with open(answer_list, 'r+') as a:
  a.write(country_min)
  a.write("\n")
  minimum = str(days_min)
  a.write(minimum)
  a.write("\n")
  a.write(country_max)
  a.write("\n")
  maximum = str(days_max)
  a.write(maximum)
  a.write("\n")
  a.write(max_country_percap_feb_10)
  a.write("\n")
  maximum = str(max_percap_feb_10)
  a.write(maximum)
  a.write("\n")
  a.write(max_country_percap_mar_10)
  a.write("\n")
  maximum = str(max_percap_mar_10)
  a.write(maximum)
  a.write("\n")
  a.write(max_country_percap_apr_10)
  a.write("\n")
  maximum = str(max_percap_apr_10)
  a.write(maximum)
