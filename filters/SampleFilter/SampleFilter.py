# sys.path.append(os.getcwd() + '/..') # Uncomment for standalone running
from abstract_filter import *


class SampleFilter(AbstractFilter):
	def __init__(self):
		self.src_language = ""
		self.trg_language = ""
		pass

	def initialize(self, source_language, target_language):
		self.num_of_scans = 0
		self.src_language = source_language
		self.trg_language = target_language
		return

	def finalize(self):
		pass

	def process_tu(self, tu, num_of_finished_scans):
		pass

	def do_after_a_full_scan(self, num_of_finished_scans):
		pass

	def decide(self, tu):
		if len(tu.src_phrase) > 0 and len(tu.trg_phrase) > 0:
			return 'accept'
		return 'reject'
