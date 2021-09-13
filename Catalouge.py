"""
This is a simple catalog app
"""

import json

'''class book:
	def __init__(self, title, author):
		self.title = title
		self.author = author'''

class catalog:
	def __init__(self, books):
		self.books = books
		#new_book = input('would you like to ad a new book? (y/n)')
		self.read()
		self.sort()
		self.show()
		self.save()
		s = input('Would you like to search the books? (y/n)   ')
		if s == 'y':
			while True:
				self.search()
				s = input('Would you like to search the books again? (y/n)   ')
				if s == 'n':
					break
	
	"""def add_book(self):
		title = input("What is the book's title?   ")
		author = input("What is the book's author?   ")
		# self.books.append(book(title, author))
		self.books.append(title + ', ' + author)"""
	
	def save(self):
		with open('data.txt', 'w') as outfile:
			json.dump(self.books, outfile)
	
	def read(self):
		with open('data.txt') as json_file:
			self.old_books = json.load(json_file)
	
	def show(self):
		print('BOOKS')
		print('======')
		for book in self.books:
			print(book)
		print('Old books:')
		print('===========')
		for book in self.old_books:
			print(book)
	
	def sort(self):
		self.books.sort()
		self.old_books.sort()
	
	def search(self):

		from fuzzywuzzy import process

		# for process library,
		query = input('What book are you looking for? (write it like this: title, author)')
		qs = self.books + self.old_books

		one = process.extractOne(query, qs)
		print('Is this the book you want?')
		print(one[0])


books = []
while True:
	new_book = input('What book would you like to add?\nplease type in format: title, author   ')
	if new_book == '':
		break
	books.append(new_book)

cat = catalog(books)
