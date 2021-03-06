from products.models import Category
from django.utils.text import slugify
import hash_info

def recurse_add(parent, depth, source):
    last_line = source.readline().rstrip()
    while last_line:
        tabs = last_line.count('\t')
        if tabs < depth:
            break
        child_categ_name = last_line.strip()
        child_categ = Category()
        child_categ.name = child_categ_name

        if parent:
            child_categ.parent = parent

        child_categ.slug = slugify(child_categ_name)
        child_categ.save()
        child_categ.my_hash = hash_info.CATEGORY.encode(child_categ.id)
        child_categ.save()
        last_line = recurse_add(child_categ, tabs+1, source)

    return last_line

def add_categories():
    infile = open('categories.txt')
    recurse_add(None, 0, infile)
