#!/usr/bin/env python

import shutil
import time

from pathlib import Path
from argparse import ArgumentParser, Namespace, ArgumentDefaultsHelpFormatter

from chris_plugin import chris_plugin

__version__ = '1.0.0'

DISPLAY_TITLE = r"""
ChRIS Plugin Template Title
"""
INPUT_DIR = 'img'

parser = ArgumentParser(description='cli description',
                        formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='foo',
                    help='argument which sets example output file name')
parser.add_argument('-V', '--version', action='version',
                    version=f'%(prog)s {__version__}')


# copy files
def copy_files(input_dir: Path, output_dir: Path):
    print("Copying path {input_dir} to path {output_dir}".format(input_dir=input_dir, output_dir=output_dir))
    shutil.copytree(str(input_dir), str(output_dir), dirs_exist_ok=True)


# documentation: https://fnndsc.github.io/chris_plugin/chris_plugin.html#chris_plugin
@chris_plugin(
    parser=parser,
    title='Generate files',
    category='',                 # ref. https://chrisstore.co/plugins
    min_memory_limit='100Mi',    # supported units: Mi, Gi
    min_cpu_limit='1000m',       # millicores, e.g. "1000m" = 1 CPU core
    min_gpu_limit=0              # set min_gpu_limit=1 to enable GPU
)
# def main(options: Namespace, inputdir: Path, outputdir: Path):
def main(options: Namespace, outputdir: Path):
    """
    :param options: non-positional arguments parsed by the parser given to @chris_plugin
    :param inputdir: directory containing input files (read-only)
    :param outputdir: directory where to write output files
    """

    # print(DISPLAY_TITLE)
    #
    # output_file = outputdir / f'{options.name}.txt'
    # output_file.write_text('did nothing successfully!')

    copy_files(Path(INPUT_DIR), outputdir)
    # print(__name__)
    # with open("%s/%s.txt" % (str(outputdir), __name__), 'w', encoding='utf-8') as f:
    #     f.write("The time of now is " + str(time.strftime("%m-%d-%Y %H:%M:%S")))



if __name__ == '__main__':
    main()
