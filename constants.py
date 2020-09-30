# -*- coding: utf-8 -*-

import re

regexes = {
	'beatmap': re.compile(r'https?://akatsuki\.pw/(?P<type>b|d)/(?P<id>\d{1,9})/?')
}
