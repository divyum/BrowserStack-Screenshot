import requests, json, os
class Screenshot(object):

	def __init__(self,user="user",pwd="pass"):
		self.session = requests.Session()
		self.url = "http://www.browserstack.com/screenshots"
		self.user=user
		self.pwd=pwd
		self.jobID='None'

	def get_os_browsers(self):
		''' gives the list of all browsers and os '''
		resp = self.session.get(os.path.join(self.url, 'browsers.json'))
		return resp.json()

	def get_screenshots(self,**kwargs):

		''' takes the screenshots '''

		'''-----to send arguments set arguments={...} and call the function as get_screenshots(**arguments)-----'''
		
		headers = {'content-type': 'application/json', 'Accept': 'application/json'}
		auth=(self.user,self.pwd)
		#kwargs={"browsers": [{"os": "Windows", "os_version": "7", "browser_version": "8.0", "browser": "ie"}], "url": "http://google.com"}
		resp = requests.post(self.url, data=json.dumps(kwargs), headers=headers, auth=auth)
		if resp.status_code==401:
			return 'Authentication Error'
		elif resp.status_code==403:
			return 'No Access'
		else:
			content=json.loads(resp.content)
			self.jobID=content['job_id']
			return json.loads(resp.content)

	def get_full_status(self):
		if self.jobID=='None':
			return 'No Jobs'
		self.jobID+='.json'
		resp = self.session.get(os.path.join(self.url, self.jobID))
		return json.loads(resp.content)

#s=Screenshot("divyum@browserstack.com","thinkagain")
#kwargs={"browsers": [{"os": "Windows", "os_version": "7", "browser_version": "8.0", "browser": "ie"}], "url": "http://google.com"}
#print s.get_screenshots(**kwargs)
#print s.get_full_status()