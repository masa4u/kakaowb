import logging

DEFAULT_FORMAT = '%(asctime)s - %(levelname)-7s - %(filename)s,%(lineno)d - %(message)s'


def set_format(logger_name='kakaowb', format=None, formatter=logging.Formatter):
    format = format if format else DEFAULT_FORMAT
    _logger = logging.getLogger(logger_name)

    if _logger.handlers == []:
        h = logging.StreamHandler()
        h.setFormatter(formatter(format))
        _logger.addHandler(h)
    else:
        handler = _logger.handlers[-1]
        handler.setFormatter(formatter(format))


def get_logger(logger_name='kakaowb'):
    if logging.root.handlers:
        # extract format for code: logging.basicConfig(format=FORMAT)
        logging.root.handlers[0].flush()
        # don't use root logger
        logging.root.handlers = []
    _logger = logging.getLogger(logger_name)

    return _logger


handler = None
logger = get_logger()

if handler is None:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(DEFAULT_FORMAT))

if __name__ == '__main__':
    class MultiLineFormatter(logging.Formatter):
        def format(self, record):
            str = logging.Formatter.format(self, record)
            header, footer = str.split(record.message)
            str = str.replace('\n', '\n' + header)
            return str


    # from kakaowb.settings import ConfigSetting
    logger.warning('\n'.join(['ddfdsafdsa', 'fdsafdsa', 'fdsafdsa']))
    logger.info('ddd')
    logger.warning('\n'.join(['ddfdsafdsa', 'fdsafdsa', 'fdsafdsa']))
    set_format('kakaowb', '%(asctime)s - %(filename)s,%(lineno)d %(message)s', MultiLineFormatter)
    logger.warning('\n'.join(['ddfdsafdsa', 'fdsafdsa', 'fdsafdsa']))
    logger.warning('\n'.join(['ddfdsafdsa', 'fdsafdsa', 'fdsafdsa']))
    set_format('kakaowb', '- %(filename)s,%(lineno)d %(message)s', MultiLineFormatter)
    logger.warning('\n'.join(['ddfdsafdsa', 'fdsafdsa', 'fdsafdsa']))
