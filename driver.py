#!/usr/bin/env python3
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import shutil
import subprocess

demo_options_dict = {
    '0: Base Demo': '0-base.conf',
    '1: Static serving': '1-static.conf',
    '2: Rewrite / redirect': '2-redir.conf',
    '3: Reverse proxy': '3-proxy.conf',
    '4: Load balance': '4-lb.conf',
    '5: Compress': '5-compress.conf',
    '6: Cache': '6-cache.conf',
    '[Quit]': None
}

def run_driver():
    demo_options = WordCompleter(demo_options_dict.keys())
    while True:
        text = prompt('Demo to run (hit TAB to show): ', completer=demo_options)
        if text == '[Quit]' or not text:
            break
        print('Running %s' % text)
        run_demo(text)


def run_demo(option):
    conf = demo_options_dict[option]
    shutil.copy(conf, 'nginx/conf/nginx.conf')
    subprocess.run(['./nginx-run.sh'])

if __name__ == '__main__':
    run_driver()