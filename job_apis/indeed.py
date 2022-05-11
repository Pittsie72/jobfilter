import requests
import csv

cookies = {

}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'www.indeed.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15',
    'Accept-Language': 'en-us',
    'Connection': 'keep-alive',
}
# https://www.indeed.com/jobs?q=Lab%20Assistant&l=Katy%2C%20TX&vjk=4d89c2165ee972d7&advn=2337189061980106

params = {
    'q': 'Human Resource',
    'l': 'Williamstown, NJ',
  


}

response = requests.get('https://www.indeed.com/jobs', headers=headers, params=params, cookies=cookies)
def indeed_api():
    for content in response.content.decode('utf-8').split('\n'):
    # pprint.pprint(content)
    
        if 'jobmap[' in content:
            _company = content.split('cmp:')[1].split(',')[0]
            _city = content.split('city:')[1].split(',')[0]
            _zip = content.split('zip:')[1].split(',')[0]
            _title = content.split('title:')[1].split(',')[0]
            _jk = content.split('jk:')[1].split(',')[0]
            url = 'https://www.indeed.com/jobs?q=' + str(_company).replace("'", "").replace(' ','') + '&l=' + str(_city).replace("'", "").replace(' ','') + '&vjk=' + str(_jk).replace("'", "").replace(' ','')
            #https://www.indeed.com/jobs?q=Hensel+Recycling+North+America&l=Williamstown,+NJ&vjk=e85ec85c95ca5fbf
            #_total_jumps = content.split('jobmap[')[1].split(']')[0]
            with open('jobfilter.csv', 'a') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([_company,_title,_zip,None, url,'Indeed'])
        # break

# with open('indeed.html', 'wb') as f:
#     f.write(response.content)



# with open("indeed.html") as fp:
#     for line in fp:
#         if 'jobmap[' in line:
#             job_srcname = line.split('srcname:')[1].split(',')[0]
#             print(job_srcname)




