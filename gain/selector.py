import re

import parsel


class Selector(object):
    def __init__(self, rule, attr=None):
        self.rule = rule
        self.attr = attr

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, self.rule)

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.rule)

    def parse_detail(self, html):
        raise NotImplementedError


class Css(Selector):
    def parse_detail(self, html):
        sel = parsel.Selector(html)
        return sel.css(self.rule)


class Xpath(Selector):
    def parse_detail(self, html):
        sel = parsel.Selector(html)
        return sel.xpath(self.rule)


class Regex(Selector):
    def parse_detail(self, html):
        sel = parsel.Selector(html)
        return sel.re(self.rule)
