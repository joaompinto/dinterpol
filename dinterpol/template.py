from collections import ChainMap as _ChainMap

LITERAL = False
DYNAMIC = True

INDEX_CODE  = 0
INDEX_KEY   = 1
VALUE_CODE  = 2

class Template(object):
    """ A template class that can be used to produce values, strings, or structured objects """

    def __init__(self, template):
        """
        Args:
            template (any): string or any iterable object used to produce a new string / object

        If an object is provided, it is iterated recursively to find all dynamic strings. A dynamic string is
        any string that contains one or more expressions between dollar signs ($).

        Template examples:                                              # Result:
            Template('$color$').render(color='blue')                    # 'blue'
            Template('$width$').render(width=12)                        # 12
            Template('My hat is $color$').render(color='red)            # 'My hat is red'
            Template('My hat is $color.upper()$').render(color='red)    # 'My hat is RED'
            Template({'color' = '$color$'}).render(color='blue)         # {'color': 'blue'}
        """
        self._dynamic_elements = []
        self._build_dynamic_elements(template)

        # If there are no dynamic elements simply return he current element
        if len(self._dynamic_elements) == 0:
            return

    def _build_dynamic_elements(self, template, path=[]):
        """
        """
        if isinstance(template, str):
            tokens = self.str2tokens(template)
            # Single token
            if len(tokens) == 1:
                token_type, token_text = tokens[0]
                if token_type == LITERAL:
                    pass
                else:
                    return compile(token_text, filename='<stdin>', mode='eval')

        return 0, template

    def render(*args, **kws):
        if not args:
            raise TypeError("descriptor 'render' of 'Template' object "
                            "needs an argument")
        self, *args = args  # allow the "self" keyword be passed
        if len(args) > 1:
            raise TypeError('Too many positional arguments')
        if not args:
            mapping = kws
        elif kws:
            mapping = _ChainMap(kws, args[0])
        else:
            mapping = None

        return self._render(mapping)

    def _render(self, mapping):
        return self.template

    def _render_eval(self, mapping):
        return eval(self.template, mapping)

    @staticmethod
    def str2tokens(text):
        """
        This function splits a string into literal and "dynamic parts".
        Where "dynamic parts" means any sequence of chars between 2 non escaped $ symbols
        """
        #  List of tokens, where a token is a list: [is_dynamic, value]
        tokens = []
        token_type = LITERAL
        token_text = ''
        for part in text.split('$'):
            # Check if part ends with an escape char
            if part and part[-1] == '\\':
                token_text += part[:-1] + '$'
                continue
            token_text += part
            token_def = [token_type, token_text]
            tokens.append(token_def)
            token_text = ''
            token_type = token_type ^ True

        # If last element was dynamic
        if token_def[0] == DYNAMIC:
            raise ValueError("Unbalanced dynamic expression '$' on value", text)

        # Filter out void values
        tokens = [t for t in tokens if t[1] is not '']

        return tokens
