import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

PIC_DIR = os.path.expanduser('~/facesnaps')

def _ensure_pic_path():
  if not os.path.exists(PIC_DIR):
    os.mkdir(PIC_DIR)

setuptools.setup(
    name="facesnap",
    version="0.1.0",
    author="Jiri Podivin",
    author_email="jpodivin@gmail.com",
    description="Open lid, take a pic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jpodivin/facesnap",
    scripts=["./facesnap.py"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pydbus",
        "opencv-python",
        "pycairo",
        "gobject",
        "PyGObject"
    ]
)

_ensure_pic_path()
