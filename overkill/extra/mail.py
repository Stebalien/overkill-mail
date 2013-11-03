from overkill.sinks import FilecountSink
from overkill.sources import Source
import os

class MaildirSource(Source, FilecountSink):
    publishes = ["mailcount"]

    def __init__(self, maildirs):
        self.watchdirs = [os.path.join(mdir, "INBOX/new") for mdir in maildirs]
        super().__init__()

    def count_changed(self, count):
        self.push_updates({"mailcount": self.count})

class MailqueueSource(Source, FilecountSink):
    publishes = ["mailqueue"]

    def __init__(self, mailqueue):
        self.watchdirs = [mailqueue]
        super().__init__()

    def matches(self, path):
        return path[-5:] == '.mail'

    def count_changed(self, count):
        self.push_updates({"mailqueue": count})


try:
    from overkill.extra.notify import Notify
except ImportError:
    pass
else:
    from overkill.sinks import SimpleSink

    class MailNotifySink(SimpleSink, Notify):
        summary = "New Mail"
        subscription = "mailcount"
        old_count = float("inf")

        def handle_update(self, update):
            if self.old_count < update:
                self.message = "You have {} new message{}.".format(update, "" if update == 1 else "s")
                self.show()
            self.old_count = update

