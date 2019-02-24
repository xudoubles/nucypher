from twisted.protocols.basic import LineReceiver


class Conversation(LineReceiver):

    def lineReceived(self, line):
        key_id, blah, blah = parse(line)
