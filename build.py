
# top_template = open('top_template.html').read()
# bottom_template = open('bottom_template.html').read()

# content = open('index.html').read()


# projects_html = top_template + content + bottom_template
# open('projects.html', 'w+').write(projects_html)


# content = open('blog.html').read()
# blog_html = top_template + content + bottom_template
# open('blog.html', 'w+').write(blog_html)


# content = open('contact.html').read()
# contact_html = top_template + content + bottom_template
# open('contact.html', 'w+').write(contact_html)






# from string import Template
# index_text = open('index.html').read()
# template = Template(index_text)



# projects_content = open('projects.html').read()
# projects_html = template.safe_substitute(
#     title="My Projects",
#     index_class="active",
#     content=projects_content,
# )
# open('projects.html', 'w+').write(projects_html)



# blog_content = open('blog.html').read()
# blog_html = template.safe_substitute(
#     title="My Blog",
#     blog_class="active",
#     content=blog_content,
# )
# open('blog.html', 'w+').write(blog_html)


# # Finally, do the same for the contact page
# contact_content = open('contact.html').read()
# contact_html = template.safe_substitute(
#     title="My Contact",
#     contact_class="active",
#     content=contact_content,
# )
# open('contact.html', 'w+').write(contact_html)


pages = [
    {
        "filename" : "content/blog.html",
        "output"   : "docs/blog.html",
        "title"    : "My Blog",
    },
    {
        "filename" : "content/projects.html",
        "output"   : "docs/projects.html",
        "title"    : "My Projects",
    },
    {
        "filename" : "content/contact.html",
        "output"   : "docs/contact.html",
        "title"    : "My Contact",

    },

]

def main():
    top = open('templates/top.html').read()
    bottom = open('templates/bottom.html').read()

    # blog_content = open('content/blog.html').read()

    # for page in pages :
    #     blog_content = open(page['docs/blog.html']).read()
    #     print(page)

    #     page_title = page ['title']
    #     print(page_title)

    # projects_content = open('content/projects.html').read()
    
    for page in pages :


        content = open(page['filename']).read()
        html = top + content + bottom
        open(page['output'], 'w+').write(html)
        
    
if __name__=='__main__':
    main()
















