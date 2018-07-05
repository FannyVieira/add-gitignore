# -*- coding: utf-8 -*-

import requests
import string


BASE_URL = 'https://api.github.com'


def get_all_templates():
    """Get all gitignore templates available
        :return response: Json with templates
    """
    r = requests.get('{baseurl}/gitignore/templates'.format(baseurl=BASE_URL))
    return r.json()


def get_template_by_language(language):
    """Get the gitignore template specified,
        if not exists, None is returned, otherwise,
        a json.
        :return response: Json with specified template
    """
    language = string.capwords(language)
    r = requests.get('{baseurl}/gitignore/templates/{lang}'.format(baseurl=BASE_URL, lang=language))
    return r.json()


if __name__ == '__main__':
    print get_all_templates()
    print get_template_by_language('HASKELL')

