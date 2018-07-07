import argparse
import textwrap
from add_gitignore.add_gitignore import *


def get_parser(choices):
    parser = argparse.ArgumentParser(description='Generate Gitignore rules basing on GitHub"s templates collection')
    parser.add_argument("-v", "--view", help='view languages available', action='store_true')
    parser.add_argument("-l", "--language", nargs='+', help='Get the language gitignore '
                                                            'template specified:\n%s'
                                                            % (textwrap.dedent('\n'.join(choices))))
    return parser


def command_line_runner():
    choices = get_all_templates()
    parser = get_parser(choices)
    args = vars(parser.parse_args())
    if args['language']:
        create_gitignore(args['language'])
    elif args['view']:
        print choices
    else:
        parser.print_help()


if __name__ == '__main__':
    command_line_runner()