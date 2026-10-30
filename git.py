import os, shutil

src = "/storage/emulated/0/Android/data/org.qpython.qpy3"
dst = "/storage/emulated/0/Documents/pyprojects/myproject"
os.makedirs(dst, exist_ok=True)

for name in os.listdir(src):
    if name.endswith(".py") and name != ".py":
        try:
            shutil.copyfile(os.path.join(src, name), os.path.join(dst, name))
            print("copied", name)
        except Exception as e:
            print("failed", name, e)