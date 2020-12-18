from google_cloud_interface import *

from multiprocessing.dummy import Pool as ThreadPool

class API_interface(object):
	"""  An interface for the API  """

	def __init__(self):
		self.google_cloud = Google_Cloud_interface()


	# Write message to feed
	def write_message(self, link, summary, publisher, company):
		res = {}

		# Send message to Pub/Sub
		result = self.google_cloud.send_message_to_pub_sub(link, summary, publisher, company)
		if result == False :
			res['status'] = 'Failed'
			res['reason'] = 'Problem in creating message.'
			return res

		res['status'] = 'Success'
		return res

	# get feed messages
	def read_feed(self, positivity_threshold):
		return self.google_cloud.get_messages(positivity_threshold)