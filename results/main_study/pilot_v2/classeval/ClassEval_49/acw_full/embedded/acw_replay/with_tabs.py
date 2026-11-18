class JobMarketplace:
	def __init__(self):
		self.job_listings = []
		self.resumes = []

	def post_job(self, job_title, company, requirements):
		# requirements = ['requirement1', 'requirement2']
		job = {"job_title": job_title, "company": company, "requirements": requirements}
		self.job_listings.append(job)

	def remove_job(self, job):
		self.job_listings.remove(job)

	def submit_resume(self, name, skills, experience):
		resume = {"name": name, "skills": skills, "experience": experience}
		self.resumes.append(resume)

	def withdraw_resume(self, resume):
		self.resumes.remove(resume)

	def search_jobs(self, criteria):
		return [
			job_listing
			for job_listing in self.job_listings
			if criteria.lower() in job_listing["job_title"].lower()
			or criteria.lower() in [r.lower() for r in job_listing["requirements"]]
		]

	def get_job_applicants(self, job):
		return [
			resume
			for resume in self.resumes
			if self.matches_requirements(resume, job["requirements"])
		]

	@staticmethod
	def matches_requirements(resume, requirements):
		return all(skill in requirements for skill in resume["skills"])
