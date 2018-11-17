from collections import ChainMap as _ChainMap

LITERAL = False
DYNAMIC = True


class Template(object):

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

        return tokens

    def __init__(self, template):

        """
        Parameters
        ----------
        template : any
            Can be a string, or any indexable object

        Returns
        -------
        The number of
        """
        self.template = template
        self._build_dynamic_elements()

    def _build_dynamic_elements(self):
        tokens = self.str2tokens(self.template)
        if len(tokens) == 1:
            self.template = tokens[0][1]

    def substitute(*args, **kws):
        if not args:
            raise TypeError("descriptor 'substitute' of 'Template' object "
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
