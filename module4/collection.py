#Program Name: collection.py
# Purpose of a program:
# Create a collection of authors and the years they died using a dictionary.
# Print the collection in the following format:

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"}

for author,date in authors.items():
    print(author + " died in "+ date)
    #print("%s" % author + " died in " + "%s." % date)
