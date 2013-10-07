from overkill.sinks import InotifySink
from overkill.sources import Source
import pyinotify
import os

class FilecountSink(InotifySink):
        add_events = pyinotify.IN_MOVED_TO | pyinotify.IN_CREATE
        remove_events = pyinotify.IN_MOVED_FROM | pyinotify.IN_DELETE
        watchdirs = []
        _count = None

        def start(self):
            if not self.watches:
                all_events = self.add_events | self.remove_events
                self.watches = [(wdir, all_events) for wdir in self.watchdirs]
            # Initialize Count
            # Asking for it initializes and sends it
            self.count
            return super().start()

        @property
        def count(self):
            if self._count is None:
                self.count = sum(sum(
                    1 for f in os.listdir(mdir)
                    if os.path.isfile(os.path.join(mdir, f))
                ) for mdir in self.watchdirs)
            return self._count

        @count.setter
        def count(self, value):
            if (self._count != value):
                self._count = value
                self.count_changed(self._count)

        def file_changed(self, path, event):
            if event & self.add_events:
                self.count += 1
            elif event & self.remove_events:
                self.count -= 1
            else:
                return

        def count_changed(self, count):
            raise NotImplementedError()

class MaildirSource(Source, FilecountSink):
    publishes = ["mailcount"]

    def __init__(self, maildirs):
        self.watchdirs = [os.path.join(mdir, "INBOX/new") for mdir in maildirs]
        super().__init__()

    def count_changed(self, count):
        self.push_updates({"mailcount": self.count})

class MailqueueSource(Source, FilecountSink):
    def __init__(self, mailqueue):
        self.watchdirs = [mailqueue]
        super().__init__()

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

