import os
import subprocess

KOLIBRI_VERSION = '0.14.7'
KOLIBRI_PEX_URL = "https://github.com/learningequality/kolibri/releases/download/{version}/kolibri-{KOLIBRI_VERSION}-py2.py3-none-any.whl"
KOLIBRI_PEX_FILE = os.path.basename(KOLIBRI_PEX_URL.split("?")[0])  # in case ?querystr...

def download_kolibri():
    """
    Downloads and installs Kolibri `.pex` file to KOLIBRI_HOME.
    """
    subprocess.call('wget --no-verbose "{}" -O {}'.format(KOLIBRI_PEX_URL, KOLIBRI_PEX_FILE))
    assert os.path.exists(KOLIBRI_PEX_FILE)
    subprocess.call(f'unzip {KOLIBRI_PEX_FILE}')

