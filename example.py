def lambda_handler(event: dict, context):
    """
    Handles a lambda event and does some stuff with it
    :param context: Unused lambda execution context.
    :return:
    """
    #...
    LOG.debug('Initialising')
    #...
    LOG.info('Processing')
    #...
    LOG.warn('Success')
    #...
    LOG.error('Failure')
    #...
    LOG.critical('Bananas')
    #...
)
