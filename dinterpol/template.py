from .attr2key import attr2key

LITERAL = False
DYNAMIC = True


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
        self.template = template
        self._build_dynamic_elements(template)

        # If there are no dynamic elements simply return he current element
        if len(self._dynamic_elements) > 0:
            self._render = self._render_eval
            return

    def _build_dynamic_elements(self, element, container=None, key=None):
        """
        """
        if container is None:
            self._dynamic_elements = []
        if element == "":
            return
        if isinstance(element, str):
            tokens = self.str2tokens(element)
            token_type, token_text = tokens[0]
            # Single token
            if len(tokens) == 1 and token_type == LITERAL:
                # Use text_token because element may contain escaped chars
                if container:
                    container[key] = token_text
                else:
                    self.template = token_text
            else:
                f_string_code = self.f_string_compile(tokens)
                self._dynamic_elements.append((container, key, f_string_code))
        elif isinstance(element, list):
            for key, value in enumerate(element):
                self._build_dynamic_elements(value, element, key)
        elif isinstance(element, dict):
            for key, value in element.items():
                self._build_dynamic_elements(value, element, key)

    def f_string_compile(self, tokens):
        token_type, token_text = tokens[0]
        if len(tokens) == 1 and tokens[0][0] == DYNAMIC:
            token_text = token_text.strip()
            token_text = attr2key(token_text)
            code = compile(
                token_text, filename='Expression: "%s"' % token_text, mode="eval"
            )
            return code
        f_string = ""
        for token_type, token_text in tokens:
            if token_type == LITERAL:
                f_string += '"""%s"""' % token_text
            else:
                token_text = token_text.strip()
                token_text = token_text.replace("{", "{{")
                token_text = token_text.replace("}", "}}")
                f_string += 'f"{%s}"' % token_text
        code = compile(f_string, filename='Expression: "%s"' % token_text, mode="eval")
        return code

    def render(self, mapping, tag=None):
        return self._render(mapping, tag)

    def _render(self, mapping, tag):
        return self.template

    def _render_eval(self, mapping, tag):

        # "_" can be used to refer to the mapping value
        if isinstance(mapping, dict):
            new_mapping = {**mapping, **{"_": mapping}, "_tag": tag}
            mapping = new_mapping
        else:
            mapping = {"_": mapping, "_tag": tag}
        container, key, f_string_code = self._dynamic_elements[0]

        if container is None:  # Container is none
            return eval(f_string_code, mapping)
        for container, key, f_string_code in self._dynamic_elements:
            container[key] = eval(f_string_code, mapping)
        return self.template

    @staticmethod
    def str2tokens(text):
        """
        This function splits a string into literal and "dynamic parts".
        Where "dynamic parts" means any sequence of chars between 2 non escaped $ symbols
        """
        #  List of tokens, where a token is a list: [is_dynamic, value]
        tokens = []
        token_type = LITERAL
        token_text = ""
        for part in text.split("$"):
            # Check if part ends with an escape char
            if part and part[-1] == "\\":
                token_text += part[:-1] + "$"
                continue
            token_text += part
            token_def = [token_type, token_text]
            tokens.append(token_def)
            token_text = ""
            token_type = token_type ^ True

        # If last element was dynamic
        if token_def[0] == DYNAMIC:
            raise ValueError("Unbalanced dynamic expression '$' on value", text)

        # Filter out void values
        tokens = [t for t in tokens if t[1] != ""]

        return tokens
