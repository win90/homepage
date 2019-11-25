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
            "title"    : name_only ,
            "output"   : 'docs/' + file_name,
        }
    )

print(pages)

 
template_html = open('templates/base.html').read()
template = Template(template_html)
html_result = template.render(
title = pages["title"],
content = pages["file_name"],

)


# print(pages)


# all_html_files = open(file).read()                      #jinja Templating
# template_html = open('templates/base.html').read()
# template = Template(template_html)
# html_result = template.render(
#     title = pages,
#     content = file
# )

# print(html_result)


# def main ():
#     template = open('templates/base.html').read()   #Read in the entire template

#     content = open (file).read()

#     finished_projects_page = template.replace('{{content}}',content)
#     open ('docs/blog.html','w+').write(finished_projects_page)


# if __name__=='__main__':
#     main()





# open('output.html', 'w+').write(html_result)





##########
# def main():
#     top = open('templates/top.html').read()
#     bottom = open('templates/bottom.html').read()

#     for page in pages :
#         content = open(page['filename']).read()
#         html = top + content + bottom
#         open(page['output'], 'w+').write(html)
        
    
# if __name__=='__main__':
#     main()
#########
# from string import template

# def main ():
#     template = open('templates/base.html').read()   #Read in the entire template

#     # for page in pages :

#     content = open ('content/blog.html').read()

#     finished_projects_page = template.replace('{{content}}',content)
#     open ('docs/blog.html','w+').write(finished_projects_page)


# if __name__=='__main__':
#     main()


# def main ():
#     template = open('templates/base.html').read()   #Read in the entire template

#     # for page in pages :

#     content = open ('content/projects.html').read()

#     finished_projects_page = template.replace('{{content}}',content)
#     open ('docs/projects.html','w+').write(finished_projects_page)


# if __name__=='__main__':
#     main()

# def main ():
#     template = open('templates/base.html').read()   #Read in the entire template

#     # for page in pages :

#     content = open ('content/contact.html').read()

#     finished_projects_page = template.replace('{{content}}', content)
#     open ('docs/contact.html','w+').write(finished_projects_page)


# if __name__=='__main__':
#     main()

#######
# import os
# import glob
# from jinja2 import Template



# # blog_html = open ('content/blog.html').read()
# # template_html = open ('templates/base.html').read()
# # template = Template(template_html)
# # html_result = template.render(

# #     title = 'My Blog',
# #     content = blog_html
# # )
# # open('output.html', 'w+').write(html_result)

# pages = []
# pages = [
#     {
#         "filename" : "content/blog.html",
#         "output"   : "docs/blog.html",
#         "title"    : "My Blog",
#     },
#     {
#         "filename" : "content/projects.html",
#         "output"   : "docs/projects.html",
#         "title"    : "My Projects",
#     },
#     {
#         "filename" : "content/contact.html",
#         "output"   : "docs/contact.html",
#         "title"    : "asdfkasjdhfklqsjdhfks",

#     },

# ]

# base = open("templates/base.html").read
# # file_path = ('content/projects.html')      #import os package
# # file_name = os.path.basename(file_path)
# # print(file_name)
# # name_only,extension = os.path.splitext(file_name)
# # print(name_only)

# for file_path in glob.glob('content/*html'):   #import glob discover files
#     print(file_path)

# all_html_files = glob.glob ('content/*.html')
# print(all_html_files)
# # print(pages)




# # blog_html = open('content/blog.html').read()      #jinja Templating
# # template_html = open('templates/base.html').read()
# # template = Template(template_html)
# # html_result = template.render(

# #     title = 'My blog',
# #     content = blog_html

    
# # )



# # def main ():
# #     template = open('templates/base.html').read()   #Read in the entire template

# #     # for page in pages :

# #     content = open ('content/contact.html').read()

# #     finished_projects_page = template.replace('{{content}}', content)
# #     open ('docs/contact.html','w+').write(finished_projects_page)


# # if __name__=='__main__':
# #     main()

# # open('output.html', 'w+').write(html_result)


