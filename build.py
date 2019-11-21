


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
#         "title"    : "My Contact",

#     },

# ]

# def main():
#     top = open('templates/top.html').read()
#     bottom = open('templates/bottom.html').read()


    
#     for page in pages :


#         content = open(page['filename']).read()
#         html = top + content + bottom
#         open(page['output'], 'w+').write(html)
        
    
# if __name__=='__main__':
#     main()

# from string import template

def main ():
    template = open('templates/base.html').read()   #Read in the entire template

    # for page in pages :

    content = open ('content/blog.html').read()

    finished_projects_page = template.replace('{{content}}',content)
    open ('docs/blog.html','w+').write(finished_projects_page)


if __name__=='__main__':
    main()


def main ():
    template = open('templates/base.html').read()   #Read in the entire template

    # for page in pages :

    content = open ('content/projects.html').read()

    finished_projects_page = template.replace('{{content}}',content)
    open ('docs/projects.html','w+').write(finished_projects_page)


if __name__=='__main__':
    main()

def main ():
    template = open('templates/base.html').read()   #Read in the entire template

    # for page in pages :

    content = open ('content/contact.html').read()

    finished_projects_page = template.replace('{{content}}', content)
    open ('docs/contact.html','w+').write(finished_projects_page)


if __name__=='__main__':
    main()









