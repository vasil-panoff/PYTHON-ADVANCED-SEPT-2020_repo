def scopes():
    def local_scope():
        text = "local scope"

    def nonlocal_scope():
        nonlocal text
        text = "nonlocal text"

    def global_scope():
        global text
        text = "global text"

    text = "Initial"
    print(text)
    local_scope()
    print(text)
    nonlocal_scope()
    print(text)
    global_scope()
    print(text)


scopes()
print(text)