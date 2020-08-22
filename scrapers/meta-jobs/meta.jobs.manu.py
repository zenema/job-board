def scrap_that_url(url):
    """
    input: expects a result page of metajob.de (e.g. https://www.metajob.de/remote)
    output: title, snippet, age, url to origin, location
    """
    try:
        page = urllib.request.urlopen(url) # connect to website
    except:
        print("Could not open URL.")
        
    soup = BeautifulSoup(page, 'html.parser') # soup object
    
    title = structure_output(soup, "rTitle")
    location = structure_output(soup, "resultLocBlock")
    age = structure_output(soup, "resultAgeBlock")
    company = structure_output(soup, "rUrl")
    description = structure_output(soup, "snippet")
    url = structure_output(soup, "rTitle", True)
    
    return title, location, age, company, description, url


def structure_output(soup, key, url=False):
    key = "^"+key
    to_scrap = re.compile(key)
    unstructured_list = soup.find_all('div', attrs={'class': to_scrap})
    output = []
    for li in unstructured_list:
        if url==True:
            output.append(get_original_job_link(li.find('a')))
        else:
            output.append(li.getText().split('\n')[0])
    return output


"""Helper function. Generate pure original job post link"""
def meta_job_redirect_to_full_link(meta_job_redirect_link):
    regex = r'(&cid*?.*)|(utm.*&)|(campaign*?.*&)' # removes affiliate backlinks#
    if "/dres/" not in meta_job_redirect_link:
        meta_job_redirect_link = str(meta_job_redirect_link)
        return re.sub(regex, "", meta_job_redirect_link)
    return re.sub(regex, "", r.get(meta_job_redirect_link).url)

"""Convert scraped metajob.de job-links into original job post links"""
def get_original_job_link(meta_job_a_tag_with_href):
    print("converting meta job link") # DEBUG
    if "/dres/" not in meta_job_a_tag_with_href['href']:
        print(meta_job_a_tag_with_href['href'])
        return meta_job_redirect_to_full_link(meta_job_a_tag_with_href)
    base_url = "https://www.metajob.de"
    if(meta_job_a_tag_with_href['href'] != "javascript:;"):
        redirect_link = base_url + meta_job_a_tag_with_href['href'] # Generate redirectional link
        # print("meta job link conversion complete!") # DEBUG
        return meta_job_redirect_to_full_link(redirect_link)

    for i in range(10):
        print(title[i])
        print( location[i])
        print( age[i])
        print(company[i])
        print(' ')
        print(description[i])
        print(' ')
        print(url[i])
        print(' ')
        print(' ')
        print(' ')