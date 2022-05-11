from job_apis import ziprecruiter
from job_apis import glassdoor
from job_apis import indeed
import webbrowser
import csv
import os
import time
from tqdm import tqdm
import filterMenu
# import toml 

count=0
total_job = 0




def total_jobs_found():
    total_job = 0
    with open('jobfilter.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            total_job += 1
    print(f"{total_job -1} jobs have been found")
    return total_job


def read_csv():
    global count,jobstotals
    jobstotals = total_jobs_found()
    with open('jobfilter.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for jobfiltered in tqdm(range(0, jobstotals), desc ="progress update"):
            if jobfiltered == 0:
                # print("jobfilter.csv has been read")
                #     writer = csv.writer(csv_file)
                #     writer.writerow([joblist[0], joblist[1], joblist[2], joblist[3]])
                next(csv_reader)
            else:
                time.sleep(.1)
                jobs = next(csv_reader)
                input("Press Enter to continue...")
                webbrowser.open(jobs[2])
                filterMenu.jobfilter_menu(jobsListing = jobs)
                # jobs = list(jobs)
                # return jobsListed


          
        

# # remove the old csv_file

def removeOldCsv():
    if os.path.exists('jobfilter.csv'):
        os.remove('jobfilter.csv')
    
    # if os.path.exists('jobs_applied.csv'):
    #     os.remove('jobs_applied.csv')


    with open('jobfilter.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['hiring_company','Title','Location', 'Posted', 'get_url', 'site_name'])


def cleanUp():
    if os.path.exists('job_url.html'):
        os.remove('job_url.html')

    if os.path.exists('glassdoor_jobs.html'):
        os.remove('glassdoor_jobs.html')
        

def start_Job_Search(search,town,state):
    search = search
    town = town
    state = state
    if town == 'Williamstown':
        glassdoor.glassdoor_api(search)
    elif town == 'Steelmantown':
        glassdoor.glassdoor_api_steel(search)
    else:
        print("Glassdoor will not be searched")
    ziprecruiter.ziprecruiter_api(search = search,radius = 25,city = town,state_abbrev = state)
    indeed.indeed_api(search,town,state)




if __name__ == '__main__':
    print("Enter Search Criteria:")
    search = map(str, input())
    
    print("Enter Search Location as City,State abbreviation:")
    town, state = map(str, input().split(","))
    
    removeOldCsv()
    start_Job_Search(search,town,state)
    cleanUp()
    read_csv()