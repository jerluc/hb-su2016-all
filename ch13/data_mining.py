LOG_DATA = [
    '2016-08-16 16:40:02,779 | INFO | Connecting to databases...',
    '2016-08-16 16:40:04,783 | INFO | Server started!',
    '2016-08-16 16:40:14,787 | INFO | User [cat] logging in...',
    '2016-08-16 16:40:15,790 | ERROR | Invalid password for user [cat]!',
    '2016-08-16 16:40:16,793 | ERROR | Invalid password for user [cat]!',
    '2016-08-16 16:40:17,796 | ERROR | Invalid password for user [cat]!',
    '2016-08-16 16:40:22,797 | FATAL | Halting server to prevent further attacks!'
]


def filter_level(desired_level):
    '''
    Filters the log data and prints only log entries whose level is
    equal to the desired_level
    '''
    pass


if __name__ == '__main__':
    filter_level('INFO')
