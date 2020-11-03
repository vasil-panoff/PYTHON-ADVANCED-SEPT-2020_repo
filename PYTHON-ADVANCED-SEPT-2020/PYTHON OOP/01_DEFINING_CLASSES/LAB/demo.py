def outer():
    vili = None

    def get_vili():
        return vili


    def inner():
        nonlocal vili
        vili = 36
        return get_vili


    return inner


fn_inner = outer()
fn_get_vili = fn_inner()
print(fn_get_vili())