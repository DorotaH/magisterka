class  JobMarketplace:
    def  __init__(self):
        self.job_listings = list()
        self.resumes = list()

    def  post_job(self, job_title, company, requirements):
        # requirements = ['requirement1', 'requirement2']
        job = {"job_title": job_title, "company": company, "requirements": requirements}
        self.job_listings.append(job)

    def  remove_job(self, job):
        self.job_listings.remove(job)

    def  submit_resume(self, name, skills, experience):
        resume = {"name": name, "skills": skills, "experience": experience}
        self.resumes.append(resume)

    def  withdraw_resume(self, resume):
        self.resumes.remove(resume)

    def  search_jobs(self, criteria):
        matching_jobs = [job_listing for job_listing in self.job_listings if criteria.lower() in job_listing["job_title"].lower() or criteria.lower() in [r.lower() for r in job_listing["requirements"]]]
        return  matching_jobs

    def  get_job_applicants(self, job):
        applicants = [resume for resume in self.resumes if self.matches_requirements(resume, job["requirements"])]
        return  applicants

    @staticmethod
    def  matches_requirements(resume, requirements):
        for  skill in  resume["skills"]:
            if  skill not  in requirements:
                return False
        return  True
