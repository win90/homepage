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

  
    for page in pages :


        content = open(page['filename']).read()
        html = top + content + bottom
        open(page['output'], 'w+').write(html)
        
    
if __name__=='__main__':
    main()
















