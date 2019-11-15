
top_template = open('top_template.html').read()
bottom_template = open('bottom_template.html').read()

content = open('index.html').read()


projects_html = top_template + content + bottom_template
open('projects.html', 'w+').write(projects_html)


content = open('blog.html').read()
blog_html = top_template + content + bottom_template
open('blog.html', 'w+').write(blog_html)


content = open('contact.html').read()
contact_html = top_template + content + bottom_template
open('contact.html', 'w+').write(contact_html)






from string import Template
index_text = open('index.html').read()
template = Template(index_text)



projects_content = open('projects.html').read()
projects_html = template.safe_substitute(
    title="My Projects",
    index_class="active",
    content=projects_content,
)
open('projects.html', 'w+').write(projects_html)



blog_content = open('blog.html').read()
blog_html = template.safe_substitute(
    title="My Blog",
    blog_class="active",
    content=blog_content,
)
open('blog.html', 'w+').write(blog_html)


# Finally, do the same for the contact page
contact_content = open('contact.html').read()
contact_html = template.safe_substitute(
    title="My Contact",
    contact_class="active",
    content=contact_content,
)
open('contact.html', 'w+').write(contact_html)

