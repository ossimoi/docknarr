class MissingSteamApiKeyError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

        self.message = message
        self.exit_code = 1

    def __str__(self):
        return 'Error: ' + self.message

