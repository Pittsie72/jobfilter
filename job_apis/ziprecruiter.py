import requests
import pprint
import csv


def ziprecruiter_api(search,radius,city,state_abbrev):
    print(search,radius,city,state_abbrev)
    
    headers = {
    'User-Agent': 'Job Search/3084 (iPhone; CPU iOS 14_0 like Mac OS X)',
    'Authorization': 'Basic YTBlZjMyZDYtN2I0Yy00MWVkLWEyODMtYTI1NDAzMzI0YTcyOg==',
}

    params = {
        'allow_currency': 'USD',
        'days': '30',
        'location': '{}, {}'.format(city,state_abbrev),
        'radius': '{}'.format(radius),
        'search': '{}'.format(search),
    }

    response = requests.get('https://api.ziprecruiter.com/jobs-app/jobs', headers=headers, params=params)
    data = response.json()
    # return data
    for job in data['jobs']:
        site_name = "ziprecruiter"
        hiring_company = job['hiring_company']['name']
        get_time = job['posted_time_friendly']
        title = job['name']
        loc = job['job_location']
        get_url = job['job_url'] 
        with open('jobfilter.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([hiring_company,title,loc, get_time, get_url,site_name])

#ziprecruiter_api(search='Human Resource',radius = 25,city= "Williamstown",state_abbrev="NJ")