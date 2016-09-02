import shlex, os, qrcode


def query(query):
    result = []
    if not query:
        result.append({
            "Title": "Enter qrcode content",
            "SubTitle": "content [-s size] [-p path] [-f filename] size [path] [filename]",
            "IcoPath": "Images/icon.png",
        })
        return result

    paramters = shlex.split(query)

    if len(paramters) == 1:  # only content
        result.append({
            "Title": "Generate content: " + paramters[0],
            "SubTitle": "Press key 'Enter' to preview qrcode",
            "IcoPath": "Images/icon.png",
            "JsonRPCAction": {
                "method": "generte_qrcode",
                "parameters": [paramters[0]],
                "dontHideAfterAction": True
            }
        })
        return result

    size, filepath, filename = None, None, None
    for k, v in zip(paramters, paramters[1:] + ["-"]):
        if k == "-s" and not v.startswith('-'):
            size = v
        elif k == "-p" and not v.startswith('-'):
            filepath = v
        elif k == "-f" and not v.startswith('-'):
            filename = v
    if not size and not filepath and not filename:
        if len(paramters) == 2 and type(paramters[1]) == int:
            size = paramters[1]
        elif len(paramters) > 2:
            filepath = paramters[2]
        if len(paramters) > 3:
            filename = paramters[3]
    filepath = get_path(filepath)
    filename = get_file(filename)

    print(filepath)
    print(filename)
    print(get_path(filepath) + get_file(filename))
    generte_qrcode([paramters[0], size, filepath, filename])


def get_path(path):
    desktop = os.path.expanduser('~\Desktop\\')
    if not path or path == "\\":
        return desktop
    if not os.path.isabs(path):
        return desktop + path + "\\"
    elif path.startswith("\\") or path.startswith("/"):
        return desktop + "\\" + path[1:] + "\\"
    return path + ("" if path.endswith("\\") else "\\")


def get_file(name):
    if not name:
        name = 'qrcode.png'
    elif not name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        name += '.png'
    return name


def generte_qrcode(*arg):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=(arg[1] if len(arg) > 1 else 20),
        border=1,
    )
    qr.add_data(arg[0])
    qr.make(fit=True)
    img = qr.make_image()

    if len(arg) == 1:
        img.show()
    elif len(arg) == 4:
        path = arg[2]
        if not os.path.isfile(path) and not os.path.exists(path):
            os.makedirs(path)
        img.save(path + arg[3])

query("test 1")
