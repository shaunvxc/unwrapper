#!/usr/bin/env python

def unwrap(content):
    starting_symbol = '[' if content.find('[') < content.find('{') else '{'
    ending_symbol = ']' if starting_symbol == '[' else '}'
    start = content.find(starting_symbol, 0)
    end = content.rfind(ending_symbol)

    return content[start:end+1]
