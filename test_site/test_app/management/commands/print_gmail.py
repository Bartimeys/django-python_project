from django.core.management.base import BaseCommand, CommandError
import sys
import imaplib
import getpass
import email
import datetime
from email.header import decode_header

class Command(BaseCommand):
    help = 'Select from people data by education'

    def handle(self, *args, **options):
        M = imaplib.IMAP4_SSL('imap.gmail.com')

        try:
            # M.login('oliatesting@gmail.com', getpass.getpass())
            M.login('oliatesting@gmail.com', "pythontest")
        except imaplib.IMAP4.error:
            print "LOGIN FAILED!!! "

        def process_mailbox(M):
            rv, data = M.search(None, "ALL")
            if rv != 'OK':
                print "No messages found!"
                return

            for num in data[0].split():
                try:
                    rv, data = M.fetch(num, '(RFC822)')
                    if rv != 'OK':
                        print "ERROR getting message", num
                        return
                    msg = email.message_from_string(data[0][1])
                    bytes, encoding = decode_header(msg['Subject'])[0]
                    decodedMsg = bytes.decode(encoding)
                    print 'Message %s: %s' % (num, decodedMsg)
                    print 'Raw Date:', msg['Date']
                    date_tuple = email.utils.parsedate_tz(msg['Date'])
                    if date_tuple:
                        local_date = datetime.datetime.fromtimestamp(
                                email.utils.mktime_tz(date_tuple))
                        print "Local Date:", \
                            local_date.strftime("%a, %d %b %Y %H:%M:%S")
                except TypeError:
                    print "TypeError - operation is not applied to the object of the appropriate type"
                    print bytes
                except AttributeError:
                    print "AttributeError - object does not have this attribute (value or method)."
                except BaseException:
                    print "There is already a fully end system exceptions (which is better not to touch it) and start the ordinary, you can work with"

        rv, mailboxes = M.list()
        if rv == 'OK':
            print "Mailboxes:"
            print mailboxes
        rv, data = M.select("INBOX")
        if rv == 'OK':
            print "Processing mailbox...\n"
            process_mailbox(M)
            M.close()

        M.logout()
cmd = Command()
cmd.handle()