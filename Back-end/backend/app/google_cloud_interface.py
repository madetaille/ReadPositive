from google.cloud import pubsub_v1
import pymongo
import json
import copy
import datetime

class Google_Cloud_interface(object):
	"""An interface for Google Cloud services"""

	# Send message to Pub/Sub
	def send_message_to_pub_sub(self, link, summary, userName, company):
		try:
			PROJECT_ID = 'readpositive-298614'
			TOPIC = 'news'
			publisher = pubsub_v1.PublisherClient()
			topic_path = publisher.topic_path(PROJECT_ID, TOPIC)

			news = {}
			news['userName'] = userName
			news['link'] = link
			news['summary'] = summary
			news['company'] = company

			publisher.publish(topic_path, json.dumps(news).encode('utf-8'))
		except Exception as e:
			return False

		return True

	# get feed messages
	def get_messages(self, positivity_threshold):
		res = {}

		try:
			client = pymongo.MongoClient('mongodb+srv://mdetaille:HackForGood@cluster0.vfkfq.mongodb.net/feed?retryWrites=true&w=majority',ssl=True, ssl_cert_reqs='CERT_NONE')
			news_coll = client.feed.news.find({'sentiment':{'$gt':float(positivity_threshold)}}).sort([('datetime', -1)]).limit(20)

		except Exception as e:
			print(e)
			log_exception = {}
			log_exception['status'] = 'Failed'
			log_exception['reason'] = 'Problem in getting feed.'
			return log_exception

		res['value'] = []
		feed = []
		for message in news_coll:
			to_add = copy.copy(message)
			del to_add['_id']
			to_add['datetime'] = datetime.datetime.strftime(datetime.datetime.strptime(to_add['datetime'], '%Y-%m-%d %H:%M:%S'), '%Y-%m-%dT%H:%M:%S')
			feed.append(to_add)

		res['value'] = feed
		res['status'] = 'Success'
		return res