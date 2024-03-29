from libraries.classes.class_address_book import Record, AddressBook
from libraries.classes.class_colors import colors

from libraries.functions.display_contact_details import display_contact_details
from libraries.functions.a_print import a_print
from libraries.functions.show_birthdays import this_week_birthday, next_month_birthday

c_title = colors.CGREEN
c_end = colors.CEND
c_cmd = colors.CGREEN2
c_bold = colors.CBOLD
c_cmd_text = colors.CYELLOW2
c_warning = colors.CRED


def replace_empty_string_with_empty(data):
    if data == '':
        return '<no data>'
    else:
        return data


def show_command(cmd, contacts):
    if len(cmd) > 1:
        contacts = AddressBook(contacts)
        cmd.pop(0)
        if len(contacts) > 0:
            match cmd[0].lower():
                case 'contacts':
                    a_print('CONTACT LIST', prefix='  ', main_color=c_title)
                    n = 1
                    for contact in contacts.values():
                        if contact.favorite:
                            a_print('{:>5}. {:<20} {:<20}'.format(n, contact.name, replace_empty_string_with_empty(contact.note)),
                                    main_color=c_cmd,
                                    prefix='  ')
                        else:
                            a_print('{:>5}. {:<20} {:<20}'.format(n, contact.name, replace_empty_string_with_empty(contact.note)),
                                    main_color=c_title,
                                    prefix='  ')
                        n += 1
                case 'favorites':
                    a_print('FAVORITE CONTACT LIST', prefix='  ', main_color=c_title)
                    n = 1
                    for contact in contacts.values():
                        if contact.favorite:
                            a_print('{:>5}. {:<20} {:<20}'.format(n, contact.name, replace_empty_string_with_empty(contact.note)),
                                    main_color=c_cmd,
                                    prefix='  ')
                        n += 1

                case 'birthdays':
                    if len(cmd) == 3:
                        if cmd[1].lower() == 'next' and cmd[2].lower() == 'week':
                            a_print('LIST OF NEXT WEEK BIRTHDAYS', prefix='< ',
                                    main_color=c_title,
                                    prefix_color=c_cmd + c_bold)
                            this_week_birthday(contacts)
                        elif cmd[1].lower() == 'this' and cmd[2].lower() == 'month':
                            a_print('LIST OF THIS MONTH BIRTHDAYS', prefix='< ',
                                    main_color=c_title,
                                    prefix_color=c_cmd + c_bold)
                            next_month_birthday(contacts)
                    else:
                        a_print('Wrong number of parameters',
                                prefix=' WARNING! ',
                                main_color=c_title,
                                prefix_color=c_warning)

                case _:
                    match = False
                    for contact in contacts.values():
                        if contact.name.lower() == cmd[0].lower():
                            display_contact_details(contact)
                            match = True
                    if not match:
                        a_print('Parameter not found', prefix='WARNING!', main_color=c_title, prefix_color=c_warning)
        else:
            a_print("<contact list is empty>", main_color=c_cmd_text, prefix='  ')
    else:
        a_print("No parameters detected", prefix='WARNING!', main_color=c_title, prefix_color=c_warning)