
import glob
import os
from jinja2 import Template


all_html_files = glob.glob('content/*.html')
print(all_html_files)



pages = []
for file in all_html_files:
    file_path = file
    print(file_path)
    



    #file_path = ('content/projects.html')      #import os package
    file_name = os.path.basename(file_path)
    print(file_name)
    name_only,extension = os.path.splitext(file_name)
    print(name_only)
    print(extension)




    pages.append(
        {
            "filename" : file_name,
            "output"   : 'docs/' + file_name,
            "title"    : name_only ,
        }
    )

print(pages)

 
template_html = open('templates/base.html').read()
template = Template(template_html)
html_result = template.render(
title = "title",
content = "file_name",
output = "output"


)



# index_html = open("docs/projects.html").read()
# template_html = open("templates/base.html").read() 
# template = Template(template_html) 
# template.render(
#     title="My_Projects",
#     content=index_html, 
# )
# # print(pages)
