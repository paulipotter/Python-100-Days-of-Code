from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

print(soup.title) # gets text with tag
print(soup.title.text) #strip tags

all_anchor_tags = soup.findAll(name='a')  # findAll gets all the tags that match the parameter

for tag in all_anchor_tags:
    print(tag.getText())  # getText strips the tag and prints the text
    print(tag.get('href'))  # .get() gets any attribute passed as a parameter

head = soup.find(name='h1', id='name')  # Find specific text based on tag AND id -- can also use 'class_'

# All matching items - example: use dot for class
company_url = soup.select(selector=".heading")

# First matching item - can use css,  id -> #id-text-goes here, class
company_url = soup.select_one(selector="p a")