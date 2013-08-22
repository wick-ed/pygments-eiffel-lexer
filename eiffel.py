import re

from pygments.lexer import RegexLexer
from pygments.token import Punctuation, Text, Comment, Operator, Keyword, Number, \
     Name, String

__all__ = ['EiffelLexer']

class EiffelLexer(RegexLexer):
    """
    For Eiffel files.
    """

    name = 'Eiffel'
    aliases = ['eiffel']
    filenames = ['*.E']
    mimetypes = ['none']

    tokens = {
        'root': [
            # Strings, and other typed values
            (r'".*"', String.Double),
            (r'\'.*\'', String.Single),
            (r'[0-9]+\.[0-9]+', Number.Integer),
            (r'[0-9]+', Number.Integer),

            # single line comment
            (r'--.*\n', Comment.Single),

            # class name
            (r'(?<=class\s)[A-Z]+\b', Name.Class),

            # List of all keywords
            (r'\bclass\b', Keyword),
            (r'\bloop\b', Keyword),
            (r'\bfeature\b', Keyword),
            (r'\bensure\b', Keyword),
            (r'\brequire\b', Keyword),
            (r'\bdo\b', Keyword),
            (r'\bend\b', Keyword),
            (r'\bis\b', Keyword),
            (r'\bindexing\b', Keyword),
            (r'\bvariant\b', Keyword),
            (r'\binvariant\b', Keyword),
            (r'\bcreation\b', Keyword),
            (r'\bdescription\b', Keyword),
            (r'\binherit\b', Keyword),
            (r'\bdeferred\b', Keyword),
            (r'\bredefine\b', Keyword),
            (r'\brename\b', Keyword),
            (r'\binspect\b', Keyword),
            (r'\bretry\b', Keyword),
            (r'\brescue\b', Keyword),
            (r'\exit\b', Keyword),
            (r'\bthen\b', Keyword),
            (r'\bwhen\b', Keyword),
            (r'\bif\b', Keyword),
            (r'\belse\b', Keyword),
            (r'\blocal\b', Keyword),
            (r'\belseif\b', Keyword),
            (r'\blike\b', Keyword),

            # true and false
            (r'\btrue\b', Keyword),
            (r'\bfalse\b', Keyword),

            # list of all types
            (r'\bINTEGER\b', Keyword.Type),
            (r'\bBOOLEAN\b', Keyword.Type),
            (r'\bREAL\b', Keyword.Type),
            (r'\bDOUBLE\b', Keyword.Type),
            (r'\bCHARACTER\b', Keyword.Type),
            (r'\b[A-Z]+\b', Keyword.Type),

            # operators
            (r'\bnot\b', Operator.Word),
            (r'\+', Operator),
            (r'\-', Operator),
            (r'\*', Operator),
            (r'\/', Operator),
            (r':', Operator),
            (r'=', Operator),

            (r'\(', Text),

            # methods
            (r'[a-z][a-z0-9_]*(?=(\s*?|\S*?)\()', Name.Function),

            # variables
            (r'[a-z][a-z0-9_]*', Name.Variable),

            # Text
            (r'\s+', Text.Whitespace),
            (r'\S+', Text),
        ]
    }




