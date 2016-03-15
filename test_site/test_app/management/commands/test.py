from django.core.management.base import BaseCommand, CommandError
import sys
import imaplib
import email
import datetime
import base64
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

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
                    prefix = '=?UTF-8?B?'
                    suffix = '?='
                    tab = '\r\n\t'
                    msg = email.message_from_string(data[0][1])
                    new_msg=msg['Subject']
                    encoded_msg=new_msg[len(prefix):len(new_msg)-len(suffix)-len(tab)]
                    decoded_msg=base64.b64decode(encoded_msg)
                    #decode the utf-8
                    decoded = unicode(decoded_msg, 'utf8')
                    if len(encoded_msg)==0:
                        print 'Message %s: %s' % (num,new_msg)
                        print 'Raw Date:', msg['Date']
                    else:
                        print 'Message %s: %s' % (num, decoded)
                        print 'Raw Date:', msg['Date']
                    date_tuple = email.utils.parsedate_tz(msg['Date'])
                    if date_tuple:
                        local_date = datetime.datetime.fromtimestamp(
                                email.utils.mktime_tz(date_tuple))
                        print "Local Date:", \
                            local_date.strftime("%a, %d %b %Y %H:%M:%S")
                except TypeError:
                    print "TypeError - operation is not applied to the object of the appropriate type"
                except AttributeError:
                    print "AttributeError - object does not have this attribute (value or method)."
                except Exception:
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