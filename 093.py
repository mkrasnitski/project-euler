import itertools
# import numexpr
operators = list(itertools.product(['+', '-', '*', '/'], repeat=3))
parentheses = [['', '', '', ''],
			   ['(', ')', '', ''],
			   ['(', ')', '(', ')'],
			   ['', '(', ')', ''],
			   ['', '', '(', ')'],
			   ['(', '', ')', ''],
			   ['((', ')', ')', ''],
			   ['(', '(', '))', ''],
			   ['', '(', '', ')'],
			   ['', '((', ')', ')'],
			   ['', '(', '(', '))']]