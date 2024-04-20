import random

# all number of chapters in old testament books
old_t = [50, 40, 27, 36, 34, 24, 21, 4, 31, 24, 22, 25, 29, 36, 10, 13, 10, 42, 150, 31, 12, 8, 66, 52, 5, 48, 12, 14, 3, 9, 1, 4, 7, 3, 3, 3, 2, 14, 4]
# all number of chapters in new testament books
new_t = [28, 16, 24, 21, 28, 16, 16, 13, 6, 6, 4, 4, 5, 3, 6, 4, 3, 1, 13, 5, 5, 3, 5, 1, 1, 1, 22]
# total number of chapters
total_chapters = sum(old_t) + sum(new_t)

#generate random chapter
randchap = random.randint(0, sum(old_t) + sum(new_t))

# print the immediate random chapterthat will later be used
print("Value of random chapter is...")
print(randchap)

# copy the random chapter for fast use
rc_copy = randchap
# index for scanning across all books
idx = 0
# scan across all books
for x in old_t + new_t:
	# remove the number of chapters from that book from the random chapter number
	rc_copy = rc_copy - x
	# exit this loop if you reach zero or go under it, #meaning the book of the random chapter has been found
	if rc_copy <= 0:
		break
	# increase the index representing the book of the bible to select
	idx = idx + 1
# print the number of the book
print("Book index: " + str(idx))
print("Book number: " + str(idx + 1))
# select the chapter of the book by taking the number of excess chapters from the number of chapters from the book
print("Chapter: " + str((old_t + new_t)[idx] + rc_copy))
# variable to hold the names of the books for printing
books = []
# fast way to generate the array for the books of the bible
booksStr = "genesis#exodus#leviticus#numbers#deuteronomy#joshua#judges#ruth#1samuel#2samuel#1kings#2kings#1chronicles#2chronicles#ezra#nehemiah#esther#job#psalms#proverbs#ecclesiastes#songofsongs#isaiah#jeremiah#lamentations#ezekiel#daniel#hosea#joel#amos#obadiah#jonah#micah#nahum#habakkuk#zephaniah#haggai#zechariah#malachi#matthew#mark#luke#john#acts#romans#1corinthians#2corinthians#galatians#ephesians#philippians#colossians#1thessalionians#2thessalonians#1timothy#2timothy#titus#philemon#hebrews#james#1peter#2peter#1john#2john#3john#jude#revelation"
# generate the books of the bible array
books = booksStr.split("#")
# print the name of the book in a user friendly way
print("Book: " + books[idx])
