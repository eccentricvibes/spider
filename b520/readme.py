import os
from pprint import pprint


def readme():
    path = os.walk("./data/content")
    with open("README.md", "w+", encoding="utf-8") as f:
        for root, file, filelist in path:
            # pprint(i[2])
            filelist.sort()
            print(filelist)
            for file in filelist:
                r = os.path.join(root, file)
                print(r)
                f.write(f"[{file}]({r})\n")


if __name__ == "__main__":
    readme()
