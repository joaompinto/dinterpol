from tokenize import tokenize, untokenize, DOT, LPAR, LSQB, RSQB, STRING, NAME
from io import BytesIO


def attr2key(text):
    """ This function receives a text with python code, and transforms
    attribute references to key references, e.g.:
        a.b -> a["b"]
    callable attributes references will not be transformed, e.g:
        a.b.upper() -> a["b"].upper()
    """
    result = []
    token_list = list(
        tokenize(BytesIO(text.encode("utf-8")).readline)
    )  # tokenize the string
    for i, token in enumerate(token_list):
        replace_with_key_access = False
        if token.exact_type == NAME:  # Got a symbol name...
            prev_is_dot = result and result[-1].exact_type == DOT
            next_not_lpar = (
                i + 1 >= len(token_list) or token_list[i + 1].exact_type != LPAR
            )
            replace_with_key_access = prev_is_dot and next_not_lpar
        if replace_with_key_access:
            del result[-1]
            replacement_token = [
                (LSQB, "["),
                (STRING, '"%s"' % token.string),
                (RSQB, "]"),
            ]
            result.extend(replacement_token)
        else:
            result.append(token)
    return untokenize(result).decode("utf-8")
