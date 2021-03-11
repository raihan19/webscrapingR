from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://jobs.bdjobs.com/jobsearch.asp?fcatId=4&icatId=').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('bdjob.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['job_position', 'institution', 'location', 'qualification', 'experience', 'deadline'])

containers = soup.findAll("div", {"class": "col-md-12"})


for container in containers:
    try:
        job_position = container.find('div', 'job-title-text').text.strip()
        institution = container.find('div', 'comp-name-text').text.strip()
        location = container.find('div', 'locon-text-d').text.strip()
        qualification = container.find('div', 'edu-text-d').text.strip()
        experience = container.find('div', 'exp-text-d').text.strip()
        deadline = container.find('div', 'dead-text-d').text.strip()
        csv_writer.writerow([job_position, institution, location, qualification, experience, deadline])
    except:
        pass


csv_file.close()