LOG_DATA = [
    '2016-08-16 16:40:02,779 | INFO | Connecting to databases...',
    '2016-08-16 16:40:04,783 | INFO | Server started!',
    '2016-08-17 11:23:14,787 | INFO | User [cat] logging in...',
    '2016-08-17 11:23:15,790 | ERROR | Invalid password for user [cat]!',
    '2016-08-17 11:23:16,793 | ERROR | Invalid password for user [cat]!',
    '2016-08-17 11:23:17,796 | ERROR | Invalid password for user [cat]!',
    '2016-08-17 11:23:22,797 | FATAL | Halting server to prevent further attacks!'
]


def filter_date(desired_date):
    '''
    Filters the log data and prints only log entries whose date is
    equal to the desired_date
    '''
    pass


if __name__ == '__main__':
    filter_date('2016-08-17')
