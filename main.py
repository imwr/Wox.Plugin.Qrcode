# -*- coding: utf-8 -*-

from wox import Wox, WoxAPI
import qrcode, os, shlex


class QrcodeGenerator(Wox):
    def query(self, query):
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
                    "dontHideAfterAction": False
                }
            })
            return result

        size, filepath, filename, has_options = 400, None, None, False
        for k, v in zip(paramters, paramters[1:] + ["-"]):
            if k == "-r" and not v.startswith('-'):
                if not os.path.exists(v):
                    result.append({
                        "Title": "Image not exist",
                        "IcoPath": "Images/icon.png"
                    })
                    return result
                else:
                    result.append({
                        "Title": qrcode.decode()
                    })
                    return result

            if k == "-s" and not v.startswith('-'):
                try:
                    size = int(v)
                except:
                    result.append({
                        "Title": "Generate content: " + paramters[0],
                        "SubTitle": "Size error",
                        "IcoPath": "Images/icon.png"
                    })
                    return result
                has_options = True
            elif k == "-p" and not v.startswith('-'):
                filepath = v
                has_options = True
            elif k == "-f" and not v.startswith('-'):
                filename = v
                has_options = True
        if not has_options:
            if len(paramters) > 1:
                try:
                    size = int(paramters[1])
                except:
                    result.append({
                        "Title": "Generate content: " + paramters[0],
                        "SubTitle": "Size error",
                        "IcoPath": "Images/icon.png"
                    })
                    return result
            if len(paramters) > 2:
                filepath = paramters[2]
            if len(paramters) > 3:
                filename = paramters[3]

        filepath = self.get_path(filepath)
        filename = self.get_file(filename)
        result.append({
            "Title": "Generate content: " + paramters[0],
            "SubTitle": "Press key 'Enter' to save image*{} in {}".format(size, filepath + filename),
            "IcoPath": "Images/icon.png",
            "JsonRPCAction": {
                "method": "generte_qrcode",
                "parameters": [paramters[0], size, filepath, filename],
                "dontHideAfterAction": False
            }
        })
        return result

    def get_path(self, path):
        desktop = os.path.expanduser('~\Desktop\\')
        if not path or path == "\\":
            return desktop
        if not os.path.isabs(path):
            return desktop + path + "\\"
        elif path.startswith("\\") or path.startswith("/"):
            return desktop + "\\" + path[1:] + "\\"
        return path + ("" if path.endswith("\\") else "\\")

    def get_file(self, name):
        if not name:
            name = 'qrcode.png'
        elif not name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            name += '.png'
        return name

    def generte_qrcode(self, *arg):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=((arg[1] / 20 - arg[1] / 100) if len(arg) > 1 else 8),
            border=2,
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


if __name__ == "__main__":
    QrcodeGenerator()
